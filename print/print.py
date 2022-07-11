import time

for i in range(10):
    time.sleep(0.2)
    print(f"\r{i+1}/10", end="")
