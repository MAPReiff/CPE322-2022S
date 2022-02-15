# I pledge my honor that I have abided by the Stevens Honor System.
# - Mitchell Reiff

# Based off of the cpu.py example from the class repository
# https://github.com/kevinwlu/iot/blob/master/lesson3/cpu.py

import psutil

print('======================= CPU =======================')
print('The number of physical cores = ', psutil.cpu_count(logical=False))
print('The number of logical threads = ', psutil.cpu_count(), "\n")

print('======================= Memory =======================')
print('The total memory in the system = ', round(psutil.virtual_memory().total/1070599167, 2), "GiB")
print('The available memory in the system = ', round(psutil.virtual_memory().available/1070599167,2 ), "GiB")
print(psutil.virtual_memory().percent, "% memory usage\n")

# SWAP stats seem to be broken on Pi but work fine on my x86_64 machines
print('The total swap memory in the system = ', round(psutil.swap_memory().total/1070599167, 2), "GiB")
print('The available swap memory in the system = ', round(psutil.swap_memory().free/1070599167, 2), "GiB")
print(psutil.swap_memory().percent, "% swap usage\n")

print('======================= Disk =======================')
print('The total disk space in the root file system = ', round(psutil.disk_usage('/').total/1070599167, 2), "GiB")
print('The available disk space in the root file system = ', round(psutil.disk_usage('/').free/1070599167, 2), "GiB")
print(psutil.disk_usage('/').percent, "% disk usage\n")

print('======================= Battery =======================')
if psutil.sensors_battery():
  if psutil.sensors_battery().power_plugged:
    print('The battery is currently plugged in and is charging')
  else:
    print('The battery is currently not plugged in and is not charging')

  print('The battery is currently at', round(psutil.sensors_battery().percent,2), '%')
  
else:
  print('No battery found')
