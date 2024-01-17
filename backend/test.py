import psutil

# Replace 'your_exe_name.exe' with the actual executable name you want to search for
target_exe_name = 'brave.exe'

# Iterate over all running processes
for process in psutil.process_iter(['pid', 'name', 'exe']):
    if process.info['exe'] == target_exe_name:
        # Process with the specified executable name found
        print("Process ID:", process.info['pid'])
        print("Process Name:", process.info['name'])
        print("Executable Path:", process.info['exe'])
        break  # Stop searching after the first match

else:
    # The loop completed without finding a matching process
    print(f"No process found with executable name: {target_exe_name}")
