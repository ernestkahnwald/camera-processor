import cv2
import numpy as np


FONT_SCALE = 1
COORDS = (10, 50)


def process_image(image):
    return _convert_array_to_image(
        _magical_processing(
            _convert_image_to_array(image)
        )
    )


def _convert_image_to_array(image):
    array = np.frombuffer(image.file.read(), np.int8)
    return cv2.imdecode(array, 1)


def _magical_processing(array):
    import time

    return cv2.putText(
        array,
        str(time.time()),
        COORDS,
        cv2.FONT_HERSHEY_PLAIN,
        FONT_SCALE,
        (0, 0, 255),
        1,
        cv2.LINE_AA,
    )


def _convert_array_to_image(array):
    return cv2.imencode('.png', array)[1].tobytes()
