import json
import os
import sys
import time

# ==========================================
# 工具名称：Grok2api-SSOconv
# 功能：自动查找当前目录下的 groksso.txt 并转存为 output.txt (JSON 格式)
# ==========================================

def main():
    print("=" * 50)
    print("       Grok2api-SSOconv 账号格式转换工具")
    print("=" * 50)

    # 1. 自动识别脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"[日志] 脚本工作目录: {current_dir}")

    # 2. 搜索目录下名称为 "groksso.txt" 的文件（大小写不敏感）
    target_filename = "groksso.txt"
    found_file = None

    for file_name in os.listdir(current_dir):
        if file_name.lower() == target_filename:
            found_file = os.path.join(current_dir, file_name)
            break

    if not found_file:
        print(f"[错误] 未在当前目录下找到 '{target_filename}' 文件！")
        countdown_and_exit(5)
        return

    print(f"[日志] 成功匹配输入文件: {found_file}")

    # 3. 读取并解析文件内容
    accounts = []
    skipped_lines = 0

    try:
        with open(found_file, "r", encoding="utf-8") as f:
            for line_number, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue

                parts = line.split("----")
                if len(parts) >= 3:
                    email = parts[0].strip()
                    sso_token = parts[2].strip()

                    accounts.append({
                        "name": email,
                        "email": email,
                        "sso_token": sso_token,
                        "token": "",
                        "tier": "basic",
                        "cloudflare_cookies": ""
                    })
                    print(f"[解析成功] 行 {line_number}: {email}")
                else:
                    skipped_lines += 1
                    print(f"[格式忽略] 行 {line_number}: 未满足 '----' 3段式结构，跳过处理")

    except Exception as e:
        print(f"[异常错误] 读取或解析文件失败: {e}")
        countdown_and_exit(5)
        return

    # 4. 构建输出 JSON 结构
    output_data = {
        "provider": "grok_web",
        "accounts": accounts
    }

    output_path = os.path.join(current_dir, "output.txt")

    # 5. 写入到当前位置的 output.txt（如存在直接覆盖）
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print("-" * 50)
        print(f"[日志] 转换完成！有效账号: {len(accounts)} 条，跳过行数: {skipped_lines} 行。")
        print(f"[成功] 结果已覆盖写入至: {output_path}")
    except Exception as e:
        print(f"[异常错误] 写入 output.txt 文件失败: {e}")

    # 6. 控制台倒计时 5 秒后退出
    print("-" * 50)
    countdown_and_exit(5)


def countdown_and_exit(seconds):
    """倒计时并在结束后退出控制台"""
    for i in range(seconds, 0, -1):
        print(f"\r[提示] 程序将在 {i} 秒后自动关闭...", end="", flush=True)
        time.sleep(1)
    print("\n[退出] 程序已关闭。")
    sys.exit(0)


if __name__ == "__main__":
    main()