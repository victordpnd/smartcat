from camera import Camera
from feeder import Feeder
from logger import add, show
from sensor import check_water
from data import water_level

camera = Camera()
feeder = Feeder(water_level)

print("=" * 30)
print("SMART CAT FEEDER")
print("=" * 30)

if camera.detect_cat():
    add("Cat detected")

    check_water(feeder.water_level)

    feeder.dispense()

    add("Water dispensed")
    add("Water level updated")

else:
    add("No cat detected")

show()

print("\nStatus: READY")
