import requests

# 请求公开接口，关闭SSL证书校验
url = "https://api.github.com/users/torvalds"
resp = requests.get(url, verify=False)
data = resp.json()
# 提取粉丝数量
followers = data["followers"]
print(f"Linus Torvalds 粉丝数：{followers}")
