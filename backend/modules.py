import psutil
import cpuinfo
import time
# init
cpu_block = cpuinfo.get_cpu_info()


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
        return f"{round(psutil.virtual_memory().total / pow(100,3),1)} GB"
    
    def mem_used():
        return f"{round(psutil.virtual_memory().used / pow(1024,3),1)} GB"
    
    def mem_percent():
        return psutil.virtual_memory().percent
    
    def mem_total_raw():
        return round(psutil.virtual_memory().total / pow(1024,3),1)
    
    def mem_asd():
        return psutil.net_io_counters()







print(api.mem_asd())













# TODO
# psutil.disk_partitions()
# /(1024^3)