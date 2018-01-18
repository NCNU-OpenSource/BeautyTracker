# 使用 analysis.py 教學
- analysis.py 使用到以下兩個open source
- [openalpr](https://github.com/openalpr/openalpr) is an open source Automatic License Plate Recognition library written in C++ with bindings in C#, Java, Node.js, Go, and Python. The library analyzes images and video streams to identify license plates. The output is the text representation of any license plate characters.
Check out a live online demo here: http://www.openalpr.com/demo-image.html
- opencv 

## openalpr 安裝

官方有提供[安裝教學](https://github.com/openalpr/openalpr/wiki/Compilation-instructions-(Ubuntu-Linux))
- Ubuntu 16.04 LTS 實測可用
- Raspbarry Pi 實測可用

### OpenCV-3.1.0安裝

- 目前 本程式要求 3.1 版本以上的 OpenCV
- Ubuntu install opencv
這個[安裝教學](https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/)照做基本上就沒問題了
- Raspberry Pi install opencv
這個[安裝教學](https://paper.dropbox.com/doc/Raspi-install-opencv-IHaVgymS9tRgfhnCaCSGv)照做基本上就沒問題了

#### 執行
- $ python analysis.py
- 因為程式還不是很完整,結束請用crtl+c
