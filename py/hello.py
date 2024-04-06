import time

for i in range(100):
    csi = "\033["  # ANSI escape code start
    color = str(i % 3)  # Cycling through colors (0, 1, 2)
    print(csi + color + "moeasy")
    time.sleep(0.2)  # Pause for 0.2 seconds
