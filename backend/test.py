import psutil
print(psutil.disk_partitions()[0].mountpoint)