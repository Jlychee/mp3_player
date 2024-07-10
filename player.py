import os

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

import style
from style import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(700, 500)
        MainWindow.setStyleSheet(style.style_main)



        self.file_path = ''

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.choose_folder_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.choose_folder_btn.setGeometry(QtCore.QRect(10, 450, 256, 41))
        font = QtGui.QFont()
        font.setFamily("inglobal")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.choose_folder_btn.setFont(font)
        self.choose_folder_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.choose_folder_btn.setStyleSheet(style.style_choose_btn)
        self.choose_folder_btn.setObjectName("choose_folder_btn")
        self.choose_folder_btn.clicked.connect(self.browse_folder)
        self.volume_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.volume_slider.setGeometry(QtCore.QRect(290, 340, 391, 41))
        self.volume_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.volume_slider.setValue(50)
        self.volume_slider.setMaximum(100)
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.music_title = QtWidgets.QLabel(parent=self.centralwidget)
        self.music_title.setGeometry(QtCore.QRect(270, 10, 420, 50))
        self.music_title.setMaximumSize(QtCore.QSize(420, 50))
        font = QtGui.QFont()
        font.setFamily("inglobal")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.music_title.setFont(font)
        self.music_title.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.music_title.setScaledContents(False)
        self.music_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.music_title.setWordWrap(False)
        self.music_title.setObjectName("music_title")
        self.play_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.play_btn.setGeometry(QtCore.QRect(430, 390, 130, 80))
        self.play_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.play_btn.setStyleSheet(style.style_play_btn)
        self.play_btn.setText("")
        self.play_btn.setIconSize(QtCore.QSize(40, 40))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/play.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.play_btn.setIcon(icon2)
        self.play_btn.setCheckable(True)
        self.play_btn.setChecked(False)
        self.play_btn.setObjectName("play_btn")
        self.play_btn.clicked.connect(self.play)
        self.previous_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.previous_btn.setGeometry(QtCore.QRect(330, 410, 60, 40))
        self.previous_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.previous_btn.setStyleSheet(style.style_prev_next_btn)
        self.previous_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/previous.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        self.previous_btn.setIcon(icon)
        self.previous_btn.setIconSize(QtCore.QSize(32, 32))
        self.previous_btn.setObjectName("previous_btn")
        self.previous_btn.clicked.connect(self.previous)
        self.next_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(600, 410, 60, 40))
        self.next_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.next_btn.setStyleSheet(style.style_prev_next_btn)
        self.next_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/next.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.next_btn.setIcon(icon1)
        self.next_btn.setIconSize(QtCore.QSize(32, 32))
        self.next_btn.setObjectName("next_btn")
        self.next_btn.clicked.connect(self.next)
        self.gif = QtGui.QMovie("./gif/gif2.gif")
        self.gif_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.gif_label.setGeometry(QtCore.QRect(330, 80, 380, 241))
        self.gif_label.setMovie(self.gif)
        self.gif_label.setObjectName("gif_label")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 256, 421))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.on_clicked)
        self.init_player()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MP3Player", "MP3Player"))
        self.choose_folder_btn.setText(_translate("MainWindow", "Выбрать папку с музыкой"))
        self.music_title.setText(_translate("MainWindow", ""))

    def init_player(self):
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(.05)

    def set_volume(self, volume):
        self.volume = self.volume_slider.value()
        self.audio_output.setVolume(self.volume * .001)

    def browse_folder(self):
        self.listWidget.clear()
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(parent=self.centralwidget,
                                                                    caption="Выберите папку с музыкой")

        self.dir_data = []
        if self.directory:
            for file in os.listdir(self.directory):
                self.dir_data.append(file)
                self.listWidget.addItem(file)

    def on_clicked(self, item):
        if self.media_player.playbackState() in [QMediaPlayer.PlaybackState.PlayingState,
                                                 QMediaPlayer.PlaybackState.PausedState]:
            self.play_btn.setChecked(False)
            self.media_player.stop()
            self.play_icon()

        self.tilte = item.data(QtCore.Qt.ItemDataRole.DisplayRole)

        if self.dir_data[-1] == self.tilte:
            self.next_btn.hide()
        else:
            self.next_btn.show()
        if self.dir_data[0] == self.tilte:
            self.previous_btn.hide()
        else:
            self.previous_btn.show()

        self.music_title.setText(self.tilte[:-4])
        if self.play_btn.isChecked():
            self.play_btn.setChecked(not self.play_btn.isChecked())
            self.play_icon()
            self.media_player.stop()

        self.file_path = f"{self.directory}/{self.tilte}"
        if self.media_player.playbackState() == QMediaPlayer.PlaybackState.StoppedState:
            QtCore.QTimer.singleShot(1, lambda: self.source_setter(self.file_path))

    def source_setter(self, url):
        self.media_player.setSource(QtCore.QUrl.fromLocalFile(url))

    def next(self):
        if self.dir_data[-1] != self.tilte:
            self.previous_btn.show()
            next_title = self.dir_data[self.dir_data.index(self.tilte) + 1]
            self.tilte = next_title
            if self.tilte == self.dir_data[-1]:
                self.next_btn.hide()
            self.media_player.stop()
            self.play_btn.setChecked(False)
            self.play()
            self.music_title.setText(self.tilte[:-4])
            QtCore.QTimer.singleShot(1, lambda: self.source_setter(f"{self.directory}/{next_title}"))
        else:
            self.next_btn.hide()

    def previous(self):
        if self.dir_data[0] != self.tilte:
            self.next_btn.show()
            next_title = self.dir_data[self.dir_data.index(self.tilte) - 1]
            self.tilte = next_title
            if self.tilte == self.dir_data[0]:
                self.previous_btn.hide()
            self.media_player.stop()
            self.play_btn.setChecked(False)
            self.play()
            self.music_title.setText(self.tilte[:-4])
            QtCore.QTimer.singleShot(1, lambda: self.source_setter(f"{self.directory}/{next_title}"))

    def play(self):
        if self.play_btn.isChecked():
            self.play_icon()
            self.media_player.play()
            try:
                if self.tilte != '': self.gif.start()
            except:
                pass
        else:
            self.play_icon()
            self.media_player.pause()
            self.gif.stop()

    def play_icon(self):
        if self.play_btn.isChecked():
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/pause.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            self.play_btn.setIcon(icon)
        else:
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("img/play.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            self.play_btn.setIcon(icon)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QtGui.QIcon("./img/ico.ico"))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
