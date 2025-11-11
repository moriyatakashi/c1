import psutil

# CPU利用率（全体）
cpu_percent = psutil.cpu_percent(interval=1)

# メモリ利用率
memory = psutil.virtual_memory()
memory_percent = memory.percent

print(f"CPU利用率: {cpu_percent}%")
print(f"メモリ利用率: {memory_percent}%")