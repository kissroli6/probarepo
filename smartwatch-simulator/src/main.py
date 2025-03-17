import random
import time
from sensors.heart_rate_sensor import HeartRateSensor
from sensors.blood_oxygen_sensor import BloodOxygenSensor

def main():
    heart_rate_sensor = HeartRateSensor()
    blood_oxygen_sensor = BloodOxygenSensor()

    while True:
        heart_rate = heart_rate_sensor.get_heart_rate()
        blood_oxygen_level = blood_oxygen_sensor.get_blood_oxygen_level()

        heart_rate_sensor.check_heart_rate(heart_rate)
        blood_oxygen_sensor.check_blood_oxygen_level(blood_oxygen_level)

        time.sleep(5)  # Simulate a delay between readings

if __name__ == "__main__":
    main()