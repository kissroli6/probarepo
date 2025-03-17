class BloodOxygenSensor:
    def __init__(self):
        self.blood_oxygen_level = 95  # Default value

    def get_blood_oxygen_level(self):
        # Simulate reading blood oxygen level (in percentage)
        import random
        self.blood_oxygen_level = random.randint(85, 100)
        return self.blood_oxygen_level

    def check_blood_oxygen_level(self):
        if self.blood_oxygen_level < 90:
            return "Warning: Low blood oxygen level!"
        elif self.blood_oxygen_level > 100:
            return "Warning: High blood oxygen level!"
        else:
            return "Blood oxygen level is normal."