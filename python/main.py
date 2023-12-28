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
from inputLabel import InputLabel
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from youtube_search import YoutubeSearch
import urllib.request
import threading as th

separator = "\\" if p.system() == "Windows" else "/"  #separator of file system
max_results = 10                                      #max result of video query
results = dict()

# Main Window Class
class MainWindow(QMainWindow):
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
    
    #Download Audio/Video Function [pytube API]
    def downloadVideo(self, index):
        global results
        url = "https://www.youtube.com/watch?v=" + results[index]["id"]
        output = ".{0}".format(separator) if self.outputFolderInputField.text() == "" else self.outputFolderInputField.text()
        self.msgLabel.setText(results[index]["title"] + "\n[⚠] in download...")

        try:
            if self.audioOnlyCheckbox.isChecked():
                audio = YouTube(url).streams.get_audio_only()
                audio.download(filename=results[index]["title"]+".mp3", output_path=output)
            else:
                video = YouTube(url)
                stream = video.streams.get_highest_resolution()
                stream.download(output_path=output)
            
            self.msgLabel.setText(results[index]["title"] + "\n[✔] Download complete!")
        except RegexMatchError:
            self.msgLabel.setText("[❌] Link entered invalid, please enter a valid YouTube link!")
    
    #Download video directly from YouTube link
    def downloadFromLink(self):
        link = self.YTLinkInputField.text()
        try:
            youtube_video = YouTube(link)
            titleOfVideo = youtube_video.title
            self.msgLabel.setText(titleOfVideo + "\n[⚠] in download...")        
            output = ".{0}".format(separator) if self.outputFolderInputField.text() == "" else self.outputFolderInputField.text()
                
            if self.audioOnlyCheckbox.isChecked():
                audio = youtube_video.streams.get_audio_only()
                audio.download(filename=titleOfVideo + ".mp3", output_path=output)
            else:
                stream = youtube_video.streams.get_highest_resolution()
                stream.download(output_path=output)
            
            self.msgLabel.setText(titleOfVideo + "\n[✔] Download complete!")
        except RegexMatchError:
            self.msgLabel.setText("[❌] Link entered invalid, please enter a valid YouTube link!")
        
    #Thread of download from link function
    def downloadFromLinkThread(self):
        thread = th.Thread(target=lambda: self.downloadFromLink())
        thread.start()
        

    #Search on youtube Function [youtube_search API]
    def loadResults(self):
        global results
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
    
    #Browse directory dialog function
    def outputFolderManager(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory", options=QFileDialog.ShowDirsOnly)
        self.outputFolderInputField.setText(directory)
    
    #init all widget relative to video info
    def initializeArrayWidget(self):
        self.miniatures = [self.miniature1, self.miniature2, self.miniature3, self.miniature4, self.miniature5, self.miniature6, self.miniature7, self.miniature8, self.miniature9, self.miniature10]
        self.titles = [self.title1, self.title2, self.title3, self.title4, self.title5, self.title6, self.title7, self.title8, self.title9, self.title10]  
        self.durations = [self.duration1, self.duration2, self.duration3, self.duration4, self.duration5, self.duration6, self.duration7, self.duration8, self.duration9, self.duration10]
        self.channels = [self.channel1, self.channel2, self.channel3, self.channel4, self.channel5, self.channel6, self.channel7, self.channel8, self.channel9, self.channel10]
    
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