from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req= Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postData=parse.urlencode(
    [("StartStation", "a7a04c89-900b-4798-95a3-c01c455622f4"),
     ("EndStation", "38b8c40b-aef0-4d66-b257-da96ec51620e"),
     ("SearchDate", "2018/06/07"),
     ("SearchTime", "15:00"),
     ("SearchWay", "DepartureInMandarin") 
    ]
)

req.add_header("Origin","http://www.thsrc.com.tw")
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36")
resp= urlopen(req,data=postData.encode('utf-8'))
print(resp.read().decode("utf-8"))