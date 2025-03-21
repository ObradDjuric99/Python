import psutil

cpu_usage = psutil.cpu_percent(interval=1)
cores = psutil.cpu_count(logical=False)
threads = psutil.cpu_count(logical=True)

current_process = psutil.Process()
num_threads = current_process.num_threads()


print(f"Total CPU usage: {cpu_usage}")
print(f"Total physical cores: {cores}")
print(f"Total logical cores: {threads} (threads)")
print(f"Number of threads in current proccess = {num_threads}")

