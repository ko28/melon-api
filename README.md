# melon-api
<img src="https://i.imgur.com/Igpf68Q.png" width="300">

![PyPI](https://img.shields.io/pypi/v/melonapi?color=success&label=pypi%20package)
[![Heroku App Status](http://heroku-shields.herokuapp.com/ko28melonapi)](https://ko28melonapi.herokuapp.com)
![GitHub last commit](https://img.shields.io/github/last-commit/ko28/melon-api)
[![Downloads](https://pepy.tech/badge/melonapi)](https://pepy.tech/project/melonapi)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A simple chart API written in Flask for Melon, a Korean music streaming service. 

# Endpoints (GET)
Replace https://ko28melonapi.herokuapp.com/ with localhost when running locally
## Chart
* https://ko28melonapi.herokuapp.com/chart/live
* https://ko28melonapi.herokuapp.com/chart/rise
* https://ko28melonapi.herokuapp.com/chart/day
* https://ko28melonapi.herokuapp.com/chart/week
* https://ko28melonapi.herokuapp.com/chart/month

Response contains 100 entries. Key is ranking of song; value is name, ranking, artists, songId, albumId (id's are Melon specific). 
Example response:
```
{{"1": {"name": "에잇(Prod.&Feat. SUGA of BTS)", "ranking": "1", "artists": "아이유", "songId": "32578498", "albumId": "10426648"}, "2": {"name": "나비와 고양이 (feat.백현 (BAEKHYUN))", "ranking": "2", "artists": "볼빨간사춘기", "songId": "32583036", "albumId": "10427559"}, "3": {"name": "ON", "ranking": "3", "artists": "방탄소년단", "songId": "32399830", "albumId": "10377346"}, "4": {"name": "아로하", "ranking": "4", "artists": "조정석", "songId": "32491274", "albumId": "10409054"}, "5": {"name": "살짝 설렜어 (Nonstop)", "ranking": "5", "artists": "오마이걸", "songId": "32559781", "albumId": "10423289"}, "6": {"name": "00:00 (Zero O’Clock)", "ranking": "6", "artists": "방탄소년단", "songId": "32399832", "albumId": "10377346"}, "7": {"name": "Black Swan", "ranking": "7", "artists": "방탄소년단", "songId": "32323969", "albumId": "10377346"}, "8": {"name": "작은 것들을 위한 시 (Boy With Luv) (Feat. Halsey)", "ranking": "8", "artists": "방탄소년단", "songId": "31737197", "albumId": "10273641"}, "9": {"name": "친구", "ranking": "9", "artists": "방탄소년단", "songId": "32399834", "albumId": "10377346"}, "10": {"name": "Filter", "ranking": "10", "artists": "방탄소년단", "songId": "32399827", "albumId": "10377346"}, "11": {"name": "시차", "ranking": "11", "artists": "방탄소년단", "songId": "32399828", "albumId": "10377346"}, "12": {"name": "Moon", "ranking": "12", "artists": "방탄소년단", "songId": "32399835", "albumId": "10377346"}, "13": {"name": "Inner Child", "ranking": "13", "artists": "방탄소년단", "songId": "32399833", "albumId": "10377346"}, "14": {"name": "We are Bulletproof : the Eternal", "ranking": "14", "artists": "방탄소년단", "songId": "32399837", "albumId": "10377346"}, "15": {"name": "Louder than bombs", "ranking": "15", "artists": "방탄소년단", "songId": "32399829", "albumId": "10377346"}, "16": {"name": "욱 (UGH!)", "ranking": "16", "artists": "방탄소년단", "songId": "32399831", "albumId": "10377346"}, "17": {"name": "Interlude : Shadow", "ranking": "17", "artists": "방탄소년단", "songId": "32399826", "albumId": "10377346"}, "18": {"name": "Respect", "ranking": "18", "artists": "방탄소년단", "songId": "32399836", "albumId": "10377346"}, "19": {"name": "Outro : Ego", "ranking": "19", "artists": "방탄소년단", "songId": "32399838", "albumId": "10377346"}, "20": {"name": "Ridin’", "ranking": "20", "artists": "NCT DREAM", "songId": "32550660", "albumId": "10421298"}, "21": {"name": "Yours (Feat. 이하이, 창모)", "ranking": "21", "artists": "Raiden, 찬열 (CHANYEOL)", "songId": "32590490", "albumId": "10429159"}, "22": {"name": "Zombie", "ranking": "22", "artists": "DAY6 (데이식스)", "songId": "32586848", "albumId": "10428497"}, "23": {"name": "너를 사랑하고 있어", "ranking": "23", "artists": "백현 (BAEKHYUN)", "songId": "32298623", "albumId": "10372655"}, "24": {"name": "처음처럼", "ranking": "24", "artists": "엠씨더맥스 (M.C the MAX)", "songId": "32486613", "albumId": "10408131"}, "25": {"name": "내게 말해줘 (7 Days)", "ranking": "25", "artists": "NCT DREAM", "songId": "32550662", "albumId": "10421298"}, "26": {"name": "시작", "ranking": "26", "artists": "가호 (Gaho)", "songId": "32345931", "albumId": "10381712"}, "27": {"name": "너의 자리 (Puzzle Piece)", "ranking": "27", "artists": "NCT DREAM", "songId": "32550664", "albumId": "10421298"}, "28": {"name": "사랑, 하자", "ranking": "28", "artists": "수호 (SUHO)", "songId": "32495729", "albumId": "10409970"}, "29": {"name": "사랑은 또다시 (Love Again)", "ranking": "29", "artists": "NCT DREAM", "songId": "32550663", "albumId": "10421298"}, "30": {"name": "덤더럼(Dumhdurum)", "ranking": "30", "artists": "Apink (에이핑크)", "songId": "32528369", "albumId": "10416723"}, "31": {"name": "Quiet Down", "ranking": "31", "artists": "NCT DREAM", "songId": "32550661", "albumId": "10421298"}, "32": {"name": "Happy", "ranking": "32", "artists": "태연 (TAEYEON)", "songId": "32572926", "albumId": "10425647"}, "33": {"name": "Dolphin", "ranking": "33", "artists": "오마이걸", "songId": "32559782", "albumId": "10423289"}, "34": {"name": "좋은 사람 있으면 소개시켜줘", "ranking": "34", "artists": "조이 (JOY)", "songId": "32473998", "albumId": "10405712"}, "35": {"name": "이제 나만 믿어요", "ranking": "35", "artists": "임영웅", "songId": "32508053", "albumId": "10412319"}, "36": {"name": "너에게 가는 이 길 위에서 (너.이.길)", "ranking": "36", "artists": "백현 (BAEKHYUN)", "songId": "32421335", "albumId": "10396078"}, "37": {"name": "Obsession", "ranking": "37", "artists": "EXO", "songId": "32217921", "albumId": "10357878"}, "38": {"name": "Blueming", "ranking": "38", "artists": "아이유", "songId": "32183386", "albumId": "10346650"}, "39": {"name": "METEOR", "ranking": "39", "artists": "창모 (CHANGMO)", "songId": "32224272", "albumId": "10359162"}, "40": {"name": "흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야", "ranking": "40", "artists": "장범준", "songId": "32003395", "albumId": "10320500"}, "41": {"name": "Love me or Leave me", "ranking": "41", "artists": "DAY6 (데이식스)", "songId": "32586850", "albumId": "10428497"}, "42": {"name": "영웅 (英雄; Kick It)", "ranking": "42", "artists": "NCT 127", "songId": "32393669", "albumId": "10391380"}, "43": {"name": "Go away go away", "ranking": "43", "artists": "찬열 (CHANYEOL), 펀치 (Punch)", "songId": "32325829", "albumId": "10377809"}, "44": {"name": "아무노래", "ranking": "44", "artists": "지코 (ZICO)", "songId": "32313543", "albumId": "10375118"}, "45": {"name": "Dance Monkey", "ranking": "45", "artists": "Tones And I", "songId": "31979846", "albumId": "10316394"}, "46": {"name": "마음을 드려요", "ranking": "46", "artists": "아이유", "songId": "32378104", "albumId": "10388744"}, "47": {"name": "그때 그 아인", "ranking": "47", "artists": "김필", "songId": "32377231", "albumId": "10388581"}, "48": {"name": "Made In You", "ranking": "48", "artists": "수호 (SUHO)", "songId": "32495730", "albumId": "10409970"}, "49": {"name": "어느 60대 노부부이야기", "ranking": "49", "artists": "임영웅", "songId": "32397381", "albumId": "10391899"}, "50": {"name": "우리 만남이", "ranking": "50", "artists": "폴킴", "songId": "32550314", "albumId": "10421264"}, "51": {"name": "해와 달처럼", "ranking": "51", "artists": "DAY6 (데이식스)", "songId": "32586847", "albumId": "10428497"}, "52": {"name": "돌덩이", "ranking": "52", "artists": "하현우 (국카스텐)", "songId": "32361098", "albumId": "10385262"}, "53": {"name": "자화상", "ranking": "53", "artists": "수호 (SUHO)", "songId": "32495732", "albumId": "10409970"}, "54": {"name": "I’m in Trouble", "ranking": "54", "artists": "뉴이스트", "songId": "32588064", "albumId": "10428727"}, "55": {"name": "O₂", "ranking": "55", "artists": "수호 (SUHO)", "songId": "32495728", "albumId": "10409970"}, "56": {"name": "너의 차례 (Feat. 윤하)", "ranking": "56", "artists": "수호 (SUHO)", "songId": "32495733", "albumId": "10409970"}, "57": {"name": "화려하지 않은 고백", "ranking": "57", "artists": "규현 (KYUHYUN)", "songId": "32508146", "albumId": "10412335"}, "58": {"name": "암막 커튼", "ranking": "58", "artists": "수호 (SUHO)", "songId": "32495731", "albumId": "10409970"}, "59": {"name": "바램", "ranking": "59", "artists": "임영웅", "songId": "32323330", "albumId": "10377157"}, "60": {"name": "어떻게 지내 (Prod. By VAN.C)", "ranking": "60", "artists": "오반", "songId": "32438894", "albumId": "10399190"}, "61": {"name": "WANNABE", "ranking": "61", "artists": "ITZY (있지)", "songId": "32445339", "albumId": "10400522"}, "62": {"name": "Tick Tock", "ranking": "62", "artists": "DAY6 (데이식스)", "songId": "32586849", "albumId": "10428497"}, "63": {"name": "반만", "ranking": "63", "artists": "진민호", "songId": "32224409", "albumId": "10359204"}, "64": {"name": "Memories", "ranking": "64", "artists": "Maroon 5", "songId": "32055419", "albumId": "10330593"}, "65": {"name": "Psycho", "ranking": "65", "artists": "Red Velvet (레드벨벳)", "songId": "32273582", "albumId": "10368053"}, "66": {"name": "품", "ranking": "66", "artists": "볼빨간사춘기", "songId": "32594046", "albumId": "10427559"}, "67": {"name": "늦은 밤 너의 집 앞 골목길에서", "ranking": "67", "artists": "노을", "songId": "32156286", "albumId": "10348811"}, "68": {"name": "Afraid", "ranking": "68", "artists": "DAY6 (데이식스)", "songId": "32586853", "albumId": "10428497"}, "69": {"name": "나의 하루는 다 너로 가득해", "ranking": "69", "artists": "지코 (ZICO), 웬디 (WENDY)", "songId": "32600237", "albumId": "10431009"}, "70": {"name": "보라빛 엽서", "ranking": "70", "artists": "임영웅", "songId": "32441451", "albumId": "10399605"}, "71": {"name": "Don't Start Now", "ranking": "71", "artists": "Dua Lipa", "songId": "32137576", "albumId": "10345880"}, "72": {"name": "FIESTA", "ranking": "72", "artists": "IZ*ONE (아이즈원)", "songId": "32381408", "albumId": "10389281"}, "73": {"name": "1 to 10", "ranking": "73", "artists": "DAY6 (데이식스)", "songId": "32586852", "albumId": "10428497"}, "74": {"name": "내 눈물 모아", "ranking": "74", "artists": "휘인 (Whee In)", "songId": "32561690", "albumId": "10423707"}, "75": {"name": "봄날", "ranking": "75", "artists": "방탄소년단", "songId": "30244931", "albumId": "10037969"}, "76": {"name": "그대 고운 내사랑", "ranking": "76", "artists": "어반자카파", "songId": "32521396", "albumId": "10415229"}, "77": {"name": "오늘도 빛나는 너에게 (To You My Light) (Feat.이라온)", "ranking": "77", "artists": "마크툽 (MAKTUB)", "songId": "31853557", "albumId": "10294603"}, "78": {"name": "2002", "ranking": "78", "artists": "Anne-Marie", "songId": "31029291", "albumId": "10137250"}, "79": {"name": "때려쳐", "ranking": "79", "artists": "DAY6 (데이식스)", "songId": "32586851", "albumId": "10428497"}, "80": {"name": "나보다 더 사랑해요", "ranking": "80", "artists": "김호중", "songId": "32560653", "albumId": "10423519"}, "81": {"name": "우리 왜 헤어져야 해", "ranking": "81", "artists": "신예영", "songId": "32187544", "albumId": "10353881"}, "82": {"name": "Love poem", "ranking": "82", "artists": "아이유", "songId": "32143487", "albumId": "10346650"}, "83": {"name": "Stay Tonight", "ranking": "83", "artists": "청하", "songId": "32559498", "albumId": "10423202"}, "84": {"name": "너를 그린 우주 (Insomnia2020) (Feat. 이라온)", "ranking": "84", "artists": "마크툽 (MAKTUB)", "songId": "32556676", "albumId": "10422586"}, "85": {"name": "Moon Dance", "ranking": "85", "artists": "뉴이스트", "songId": "32588063", "albumId": "10428727"}, "86": {"name": "Stuck with U", "ranking": "86", "artists": "Ariana Grande, Justin Bieber", "songId": "32584913", "albumId": "10428037"}, "87": {"name": "넌 내가 보고 싶지 않나 봐", "ranking": "87", "artists": "신예영", "songId": "32559566", "albumId": "10423244"}, "88": {"name": "Back To Me (평행우주)", "ranking": "88", "artists": "뉴이스트", "songId": "32588066", "albumId": "10428727"}, "89": {"name": "모든 날, 모든 순간 (Every day, Every Moment)", "ranking": "89", "artists": "폴킴", "songId": "30962526", "albumId": "10149492"}, "90": {"name": "꼭", "ranking": "90", "artists": "뉴이스트", "songId": "32588067", "albumId": "10428727"}, "91": {"name": "일편단심 민들레야", "ranking": "91", "artists": "임영웅", "songId": "32362652", "albumId": "10385603"}, "92": {"name": "Firework", "ranking": "92", "artists": "뉴이스트", "songId": "32588065", "albumId": "10428727"}, "93": {"name": "어떻게 이별까지 사랑하겠어, 널 사랑하는 거지", "ranking": "93", "artists": "AKMU (악동뮤지션)", "songId": "32061975", "albumId": "10331947"}, "94": {"name": "Maniac", "ranking": "94", "artists": "Conan Gray", "songId": "32122539", "albumId": "10343276"}, "95": {"name": "반딧별", "ranking": "95", "artists": "뉴이스트", "songId": "32588068", "albumId": "10428727"}, "96": {"name": "상사화", "ranking": "96", "artists": "임영웅", "songId": "32555799", "albumId": "10422374"}, "97": {"name": "배신자", "ranking": "97", "artists": "임영웅", "songId": "32457760", "albumId": "10402513"}, "98": {"name": "Zombie (English Ver.)", "ranking": "98", "artists": "DAY6 (데이식스)", "songId": "32586854", "albumId": "10428497"}, "99": {"name": "LALALILALA", "ranking": "99", "artists": "에이프릴 (APRIL)", "songId": "32550258", "albumId": "10421256"}, "100": {"name": "두 주먹", "ranking": "100", "artists": "임영웅", "songId": "32457753", "albumId": "10402513"}}
```
## Lyric 
* https://ko28melonapi.herokuapp.com/lyric/[songId]

Example response:
```
이 밤 그날의 반딧불을
당신의 창 가까이 보낼게요
음 사랑한다는 말이에요
나 우리의 첫 입맞춤을 떠올려
그럼 언제든 눈을 감고
음 가장 먼 곳으로 가요
난 파도가 머물던
모래 위에 적힌 글씨처럼
그대가 멀리 사라져 버릴 것 같아
늘 그리워 그리워
여기 내 마음속에
모든 말을 다 꺼내어 줄 순 없지만
사랑한다는 말이에요
어떻게 나에게
그대란 행운이 온 걸까
지금 우리 함께 있다면 아
얼마나 좋을까요
난 파도가 머물던
모래 위에 적힌 글씨처럼
그대가 멀리 사라져 버릴 것 같아
또 그리워 더 그리워
나의 일기장 안에
모든 말을 다 꺼내어 줄 순 없지만
사랑한다는 말
이 밤 그날의 반딧불을 당신의
창 가까이 띄울게요
음 좋은 꿈 이길 바라요
```
# Use as a Python package
melon-api can be installed from pypi
```bash
pip install melonapi
```
### Example usage 
[![Run on Repl.it](https://repl.it/badge/github/ko28/melonapi-example)](https://repl.it/@ko28/melonapi-example)

Printing out the top 100 songs right now on Melon.
```python
from melonapi import scrapeMelon
print(scrapeMelon.getList("LIVE").decode())
```
# Local Development
Run the following command inside the melonapi folder to serve up flask web app.
`FLASK_APP=melonapi.py FLASK_ENV=development flask run --port 8000`
Navigate to `localhost:8000` to access the app. 

# Misc information
Add this to your .bashrc or run it in your shell or add it to heroku config vars if you want spotify playlist
https://developer.spotify.com/
* export client_id='yourClientID'
* export client_secret='yourClientSecret'

add (flask.request.host_url or localhost:8000) + 'spotify/playlist' to valid redirect link


# Todo
- [ ] Search (by name, genre, etc)
- [ ] Playlist creation, list of song id's and create a new playlist (reverse engineering)
- [ ] List most popular songs of a given artist
- [ ] Visualize data 
- [x] Download lyric support
- [ ] Top 100 songs => Spotify Playlist conversion (nontrival task as spotify search is not very good for korean input, apple music search is really good but their api rate limited me so i tried tor but seemed like abuse) 
- [ ] Caching results (https://hackernoon.com/a-cache-is-fast-enhancing-our-api-with-redis-bd61d13c3ca8 and http://ghibliapi.herokuapp.com/#section/Helper-Libraries)
- [x] Refractor scrapeMelon to remove subprocess, this will not work on windows machines which do not have cURL 
- [ ] Auto push to pip using github actions
