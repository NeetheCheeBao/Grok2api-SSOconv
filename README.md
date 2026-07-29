# Grok2api-SSOconv

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> 如果你使用了 [Grok Register](https://github.com/AaronL725/grok-register) ，账号导出成功但是是 （`邮箱----密码----sso_token`） 的格式，导入到 [grok2api](https://github.com/chenyme/grok2api) 账号却无法正常识别及使用。此脚本可批量解析并自动转换为 `JSON` 格式的账号文件。

---

示例原文件格式：

```text
yl448k4fc0@110666666.xyz----N5c8892a5!a7#Z400yY2k----eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiMWQ4NzY4ODAtNTFmZi00MjQ4LTllNmEtNDNiYTk2YTlhMjg5In0.HpmSEVwxDvV6QeaZLUAvji-bKRgqoS0y6z4k1kBskuc`
```

---

转化后格式：

```json
{
  "provider": "grok_web",
  "accounts": [
    {
      "name": "yl448k4fc0@110666666.xyz",
      "email": "yl448k4fc0@110666666.xyz",
      "sso_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiMWQ4NzY4ODAtNTFmZi00MjQ4LTllNmEtNDNiYTk2YTlhMjg5In0.HpmSEVwxDvV6QeaZLUAvji-bKRgqoS0y6z4k1kBskuc",
      "token": "",
      "tier": "basic",
      "cloudflare_cookies": ""
    }
  ]
}
```

## 🛠️ 使用说明

### 1. 重命名文件

将你要转换的`账号文件`放置在脚本**同一目录下**，并重命名为：

```text
groksso.txt
```

### 2. 运行脚本

直接使用 Python 运行 `Grok2api-SSOconv.py` ：

```bash
python Grok2api-SSOconv.py
```

### 3. 查看输出

脚本运行完成后，将在同一目录下自动生成：

```text
output.txt
```

- `output.txt` 可直接导入 [grok2api](https://github.com/chenyme/grok2api) 并且账号被正常识别。

## ⚖️ 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。