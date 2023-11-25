from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QStatusBar
from PyQt5.QtGui import QImage, QPixmap
from Controller import Controller


class ImageViewer(QMainWindow):
    def __init__(self):
        super(ImageViewer, self).__init__()
        uic.loadUi('interfaz_imagenes/img_interfaz.ui', self)
        self.controller = Controller()
        self.setup()

    def setup(self):
        self.abrir.clicked.connect(self.open_image)
        self.guardar.clicked.connect(self.save_image)
        self.cerrar.clicked.connect(self.close)
        self.apertura.clicked.connect(self.controller.open)
        self.cierre.clicked.connect(self.controller.close)
        self.dilatar.clicked.connect(self.controller.dilate)
        self.erosionar.clicked.connect(self.controller.erode)
        self.horizontalSlider.valueChanged.connect(self.controller.set_kernel_size)

        self.apertura.clicked.connect(self.apply_operation_and_update_image(self.controller.open, 'Apertura'))
        self.cierre.clicked.connect(self.apply_operation_and_update_image(self.controller.close, 'Cierre'))
        self.dilatar.clicked.connect(self.apply_operation_and_update_image(self.controller.dilate, 'Dilatación'))
        self.erosionar.clicked.connect(self.apply_operation_and_update_image(self.controller.erode, 'Erosión'))
        self.statusbar = self.statusBar

    def open_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()",
                                                   "", "All Files (*);;JPEG (*.jpg *.jpeg);;PNG (*.png)",
                                                   options=options)
        if file_name:
            self.controller.load_image(file_name)
            self.update_image()
            self.statusbar.showMessage('Imagen cargada correctamente')

    def save_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()",
                                                   "", "JPEG (*.jpg *.jpeg);;PNG (*.png)",
                                                   options=options)
        if file_name:
            self.controller.save_image(file_name)
            self.statusbar.showMessage('Imagen guardada correctamente')

    def update_image(self):
        # Convertir la imagen de OpenCV a QPixmap
        height, width = self.controller.image_processor.image.shape
        bytes_per_line = width
        qt_image = QImage(self.controller.image_processor.image.data,
                          width, height, bytes_per_line, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qt_image)

        # Actualizar el QLabel
        self.imagen.setPixmap(pixmap)

    def apply_operation_and_update_image(self, operation, operation_name):
        def wrapper():
            operation()
            self.update_image()
            self.statusbar.showMessage(f'{operation_name} realizada con éxito')
        return wrapper
