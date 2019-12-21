# melonApi
<img src="https://i.imgur.com/Igpf68Q.png" width="300">


Add this to your .bashrc or run it in your shell or add it to heroku config vars if you want spotify 
https://developer.spotify.com/
export ClientId='yourClientID'
export ClientSecret='yourClientSecret'

add flask.request.host_url + 'spotify/playlist'
flask.request.host_url + 'spotify'
to valid redirect link

https://ko28melonapi.herokuapp.com/chart/live

https://ko28melonapi.herokuapp.com/chart/rise

https://ko28melonapi.herokuapp.com/chart/day

https://ko28melonapi.herokuapp.com/chart/week

https://ko28melonapi.herokuapp.com/chart/month

TODO: download lyric support, genre support, chart with different parameters, most popular songs of a given artist  
Add spotify feature, https://hackernoon.com/a-cache-is-fast-enhancing-our-api-with-redis-bd61d13c3ca8 and caching
http://ghibliapi.herokuapp.com/#section/Helper-Libraries