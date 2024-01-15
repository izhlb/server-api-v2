import psutil
import cpuinfo
import time
import requests
import pytz
from datetime import datetime, timezone
import humanize
import threading


# init
cpu_block = cpuinfo.get_cpu_info()
cpu = []

class api:

    def cpu_threads():
        return psutil.cpu_count()
    
    def cpu_freq():
        return psutil.cpu_freq()
    
    def cpu_architecture():
        return cpu_block["arch"]
    
    def cpu_name():
        return cpu_block["brand_raw"]
    
    def cpu_clock():
        cpu_clock = cpu_block["hz_actual"][0]

        if cpu_clock / 1000000000 < 1:
            return f"{int(cpu_clock / 100000)} MHz" # MHz
        else:
            return f"{cpu_clock / 1000000000} GHz" # GHz
    
    def disk_primary_total():
        return psutil.disk_usage("/").total
    
    def disk_primary_used():
        return psutil.disk_usage("/").used

    def disk_primary_free():
        return psutil.disk_usage("/").free
    
    def disk_primary_percent():
        return psutil.disk_usage("/").percent

    def mem_total():
        return f"{round(psutil.virtual_memory().total / pow(1000,3),1)} GB"
    
    def mem_used():
        return f"{round(psutil.virtual_memory().used / pow(1024,3),1)} GB"
    
    def mem_percent():
        return psutil.virtual_memory().percent
    
    def mem_total_raw():
        return round(psutil.virtual_memory().total / pow(1024,3),1)
    
    def net_sent_data_gb():
        return round(psutil.net_io_counters().bytes_sent / pow(1024,2))
    
    def net_reci_data_gb():
        return round(psutil.net_io_counters().bytes_recv / pow(1024,2))

    def username():
        return psutil.users()[0].name
    
    def cpu_graph():
        global cpu
        global api_requests

        while True:
            curr_cpu = psutil.cpu_percent(interval=1)
            cpu.append(curr_cpu)

            if len(cpu) > 20:
                cpu.pop(0)
        

            time.sleep(1)
    
    def public_ip():
        return requests.get('https://checkip.amazonaws.com').text.strip()

    def startup():
        unix_timestamp = psutil.boot_time()
        desired_timezone = 'Europe/Budapest'
        datetime_utc = datetime.fromtimestamp(unix_timestamp, timezone.utc)
        desired_timezone = pytz.timezone(desired_timezone)
        datetime_desired_timezone = datetime_utc.astimezone(desired_timezone)
        current_time = datetime.now(desired_timezone)
        time_difference = current_time - datetime_desired_timezone
        relative_time = humanize.naturaltime(time_difference)

        return relative_time


while True:
    api.cpu_graph()
    print(cpu)
    time.sleep(1)

print(api.startup())













# TODO
# psutil.disk_partitions()
# /(1024^3)