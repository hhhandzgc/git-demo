import requests
import urllib3
# 关闭SSL警告
urllib3.disable_warnings()

# 请求公开接口，无需token
url = "https://api.github.com/users/torvalds"
# 新增 verify=False 跳过证书校验
resp = requests.get(url, verify=False)

# 判断请求成功
if resp.status_code == 200:
    data = resp.json()
    followers = data["followers"]
    print(f"Linus Torvalds 的粉丝数量：{followers}")
else:
    print(f"接口请求失败，状态码：{resp.status_code}")
