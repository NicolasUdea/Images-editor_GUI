import cv2
import numpy as np


class ImageProcessor:
    def __init__(self):
        self.kernel_size = 1
        self.image = None

    def set_kernel_size(self, size):
        self.kernel_size = size

    def load_image(self, path):
        self.image = cv2.imread(path, 0)

    def save_image(self, path):
        cv2.imwrite(path, self.image)

    def erode(self):
        kernel = np.ones((self.kernel_size, self.kernel_size), np.uint8)
        self.image = cv2.erode(self.image, kernel, iterations=1)

    def dilate(self):
        kernel = np.ones((self.kernel_size, self.kernel_size), np.uint8)
        self.image = cv2.dilate(self.image, kernel, iterations=1)

    def open(self):
        kernel = np.ones((self.kernel_size, self.kernel_size), np.uint8)
        self.image = cv2.morphologyEx(self.image, cv2.MORPH_OPEN, kernel)

    def close(self):
        kernel = np.ones((self.kernel_size, self.kernel_size), np.uint8)
        self.image = cv2.morphologyEx(self.image, cv2.MORPH_CLOSE, kernel)
