from config import MIN_WATER_LEVEL


def check_water(level):

    print(f"Water level: {level}%")

    if level < MIN_WATER_LEVEL:
        print("Warning: Low water level")
