#!/bin/bash
# Fail immediately on any unhandled error
set -e

# Configure Wine and virtual display environment variables
export DISPLAY=:99
#export WINEDEBUG=-all
#export WINEARCH=win64

# Clean up any residual X11 sockets or lock files from previous unclean shutdowns
rm -f /tmp/.X11-unix/X99 /tmp/.X99-lock

# 1. Launch Xvfb in the background and explicitly capture its Process ID (PID)
# -nolisten tcp is added as a BKM security measure to restrict network exposure
Xvfb :99 -screen 0 1024x768x16 -nolisten tcp 2>/dev/null &
XVFB_PID=$!

# =====================================================================
# 2. Inject Asynchronous Watchdog Subshell
# This background process blocks and waits for Xvfb to exit. 
# If Xvfb crashes, it sends a termination signal to PID 1.
# =====================================================================
# =====================================================================
# 2. Inject Asynchronous Watchdog Subshell
# =====================================================================
(
    # Use 'kill -0' to poll process existence instead of 'wait'.
    # Bash 'wait' fails here because Xvfb is a sibling, not a child of this subshell.
    while kill -0 "$XVFB_PID" 2>/dev/null; do
        sleep 1
    done
    
    echo "[Watchdog] FATAL: Xvfb (PID $XVFB_PID) crashed unexpectedly!"
    
    # Send SIGTERM to PID 1 (FastAPI/tini) to trigger graceful container shutdown
    kill -SIGTERM 1
) &

# 3. Wait for the X11 Socket to be fully ready with a timeout fallback (BKM)
TIMEOUT_LIMIT=100  # 100 * 0.1s = 10 seconds timeout
while [ ! -e /tmp/.X11-unix/X99 ]; do
    sleep 0.1
    TIMEOUT_LIMIT=$((TIMEOUT_LIMIT - 1))
    if [ "$TIMEOUT_LIMIT" -le 0 ]; then
        echo "[Entrypoint] ERROR: Timeout waiting for Xvfb to initialize."
        # Exit with error code to trigger container restart policy
        exit 1
    fi
done

# 4. Hand over process control to the main application (Docker CMD)
exec "$@"
