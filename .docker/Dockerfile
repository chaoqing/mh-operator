# ==============================================================================
# Stage 1: Builder - Environment Initialization, Winetricks, and App Installation
# ==============================================================================
FROM ubuntu:24.04 AS wine

# Disable interactive prompts during apt operations
ENV DEBIAN_FRONTEND=noninteractive

# Install core build dependencies and Wine environment
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        wine wine32 wine64 \
        xvfb xauth \
        wget curl cabextract unzip p7zip-full ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Deploy the latest upstream Winetricks
RUN wget -qO /usr/local/bin/winetricks https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks \
    && chmod +x /usr/local/bin/winetricks

# Enforce 64-bit Wine architecture and suppress debug logs
ENV WINEARCH=win64
ENV WINEDEBUG=-all
ENV WINEPREFIX=/opt/wine

# Initialize Wine prefix and apply Windows 10 configuration
# Inject registry patches to completely disable winedbg and crash dialogs
# Update Current User (HKCU) & System-wide (HKLM) Temp variables
# Note: xvfb-run is strictly required during image build to provide a temporary X server
RUN xvfb-run -a wineboot -u && \
    xvfb-run -a winecfg -v win10 && \
    xvfb-run -a wine reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\AeDebug" /v Auto /t REG_SZ /d 0 /f && \
    xvfb-run -a wine reg add "HKLM\Software\Microsoft\Windows NT\CurrentVersion\AeDebug" /v Debugger /t REG_SZ /d "" /f && \
    xvfb-run -a wine reg add "HKCU\Software\Wine\WineDbg" /v ShowCrashDialog /t REG_DWORD /d 0 /f && \
    rm -f "${WINEPREFIX}/dosdevices/z:" && \
    mkdir -p "${WINEPREFIX}/drive_c/Temp" && \
    wine reg add "HKCU\Environment" /v TEMP /t REG_SZ /d "C:\Temp" /f && \
    wine reg add "HKCU\Environment" /v TMP /t REG_SZ /d "C:\Temp" /f && \
    wine reg add "HKLM\System\CurrentControlSet\Control\Session Manager\Environment" /v TEMP /t REG_SZ /d "C:\Temp" /f && \
    wine reg add "HKLM\System\CurrentControlSet\Control\Session Manager\Environment" /v TMP /t REG_SZ /d "C:\Temp" /f && \
    wineserver -w

WORKDIR ${WINEPREFIX}/drive_c/Temp

# Install .NET and VC++ redistributables via Winetricks
# wineserver -w ensures all registry and file writes are committed before the layer closes
RUN xvfb-run -a winetricks -q dotnet48 vcrun2019 gdiplus corefonts && \
    wineserver -w && \
    rm -rf ~/.cache/winetricks

FROM wine as builder
ENV WINEDEBUG=+seh,+mscoree,+loaddll

ARG IPY_MSI_URL=https://github.com/IronLanguages/main/releases/download/ipy-2.7.5/IronPython-2.7.5.msi
RUN wget -qO IronPython.msi ${IPY_MSI_URL} && \
    xvfb-run -a wine msiexec /i IronPython.msi /q || test -d "${WINEPREFIX}/drive_c/Program Files (x86)/IronPython 2.7/Lib/" && \
    wineserver -w && \
    rm -rf IronPython.msi

ARG QUANT_ZIP_URL=http://172.17.0.1:8000/assets/QuantAnalysis.zip
ENV QUANT_DIR="${WINEPREFIX}/drive_c/Program Files/Agilent/MassHunter/Workstation/Quant"
# Download, extract, and install the Agilent software
# Replace the URL with your actual reachable endpoint during build
RUN wget -qO QuantAnalysis.zip ${QUANT_ZIP_URL} && \
    unzip QuantAnalysis.zip && cd QuantAnalysis && \
    xvfb-run -a wine msiexec /i QuantAnalysis.msi /q || test -d "${QUANT_DIR}/bin/" && \
    wineserver -w && \
    rm -rf "${QUANT_DIR}/help" && \
    cd ../ && rm -rf QuantAnalysis.zip QuantAnalysis

ARG PY3_EXE_URL=https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe
RUN wget -qO Python3.exe ${PY3_EXE_URL} && chmod +x Python3.exe && \
    xvfb-run -a winecfg -v win10 && \
    xvfb-run -a wine Python3.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 Include_pip=1 && \
    xvfb-run -a wine python -m pip install mh-operator[mcp] && \
    mkdir -p "${WINEPREFIX}/drive_c/Program Files (x86)/IronPython 2.7/Lib/mh_operator/legacy" && \
    cp -r "${WINEPREFIX}/drive_c/Program Files/Python310/Lib/site-packages/mh_operator/__init__.py" "${WINEPREFIX}/drive_c/Program Files (x86)/IronPython 2.7/Lib/mh_operator/__init__.py" && \
    cp -r "${WINEPREFIX}/drive_c/Program Files/Python310/Lib/site-packages/mh_operator/legacy" "${WINEPREFIX}/drive_c/Program Files (x86)/IronPython 2.7/Lib/mh_operator/legacy" && \
    wineserver -w && \
    rm -rf Python3.exe

# Inject registry patches to disable WPF hardware acceleration and force GDI
# Inject the required paths into the Current User's PATH environment variable.
RUN xvfb-run -a wine reg add 'HKCU\Environment' /v PATH /t REG_SZ /d 'C:\Program Files\Agilent\MassHunter\Workstation\Quant\bin;C:\Program Files (x86)\IronPython 2.7' /f && \
    xvfb-run -a wine reg add "HKCU\Software\Microsoft\Avalon.Graphics" /v DisableHWAcceleration /t REG_DWORD /d 1 /f && \
    xvfb-run -a wine reg add "HKCU\Software\Wine\Direct3D" /v renderer /t REG_SZ /d gdi /f && \
    wineserver -w && \
    rm -rf "${WINEPREFIX}/drive_c/users/" "${WINEPREFIX}/drive_c/Temp/"

# ==============================================================================
# Stage 2: Minimal Runtime - Final Lean Image
# ==============================================================================
FROM ubuntu:24.04

# Inherit necessary runtime environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install ONLY runtime dependencies (stripping out wget, unzip, cabextract, etc.)
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        wine wine32 wine64 xvfb \
	python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY --chmod=755 ./entrypoint.sh /usr/local/bin/entrypoint.sh

# Recreate the target user
ARG PUSER=ubuntu
ARG PUID=1000
RUN id -u $PUID 2> /dev/null || useradd -m -U -u $PUID -s /bin/bash $PUSER
USER $PUID

ENV WINEPREFIX=/opt/wine
ENV WINEARCH=win64
ENV WINEDEBUG=-all
ENV LIBGL_ALWAYS_SOFTWARE=1

# Migrate the fully prepared Wine prefix from the builder stage
COPY --from=builder --chown=$PUID:$PUID /opt/wine ${WINEPREFIX}

WORKDIR ${WINEPREFIX}/drive_c/Temp

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

# Define the container's default execution point
CMD ["wine", "cmd"]
