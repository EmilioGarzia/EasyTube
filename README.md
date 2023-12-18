#### Summary
* [EasyTube: Introduction](#easytube)
    * [How to execute](#how-to-run)
    * [Used technologies](#used-technologies)
    * [Dependencies](#dependencies)
    * [Screenshot](#screenshot)
    * [MP3 Converter (Linux Users)](#mp3-converter-only-for-linux-users)
        * [How to execute "Converter"](#how-to-execute-convertersh)
    * [References](#references)
    * [Author](#author)

# EasyTube

**EasyTube** can download audio/video from youtube using YouTube API

## How to run

This software is written in **python**, to execute EasyTube with python interpreter you have to enter into the `python` directory and execute the command:

```bash
python main.py
```

## Used technologies

* *Python*
* *PyQt5 (User Interface)*
* *CSS (for GUI style)*

## Dependencies

* *pytube*
* *youtube_search*
* *PyQt5*

⚠️: Keep `pytube` and `youtube_search` APIs up to date

## Screenshot

![f](./EasyTube%20Screenshot.png)

## MP3 Converter *(Only for Linux Users)*

When you download an audio file from EasyTube the output type files are `MP4 ISO Media`, for this reason if you want to play that songs on an old `MP3 stereo` you must do the conversion of this file in an pure `MP3 file`.
In this project you can find a script written in `bash` named `Converter.sh`.

`Converter.sh` is an MP3 converter based on a `ffmpeg` package, if you don't have this package on your system, you have to install it with command:

```bash
# APT Ubuntu Package Manager
sudo apt install ffmpeg 
```

### How to execute `Converter.sh`

The *Converter* convert in MP3 all audio files into a specific directory, all output files are contained in a new directory named `Converted`.

To execute this converter open Linux terminal and insert the command:

```bash
./Converter <Directory that contains your songs>
```

⚠️: You can use the converter on *Windows* with the **WSL** *(Windows Subsystem Linux)*

## References

[Pytube](https://pytube.io/en/latest/)

[youtube_search](https://pypi.org/project/youtube-search-python/#description)

[ffmpeg](https://ffmpeg.org/)

## Author
Emilio Garzia, 2023
