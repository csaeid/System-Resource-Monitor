import os
import time
import sys
sys.stdout.reconfigure(encoding='utf-8')

from Monitor.cpu_percent import get_cpu_percent
from Monitor.virtual_memory import get_ram_info 
from Monitor.disk_usage import get_disk_usage
from Monitor.os_info import get_os_info

print("Starting System Monitor... Please wait 1-2 seconds 🕵️‍♂️")    

shrek_ascii = """
⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
""".strip('\n').split('\n')

shrek_width = max(len(line) for line in shrek_ascii)

while True:
    cpu_data = get_cpu_percent()
    ram_data = get_ram_info()   
    disk_data = get_disk_usage()
    os_data = get_os_info()

    os.system('cls')

    info_panel = f"""
╭───────── SYSTEM RESOURCE MONITOR ─────────
│
│  System Information
│  🖥️ CPU : {cpu_data}%
│
│  Memory Information
│  🧠 RAM PERCENT: {ram_data['percent']}%
│  💾 TOTAL RAM: {ram_data['total']} GB
│  ✅ AVAILABLE RAM: {ram_data['available']} GB
│
│  Hardware Information
│  💿 TOTAL Disk: {disk_data['total-gb']}%
│  📦 FREE Disk: {disk_data['free-gb']} GB
|
│  System Information
│  💻 OS  : {os_data['system']} {os_data['release']} ({os_data['architecture']})
│  🏷️ Node: {os_data['node']}
│  ⚙️ CPU : {os_data['processor']}
│  🖥️ CPU : {cpu_data}%
╰──────────────────────────────────────────
If you want to stop the program, press Ctrl + C
""".strip('\n').split('\n')

    screen = ""
    
    total_lines = max(len(shrek_ascii), len(info_panel))
    
    for i in range(total_lines):
        left_side = shrek_ascii[i].ljust(shrek_width) if i < len(shrek_ascii) else " " * shrek_width
        
        right_side = info_panel[i] if i < len(info_panel) else ""
        
        screen += f"{left_side}    {right_side}\n"

    print(screen, flush=True)
    time.sleep(1)
