import psutil

memory_info = psutil.virtual_memory()

memory_bytes = memory_info.total

memory_gigabytes = memory_bytes / (1024**3) #brojke koje se dobiju su u bajtovima dakle mora se bajt u kb pa kb u mb

print(f"{memory_gigabytes:.2f}")