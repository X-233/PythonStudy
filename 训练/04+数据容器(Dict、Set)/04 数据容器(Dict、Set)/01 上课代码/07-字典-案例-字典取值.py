import pprint

data = {
    "songinfo": {
        "collect_num": 144123,
        "hot": "100627",
        "title": "你还要我怎样",
        "language": "国语",
        "country": "内地",
        "si_proxycompany": "华宇世博音乐文化（北京）有限公司-普通代理",
        "compose": "薛之谦",
        "song_id": "100575177",
        "high_rate": "320",
        "artist": "薛之谦",
        "artist_list": [
            {
                "ting_uid": "2517",
                "del_status": "0",
                "artist_name": "薛之谦",
                "artist_id": "88"
            }
        ],
        "songwriting": "薛之谦",
        "album_id": "93104033",
        "share_num": 4266,
        "author": "薛之谦",
        "publishtime": "2013-11-11",
        "album_title": "意外"
    },
    "error_code": 22000
}

# 获取歌名与作者名(artist_name)
# 复杂字典取值就像剥洋葱一样
print('歌名:\t', data["songinfo"]['title'])
print('作者名:\t', data["songinfo"]['artist_list'][0]['artist_name'])

# print(data)
# pprint.pprint(data)