import requests
total_list=[]
index=0
while True:
    print('@Nick_Ye超级会员版VIP音乐')
    song=input('输入歌曲名：')
    wz={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a1b) XWEB/9129',
        'referer':'https://servicewechat.com/wxe9188e46b544384b/62/page-frame.html',
        'channel':'0140210'
        }
    search_url=f'http://c.musicapp.migu.cn/v1.0/content/search_all.do?text={song}&pageNo=1&pageSize=20&isCopyright=1&sort=1&searchSwitch=%7B%22song%22%3A1%2C%22album%22%3A0%2C%22singer%22%3A0%2C%22tagSong%22%3A1%2C%22mvSong%22%3A0%2C%22bestShow%22%3A1%7D'
    search_res = requests.get(search_url,headers=wz)
    JSON=search_res.json()
    song_list=JSON['songResultData']['result'] #第一页所有歌曲结果
    for song_data in song_list:
        # print(song_data)
        song_name=song_data['name']
        singer=song_data['singers'][0]['name']
        contentId=song_data['contentId']
        copyrightId=song_data['copyrightId']
        try:
            albumsId=song_data['albums'][0]['id']
            albums_name=song_data['albums'][0]['name']
            list=[index,song_name,singer,albums_name,albumsId,contentId,copyrightId]
        except:
            list=[index,song_name,singer,'0','0',contentId,copyrightId]
        total_list.append(list)
        index+=1
    for li in total_list:
         print(li)

    choice=int(input('请选择你要下载的歌曲编号！'))
    url=f'http://c.musicapp.migu.cn/MIGUM3.0/strategy/listen-url/v2.3?copyrightId={total_list[choice][-1]}&contentId={total_list[choice][5]}&resourceType=2&albumId={total_list[choice][4]}&netType=01&toneFlag=PQ'
    res=requests.get(url,headers=wz)
    JSON1=res.json()
    download_url=JSON1['data']['url']

    res1=requests.get(download_url)
    open(f'{total_list[choice][1]}-{total_list[choice][2]}-{total_list[choice][3]}.mp3','wb').write(res1.content)
    print('下载成功，请享用~')