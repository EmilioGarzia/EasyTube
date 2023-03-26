# PROJECT: EasyTube
# DEVELOPER: Emilio Garzia
# YEAR: 2023
# DESCRIPTION: Download easy Audio/Video from YouTube

#Dependencies
import sys
import platform as p
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from pytube import YouTube
from youtube_search import YoutubeSearch
import urllib.request

separator = "\\" if p.system() == "Windows" else "/"  #separator of file system
max_results = 5                                       #max result of video query

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #load GUI
        loadUi("..{0}gui{0}gui.ui".format(separator), self)
        #set scroll invisible area at launch
        self.outputScrollArea.setVisible(False)
        #apply CSS style to main window
        self.applyDarkTheme()
        #array of details widget
        self.miniatures = []
        self.titles = []
        self.durations = []
        self.channels = []
        self.initializeArrayWidget()

    def loadResults(self):
        pixmap = QPixmap()
        keyword = self.searchInputField.text()
        results = YoutubeSearch(keyword, max_results=max_results).to_dict()
        if len(results) > 0:
            for i in range(max_results):
                url_miniature = results[i]["thumbnails"][0]             #url of video thumbnail
                data = urllib.request.urlopen(url_miniature).read()     #extract data image
                pixmap.loadFromData(data)                               #load image in pixmap
                self.titles[i].setText(results[i]["title"])             #set title of videos
                self.durations[i].setText(results[i]["duration"])       #set duration of videos
                self.channels[i].setText(results[i]["channel"])         #set channel of videos
                self.miniatures[i].setPixmap(pixmap)                    #set pixmap in QLabel
            self.msgLabel.setText("Click on thumbnail or title of your favourite video!")
            self.outputScrollArea.setVisible(True)
        else:
            self.msgLabel.setText("No videos found")
    
    def initializeArrayWidget(self):
        self.miniatures = [self.miniature1, self.miniature2, self.miniature3, self.miniature4, self.miniature5]
        self.titles = [self.title1, self.title2, self.title3, self.title4, self.title5 ]  
        self.durations = [self.duration1, self.duration2, self.duration3, self.duration4, self.duration5]
        self.channels = [self.channel1, self.channel2, self.channel3, self.channel4, self.channel5]

    #set dark suite of main window
    def applyDarkTheme(self):
        with open("..{0}css{0}style.css".format(separator)) as myCSSfile:
            myCSS = myCSSfile.read()
            self.setStyleSheet(myCSS)


#Main Code
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())