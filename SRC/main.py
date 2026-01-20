import psutil
import time
from datetime import datetime

LOG_FILE = "logs/system.log"

def get_system_health():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return cpu, ram, disk

def log_health():
    cpu, ram, disk = get_system_health()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = f"{timestamp} | CPU: {cpu}% | RAM: {ram}% | DISK: {disk}%\n"

    with open(LOG_FILE, "a") as file:
        file.write(log)

    print(log.strip())

if __name__ == "__main__":
    print("Starting Linux System Health Monitor...")
    while True:
        log_health()
        time.sleep(5)