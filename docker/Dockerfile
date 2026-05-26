# ==============================================================================
# Stage 1: Builder - Environment Initialization, Winetricks, and App Installation
# ==============================================================================
FROM ubuntu:24.04 AS builder

# Disable interactive prompts during apt operations
ENV DEBIAN_FRONTEND=noninteractive

# Enforce 64-bit Wine architecture and suppress debug logs
ENV WINEARCH=win64
ENV WINEDEBUG=-all
#ENV WINEDEBUG=+seh,+mscoree,+loaddll

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

# Create unprivileged user
RUN id -u ubuntu &> /dev/null || useradd -m -u 1000 -s /bin/bash ubuntu
USER ubuntu
WORKDIR /home/ubuntu

# Initialize Wine prefix and apply Windows 10 configuration
# Note: xvfb-run is strictly required during image build to provide a temporary X server
RUN xvfb-run -a wineboot -u && \
    xvfb-run -a winecfg -v win10 && \
    wineserver -w

# Install .NET and VC++ redistributables via Winetricks
# wineserver -w ensures all registry and file writes are committed before the layer closes
RUN xvfb-run -a winetricks -q dotnet48 vcrun2013 vcrun2019 gdiplus corefonts && \
    wineserver -w && \
    rm -rf /home/ubuntu/.cache/winetricks

# Download, extract, and install the Agilent software
# Replace the URL with your actual reachable endpoint during build
RUN wget -qO QuantAnalysis.zip http://172.17.0.1:8000/QuantAnalysis.zip && \
    unzip QuantAnalysis.zip && cd QuantAnalysis && \
    xvfb-run -a wine msiexec /i QuantAnalysis.msi /q && \
    wineserver -w && \
    cd ../ && rm -rf QuantAnalysis.zip QuantAnalysis

# Inject registry patches to disable WPF hardware acceleration and force GDI
RUN xvfb-run -a wine reg add "HKCU\Software\Microsoft\Avalon.Graphics" /v DisableHWAcceleration /t REG_DWORD /d 1 /f && \
    xvfb-run -a wine reg add "HKCU\Software\Wine\Direct3D" /v renderer /t REG_SZ /d gdi /f && \
    wineserver -w

# ==============================================================================
# Stage 2: Minimal Runtime - Final Lean Image
# ==============================================================================
FROM ubuntu:24.04

# Inherit necessary runtime environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV WINEARCH=win64
ENV WINEDEBUG=-all
ENV LIBGL_ALWAYS_SOFTWARE=1
ENV DISPLAY=:99

# Install ONLY runtime dependencies (stripping out wget, unzip, cabextract, etc.)
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        wine wine32 wine64 xvfb && \
    rm -rf /var/lib/apt/lists/*

# Recreate the target user
RUN id -u ubuntu &> /dev/null || useradd -m -u 1000 -s /bin/bash ubuntu
USER ubuntu
WORKDIR /home/ubuntu

# Migrate the fully prepared Wine prefix from the builder stage
COPY --from=builder --chown=ubuntu:ubuntu /home/ubuntu/.wine /home/ubuntu/.wine

# Generate the runtime entrypoint script
# This script spawns Xvfb in the background and hands over PID 1 to wine cmd
RUN echo '#!/bin/bash\nXvfb :99 -screen 0 1024x768x16 2>/dev/null &\ncd "/home/ubuntu/.wine/drive_c/Program Files/Agilent/MassHunter/Workstation/Quant/bin" \nexec wine cmd ""' > /home/ubuntu/entrypoint.sh && \
    chmod +x /home/ubuntu/entrypoint.sh

# Define the container's default execution point
ENTRYPOINT ["/home/ubuntu/entrypoint.sh"]
