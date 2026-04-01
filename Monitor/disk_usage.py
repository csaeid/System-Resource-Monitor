import psutil

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return {
        "percent": disk.percent,
        "total-gb": round(disk.total / 1024 ** 3, 2),
        "used-gb": round(disk.used / 1024 ** 3, 2),
        "free-gb": round(disk.free / 1024 ** 3, 2)
    }