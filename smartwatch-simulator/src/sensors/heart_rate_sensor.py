class HeartRateSensor:
    def __init__(self):
        self.heart_rate = 70  # Default heart rate

    def get_heart_rate(self):
        # Simulate reading heart rate values (for simplicity, we return a static value)
        return self.heart_rate

    def check_heart_rate(self):
        if self.heart_rate < 60:
            return "Warning: Low heart rate detected!"
        elif self.heart_rate > 100:
            return "Warning: High heart rate detected!"
        else:
            return "Heart rate is normal."