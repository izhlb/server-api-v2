import socket

# Get address information for a specific host and port
addr_info = socket.getnameinfo()
print("Address Information:", addr_info)
