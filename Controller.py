from Model import ImageProcessor


class Controller:
    def __init__(self):
        self.image_processor = ImageProcessor()

    def set_kernel_size(self, size):
        self.image_processor.set_kernel_size(size)

    def load_image(self, path):
        self.image_processor.load_image(path)

    def save_image(self, path):
        self.image_processor.save_image(path)

    def erode(self):
        self.image_processor.erode()

    def dilate(self):
        self.image_processor.dilate()

    def open(self):
        self.image_processor.open()

    def close(self):
        self.image_processor.close()
