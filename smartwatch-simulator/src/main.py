import random
import time

class HeartRateSensor:
    def get_heart_rate(self):
        # Simulate a human heart rate between 50 and 120 bpm
        return random.randint(50, 120)

    def check_heart_rate(self, heart_rate):
        if heart_rate < 60:
            print(f"Warning: Low heart rate detected - {heart_rate} bpm")
        elif heart_rate > 100:
            print(f"Warning: High heart rate detected - {heart_rate} bpm")
        else:
            print(f"Heart rate is normal - {heart_rate} bpm")

class BloodOxygenSensor:
    def get_blood_oxygen_level(self):
        # Simulate a human blood oxygen level between 90% and 100%
        return random.uniform(90, 100)

    def check_blood_oxygen_level(self, blood_oxygen_level):
        if blood_oxygen_level < 95:
            print(f"Warning: Low blood oxygen level detected - {blood_oxygen_level:.2f}%")
        elif blood_oxygen_level > 100:
            print(f"Warning: High blood oxygen level detected - {blood_oxygen_level:.2f}%")
        else:
            print(f"Blood oxygen level is normal - {blood_oxygen_level:.2f}%")

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