import requests
import execjs
import hashlib


def get_md5(f):
    fmd5 = hashlib.new('md5', f.encode()).hexdigest()
    return fmd5

with open('w_x-s.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

ctx = execjs.compile(jscode)
api = "/api/sns/mp/v1/user_posted?num=10&cursor=&user_id=5d2c85200000000011020dda&image_formats=jpg"
param_str = 'url='+api
a1 = '190e8738bc5mily8lgurte9tj61wab3ajybx3no3n90001365283'
md5_str = get_md5(param_str)

dic_str = ctx.call('Decrypt', md5_str,a1)
print(dic_str)


cookies = {
    # "eoId": "tog+awklpd4cR0OCS7L5wZ+dMhNFS043/JI1CJ2Smko",
    "web_session":  "0b0069b09c66075bdfc6900986344ba470e35d",
    "a1": a1,
    # "webId": "f8214215a9302cc7a327adfe8ffc6c22",
    # "acw_tc": "29cd2b255e655f4859c9511d7d22e37bcfab33a20a6b9c4bdf61164ef9fdd92e",
    # "gid": "yj8dYWqjJYV0yj8dYWqYDvIlS2631vY1k7F9DqIdj9VKyCj8E0Dq0q88yqK2JYq82qYiK0Y4"
}

headers = {
    'X-WX-EXCLUDE-CREDENTIALS': 'unionid, cloudbase-access-token, openid',
    'XX-WX-REGION': 'ap-shanghai',
    'X-WX-GATEWAY-ID': 'weixing-gateway-test-8bbcdf0f641',
    'HOST': 'edith.xiaohongshu.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a1b)XWEB/9193',
    'X-S': dic_str['x-s'],
    'X-T': dic_str['x-t'],
    'content-type':'application/json',
    'referer':'https://servicewechat.com/wxb296433268a1c654/128/page-frame.html',
    'X-WX-ENV':'xhs-test-9gdy28ik50bbd955'
}

response = requests.get('https://www.xiaohongshu.com'+api,cookies=cookies,headers=headers)
print(response.text)
