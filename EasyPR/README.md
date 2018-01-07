# EasyPR 教學

[EasyPR](https://github.com/liuruoze/EasyPR) 是一個開源的中文車牌識別系統，其目標是成為一個簡單、高效、準確的非限制場景(unconstrained situation)下的車牌識別庫。 **目前仍不能辨識台灣車牌**

## 安裝

官方有提供[安裝教學](https://github.com/liuruoze/EasyPR/blob/master/Usage.md)，在此還是整理一下在 Ubuntu16.04 上面安裝遇到的問題

- 注意，此套件需要桌面版環境，筆者全套裝完才發現這件事... 還好用 apt 裝了 ubuntu-desktop 挽回
- Ubuntu 16.04 LTS 實測可用

### OpnnCV安裝

- 目前 EasyPR 要求 3.2 版本以上的 OpenCV

這個[安裝教學](https://www.learnopencv.com/install-opencv3-on-ubuntu/)照做基本上就沒問題了

- 小訣竅，可以把上面每個區塊指令貼到文字檔，用 sudo sh file.sh，去執行安裝，可以將 apt-get install 替換成 apt-get install -y 免去按 y 的麻煩
- 在 **Install OS libraries** 時請注意自己的版本，別無腦複製貼上
- 在 **Install Python libraries** 時第一部份可能會遇到 locales 問題而報錯，以下新增了三行可以比對看看


```
sudo apt-get install -y python-dev python-pip python3-dev python3-pip
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales
sudo -H pip2 install -U pip numpy
sudo -H pip3 install -U pip numpy
```

- 在 Make 過程中，先下載 OpenCV, OpenCV_contrib 以節省時間
- **Step 5.3** 記得替換成正確的 CPU 核心數，後面在 ln 路徑請用自己的路徑！

### EasyPR 安裝

`$ git clone https://github.com/liuruoze/EasyPR`

進去資料夾後設定 CMakeLists.txt，若是照上面的裝法路徑會在 /usr/local/share/OpenCV/，所以該行要改成
`set(CMAKE_PREFIX_PATH ${CMAKE_PREFIX_PATH} "/usr/local/share/OpenCV/")`

OpenCV 3.2 以上版本會 build 報錯，請編輯 ./include/easypr/config.h，將 `#define CV_VERSION_THREE_ZERO` ，改成 `#define CV_VERSION_THREE_TWO`

就可以開心的 `./build.sh` 啦～

完成後你可以：

```
$ ./demo // 進入選單界面
$ ./demo ? // 查看 CLI 幫助
```

若你在遠端執行，請嘗試使用
`$ ssh -X your_machine`，可以將畫面回傳

