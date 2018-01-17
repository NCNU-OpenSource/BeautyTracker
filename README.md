# BeautyTracker
正妹追蹤器

## 緣起
當你在路上看到一位正妹，卻不知道他的系級學號出沒地點。
這時候我們可以使用部署在學校各個停車場的攝影裝置，進而知道正妹都在哪邊出沒，
這時候就可以說，「欸，好巧喔，又見面了，我們真有緣份呢」"

## 成員
- [IishaWu <3](https://github.com/IishaWu)
- [s104321072](https://github.com/s104321072)
- [qianchuen](https://github.com/qianchuen)
- [SihYingChen](https://github.com/SihYingChen)
- [JackKuo-tw](https://github.com/JackKuo-tw)
- [Dorothy0405](https://github.com/Dorothy0405)

## 使用裝置
- Raspberry Pi 3
- Pi Camera Module v2

## 實作所需材料
<table>
  <thead>
      <tr>
        <td>材料名稱</td>
        <td>數量</td>
        <td>來源</td>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>樹莓派</td>
        <td>兩個</td>
        <td>Moli</td>
      </tr>
      <tr>
        <td>pi camera</td>
        <td>一個</td>
        <td>Nicole</td>
      </tr>
    </tbody>
</table>

## 程式流程
- 利用camera 進行即時的車牌辨識，有辨識到車牌之後會拍照並儲存照片。
- 再進入臉部辨識的部分，偵測到人臉與資料庫進行比對，如果比對成功再拍一張照片，
- 把對應的資料存到資料庫，最後再回到車牌辨識的部分。
