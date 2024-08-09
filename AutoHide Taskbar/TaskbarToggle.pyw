import time
import pygetwindow as gw
import win32gui
import win32con
import subprocess
import os

# Path to the taskbartoggle.exe executable
TASKBAR_TOGGLE_PATH = os.path.join(os.path.dirname(__file__), 'taskbartoggle.exe')

def is_window_maximized(hwnd):
    """Check if a window is maximized."""
    placement = win32gui.GetWindowPlacement(hwnd)
    return placement[1] == win32con.SW_SHOWMAXIMIZED

def hide_taskbar():
    """Hide the taskbar."""
    taskbar = win32gui.FindWindow("Shell_TrayWnd", None)
    win32gui.ShowWindow(taskbar, win32con.SW_HIDE)

def show_taskbar():
    """Show the taskbar."""
    taskbar = win32gui.FindWindow("Shell_TrayWnd", None)
    win32gui.ShowWindow(taskbar, win32con.SW_SHOW)

def start_taskbar_toggle():
    """Start taskbartoggle.exe."""
    global taskbar_toggle_process
    taskbar_toggle_process = subprocess.Popen(TASKBAR_TOGGLE_PATH)

def kill_taskbar_toggle():
    """Kill taskbartoggle.exe."""
    global taskbar_toggle_process
    if taskbar_toggle_process:
        taskbar_toggle_process.terminate()
        taskbar_toggle_process = None

def komorebi_tiling():
    command = "komorebic.exe toggle-tiling"
    subprocess.run(command, shell=True)

def main():
    global taskbar_toggle_process
    taskbar_toggle_process = None
    taskbar_hidden = False

    while True:
        # Get all open windows
        windows = gw.getAllWindows()
        any_maximized = False

        for window in windows:
            hwnd = window._hWnd
            if is_window_maximized(hwnd):
                any_maximized = True
                break

        if any_maximized and not taskbar_hidden:
            komorebi_tiling()
            start_taskbar_toggle()
            taskbar_hidden = True
            print("Taskbar hidden and taskbartoggle.exe started")
        elif not any_maximized and taskbar_hidden:
            start_taskbar_toggle()
            taskbar_hidden = False
            time.sleep(1)  # Check every 2 seconds
            komorebi_tiling()
            print("Taskbar shown and taskbartoggle.exe terminated")

        time.sleep(2)  # Check every 2 seconds

if __name__ == "__main__":
    main()
