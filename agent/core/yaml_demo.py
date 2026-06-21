import yaml

# 1. 读取yaml文件
with open("config.yaml", "r", encoding="utf8") as f:
    cfg = yaml.safe_load(f)

print("读取原始配置：")
print(cfg)

# 2. 修改配置字段
cfg["version"] = "0.0.2"
cfg["github_token"] = "test-token-123456"
cfg["debug"] = False

# 3. 写回文件
with open("config.yaml", "w", encoding="utf8") as f:
    yaml.dump(cfg, f, sort_keys=False, allow_unicode=True)

print("\n修改并保存完成，新版本配置：")
print(cfg)
