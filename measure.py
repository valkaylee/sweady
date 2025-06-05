# https://github.com/Seeed-Studio/wiki-documents/blob/docusaurus-version/docs/Sensor/Grove/Grove_Sensors/Biometric/Grove-GSR_Sensor.md


import sys
import time
import grovepi
import pandas as pd


class GroveGSRSensor:
    def __init__(self, port):
        self.port = port
        grovepi.pinMode(self.port, "INPUT")

    @property
    def GSR(self):
        try:
            return grovepi.analogRead(self.port)
        except IOError as e:
            print("I/O Error on grovepi bus:", e)
            return None


Grove = GroveGSRSensor


def measure(port=0):
    sensor = GroveGSRSensor(port)

    readings = []
    print("Detecting GSR on GrovePi+ port A%d… (Ctrl+C to stop)" % port)

    try:
        for i in range(100):
            val = sensor.GSR
            timestamp = time.time()
            if val is not None:
                print(f"GSR value: {val}")
                readings.append({"timestamp": timestamp, "GSR": val})
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nData collection stopped by user.")

    df = pd.DataFrame(readings)
    print("\nCollected GSR Data:")
    print(df)

    df.to_csv("gsr_data.csv", index=False)


if __name__ == "__main__":
    measure()
