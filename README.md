# Smart Cat Feeder

A simple Python simulation of an automatic cat water dispenser with webcam monitoring.

## Overview

Smart Cat Feeder simulates a pet water station equipped with a webcam. The application checks whether a cat is detected, dispenses water, and records all events in a log.

The project demonstrates modular Python development, object-oriented programming, and clean project organization.

## Features

- Webcam detection simulation
- Automatic water dispensing
- Water level monitoring
- Event logging
- Device status report

## Project Structure

```
.
├── main.py
├── camera.py
├── feeder.py
├── sensor.py
├── logger.py
├── data.py
├── config.py
└── README.md
```

## Example Output

```
===== SMART CAT FEEDER =====

Camera: Cat detected
Water level: 78%

Dispensing water...

Event Log
---------
Cat detected
Water dispensed
Water level updated

Status: READY
```

## Technologies

- Python 3
- Git
- GitHub

## Future Improvements

- OpenCV integration
- Motion detection
- MQTT support
- Raspberry Pi GPIO
- Mobile notifications

