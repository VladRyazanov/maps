import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from data_getter import DataGetter

lon = float(input())
lat = float(input())
delta = float(input())
delta_step = 0.001


class Map(QWidget):
    def __init__(self):
        super().__init__()
        self.data_getter = DataGetter()
        self.current_lon = lon
        self.current_lat = lat
        self.current_delta = delta
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.map_widget = self.setup_map_widget(self.current_lon, self.current_lat, self.current_delta)
        self.layout.addWidget(self.map_widget)
        self.setLayout(self.layout)

    def setup_map_widget(self, lon, lat, delta):
        image = self.data_getter.get_map_image(str(lon), str(lat), str(delta))
        temporary_file_name = "temporary_image_file.jpg"
        with open(temporary_file_name, "wb") as image_file:
            image_file.write(image)
        pixmap = QPixmap(temporary_file_name)
        pixmap = pixmap.scaled(640, 360, aspectRatioMode=Qt.KeepAspectRatio)
        image_label = QLabel(alignment=Qt.AlignmentFlag.AlignHCenter)
        image_label.setPixmap(pixmap)
        return image_label

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_PageUp:
            self.current_delta += delta_step
            if self.current_delta > 1:
                self.current_delta = 1
        elif key == Qt.Key_PageDown:
            self.current_delta -= delta_step
            if self.current_delta < 0:
                self.current_delta = 0

        self.layout.removeWidget(self.map_widget)
        self.map_widget = self.setup_map_widget(lon, lat, self.current_delta)
        self.layout.addWidget(self.map_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Map()
    window.show()
    sys.exit(app.exec())



