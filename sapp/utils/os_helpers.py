import os
import platform

def get_os_type():
    """Detect the current operating system."""
    return platform.system()

def check_elevation():
    """Check if the script is run with elevated privileges (Admin on Windows, sudo/root on Linux)."""
    os_type = get_os_type()

    if os_type == "Windows":
        try:
            # Windows check: only administrators can access this directory
            is_admin = os.listdir(os.path.join(os.environ['WINDIR'], 'System32', 'config'))
        except PermissionError:
            return False
        return True
    elif os_type == "Linux":
        # Linux check: ensure the script is run as root (euid 0)
        return os.geteuid() == 0
    else:
        # Unsupported OS
        return False

def is_windows():
    """Check if the OS is Windows."""
    return get_os_type() == "Windows"

def is_linux():
    """Check if the OS is Linux."""
    return get_os_type() == "Linux"
