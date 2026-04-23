import time

seconds = int(input("Set timer in seconds: "))
for i in range(seconds, 0, -1):
    print(f"Time remaining: {i}s", end="\r")
    time.sleep(1)

print("\nTime's up! Wake up!")