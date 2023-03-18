from email import header
from matplotlib.font_manager import json_dump
from hashlib import md5
import requests
import time
import math
import json

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "insert_cookie=34835379",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}
id = '361276'
source_data = '{"id":%s}' % id
current_time = math.floor(time.time())

data = {
    "data": source_data,
    "version": "1.0",
    "time": current_time,
    "sign": md5(("fileDownloadService" + str(current_time) + source_data + "1.0" + "8HkocpYLeG1LNi5m").encode('utf-8')).hexdigest()
}

print(data)

get_response = requests.post("http://114.251.10.30/enterprise/api/fileDownloadService", headers=headers, data=data)

with open(id, 'wb') as f:
    f.write(get_response.content)