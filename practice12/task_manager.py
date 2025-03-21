import psutil
import time

processes = list(psutil.process_iter(["name", "memory_percent", "cpu_percent"]))

for process in processes:
    process.cpu_percent(interval=None)

time.sleep(1)

print(f"{"Name":<55}{"Memory":<35}{"CPU":<50}{"Percentage":<10}")

for process in processes:
    print(f"Name: {process.name():<50} Memory: {process.memory_percent():<30.2f}%, CPU: {process.cpu_percent():<50}%")
