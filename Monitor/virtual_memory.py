import psutil

def get_ram_info():
    ram = psutil.virtual_memory()
    return {
        "percent": ram.percent,
        "total": round(ram.total / 1024 ** 3, 2),
        "available": round(ram.available / 1024 ** 3,2),
        "used": round(ram.used / 1024 ** 3, 2)
    }