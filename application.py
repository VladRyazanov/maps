import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from data_getter import DataGetter

lon = "37.530887"
lat = "55.703118"
delta = "0.002"


class Map(QWidget):
    def __init__(self, content):
        super().__init__()
        self.image = content
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        if self.image is not None:
            temporary_file_name = "temporary_image_file.jpg"
            with open(temporary_file_name, "wb") as image_file:
                image_file.write(self.image)
            pixmap = QPixmap(temporary_file_name)
            pixmap = pixmap.scaled(640, 360, aspectRatioMode=Qt.KeepAspectRatio)
            image_label = QLabel(alignment=Qt.AlignmentFlag.AlignHCenter)
            image_label.setPixmap(pixmap)
            self.layout.addWidget(image_label)
        self.setLayout(self.layout)


data_getter = DataGetter()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Map(data_getter.get_map_image(lon, lat, delta))
    window.show()
    sys.exit(app.exec())



