from data import cat_detected


class Camera:

    def detect_cat(self):

        if cat_detected:
            print("Camera: Cat detected")
            return True

        print("Camera: No cat detected")
        return False
