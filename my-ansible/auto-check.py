#!/bin/python3

import os


os_info = os.popen('cat /etc/redhat-release').read().strip()
cpu_usage = os.popen("top -bn1 | grep 'Cpu(s)' | awk '{print $2 + $4}'").read().strip()
disk_usage = os.popen("df -h / | awk 'NR==2 {print $5}'").read().strip()
memory_usage = os.popen("free -h | awk 'NR==2 {print $3}'").read().strip()

print("OS 정보: ",os_info)
print("CPU 사용량: ",cpu_usage,"%")
print("Disk 사용량: ",disk_usage)
print("Memory 사용량: ",memory_usage)

