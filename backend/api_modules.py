import psutil
import cpuinfo
import time
import requests
import pytz
from datetime import datetime, timezone
import humanize
import socket
import ping3





# init
cpu_block = cpuinfo.get_cpu_info()
cpu = []
mem = []

class api:

    def cpu_threads():
        return psutil.cpu_count()
    
    
    def cpu_architecture():
        return cpu_block["arch"]
    
    def cpu_name():
        if psutil.LINUX:
            return cpu_block["brand"].replace(" Processor", "").replace(" 6-Core", "").replace("AMD ","").rstrip()
        else:
            return cpu_block["brand_raw"].replace("Processor", "").replace("6-Core", "").replace("AMD ","").replace("asn","asdasdsadadasdasdasdasd").rstrip()

    def cpu_arch2():
        return cpu_block["arch_string_raw"]
    def cpu_clock():
        if psutil.LINUX:
            cpu_clock = cpu_block["hz_actual_raw"][0]
        else:
            cpu_clock = cpu_block["hz_actual"][0]

        if cpu_clock / 1000000000 < 1:
            return f"{int(cpu_clock / 100000)} MHz" # MHz
        else:
            return f"{cpu_clock / 1000000000} GHz" # GHz
    
    def disk_primary_total():
        return round(psutil.disk_usage("/").total / pow(1024,3),2)
    
    def disk_primary_used():
        return round(psutil.disk_usage("/").used / pow(1024,3),2)

    def disk_primary_free():
        return round(psutil.disk_usage("/").free / pow(1024,3),2)
    
    def disk_primary_percent():
        return psutil.disk_usage("/").percent 
    
    def disk_partition():
        return psutil.disk_partitions()[0]

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

        while True:
            curr_cpu = psutil.cpu_percent(interval=1)
            cpu.append(curr_cpu)

            if len(cpu) > 20:
                cpu.pop(0)

            time.sleep(1)

    def mem_graph():
        global mem

        while True:
            curr_mem = float(psutil.virtual_memory().percent)
            mem.append(curr_mem)

            if len(mem) > 20:
                mem.pop(0)

            time.sleep(2)
    
    def public_ip():
        return requests.get('https://checkip.amazonaws.com').text.strip()

    def format_time_difference(time_difference):
        days, seconds = time_difference.days, time_difference.seconds
        hours = days * 24 + seconds // 3600
        minutes = (seconds % 3600) // 60

        if hours > 0:
            return f"{hours} hrs"
        elif minutes > 0:
            return f"{minutes} mins"
        else:
            return "just now"

    def startup():
        unix_timestamp = psutil.boot_time()
        desired_timezone = 'Europe/Budapest'
        datetime_utc = datetime.fromtimestamp(unix_timestamp, timezone.utc)
        desired_timezone = pytz.timezone(desired_timezone)
        datetime_desired_timezone = datetime_utc.astimezone(desired_timezone)
        current_time = datetime.now(desired_timezone)
        time_difference = current_time - datetime_desired_timezone

        relative_time = api.format_time_difference(time_difference)

        return relative_time

    
    def local_ip():
        return socket.gethostbyname(socket.gethostname())
    
    def hostname():
        return socket.gethostname()
    
    def ping():
        return round(ping3.ping('1.1.1.1')*1000)
    
    def swap_space():

        return psutil.swap_memory()[0] / 1000000




















# TODO
# psutil.disk_partitions()
# /(1024^3)