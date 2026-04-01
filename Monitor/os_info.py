import platform

def get_os_info():
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "architecture": platform.architecture()[0],
        "processor": platform.processor()
    }