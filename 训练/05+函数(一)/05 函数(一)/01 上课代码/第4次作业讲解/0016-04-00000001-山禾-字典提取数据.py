"""
作业3
要求：从字典中提取歌手、歌名、音乐地址
"""
data = {
    'state': True,
    'errno': 22000,
    'errmsg': '',
    'elapsed_time': '0.0122',
    'data': {
        'artist': [
            {'artistCode': 'A10047720', 'birthday': '1983-07-17', 'gender': '男', 'name': '薛之谦', 'artistType': 38,
             'artistTypeName': '歌手',
             'pic': 'https://img01.dmhmusic.com/0101/M00/F8/AE/ChR45V7XEJWAZJ8KAAL8wj6aS4w115.jpg',
             'region': ''}],
        'cpId': 23,
        'pic': 'https://img01.dmhmusic.com/0412/M00/FE/96/ChAKEl_IzFiAUZyEAA-Q7DRXeIo850.jpg',
        'title': '你还要我怎样',
        'duration': 310,
        'assetId': 'T10038986648',
        'genre': '流行',
        'albumTitle': '意外',
        'id': 'T10038986648',
        'lang': '中文',
        'afReplayGain': -0.370003,
        'albumAssetCode': 'P10001640807',
        'releaseDate': '2013-11-11T00:00:00.000Z',
        'isrc': 'CNA651302299',
        'sort': 3, 'meanVolume': -17.1,
        'maxVolume': 0,
        'lyric': 'https://static-qianqian.taihe.com/0412/M00/FE/96/ChAKEl_IzFiAA1agAAAG_sbemkw066.lrc',
        'pay_model': 2,
        'TSID': 'T10038986648',
        'allRate': ['320', '128',
                    '3000', '64'],
        'pushTime': '2019-03-05T16:42:51+08:00',
        'downTime': '2037-01-01T00:00:00+08:00',
        'bizList': ['sdk_cpm'],
        'bits': 16,
        'path': 'https://audio04.dmhmusic.com/71_53_T10038986648_128_4_1_0_sdk-cpm/cn/0208/M00/E5/61/ChR46119DrGAW4d4AEvErRDwLyg867.mp3?xcode=c1a597cce27ff185785e95c6cf346f934713ee4',
        'size': 4965549, 'rate': 128,
        'hashcode': 'cee20c55e4518f0511c101f76c2914c0ba9895b9',
        'format': 'mp3',
        'filemd5': 'feacadc129c14b6418d7bd12864b1757',
        'expireTime': 1609416230,
        'isFavorite': 0, 'isVip': 0}}

print(data)
"""

要求以以下格式输出：
```
歌手： 薛之谦
歌名： 你还要我怎样
音乐地址： https://audio04.dmhmusic.com/71_53_T10038986648_128_4_1_0_sdk-cpm/cn/0208/M00/E5/61/ChR46119DrGAW4d4AEvErRDwLyg867.mp3?xcode=c1a597cce27ff185785e95c6cf346f934713ee4
```
最后点击一下音乐地址，你会发现一件神奇的事情 `φ(>ω<*)` 
"""
"""自己在下方编写代码实现功能"""
print(data['data']['artist'][0]['name'])
print(data.get('data').get('artist')[0].get('name'))


print(data['data']['title'])
print(data['data']['path'])
print(data.get('data').get('title'))
print(type(data.get('data').get('title')))

# 对象有对象的方法及属性
