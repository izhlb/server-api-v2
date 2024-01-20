import psutil

print(psutil.swap_memory()[0] / 1000000)