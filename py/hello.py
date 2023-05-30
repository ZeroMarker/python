import time
for i in range(100):
    csi = "\033["
    color = str(i % 3)
    print(csi + color + "moeasy")
    time.sleep(0.2)

