import requests
import json
url1 = 'http://nba.nowscore.com/jsData/rank/19-20/s1.js?version=2019092616'
head = {
'Referer': 'http://nba.nowscore.com/cn/LeagueRank.aspx?SclassID=1&matchSeason=2019-2020',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
r = requests.get(url=url1,headers=head)

if(r.status_code==200):
    print(r.text)