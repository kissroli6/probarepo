# Smartwatch Simulator

This project simulates a smartwatch with two sensors: a heart rate sensor and a blood oxygen level sensor. The smartwatch monitors the user's heart rate and blood oxygen levels, providing warnings when values are outside of normal ranges.

## Features

- Simulates heart rate readings and checks for high or low values.
- Simulates blood oxygen level readings and checks for high or low values.
- Provides user-friendly warnings for abnormal readings.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/smartwatch-simulator.git
   ```
2. Navigate to the project directory:
   ```
   cd smartwatch-simulator
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the smartwatch simulation, execute the following command:
```
python src/main.py
```

The simulation will continuously check the sensor values and print warnings if any readings are outside the normal thresholds.

## Sensors

### Heart Rate Sensor

- **Normal Range**: 60 - 100 beats per minute
- Warnings:
  - Low Heart Rate: Below 60 bpm
  - High Heart Rate: Above 100 bpm

### Blood Oxygen Sensor

- **Normal Range**: 95% - 100%
- Warnings:
  - Low Blood Oxygen: Below 95%
  - High Blood Oxygen: Above 100% (not typical, but included for completeness)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.