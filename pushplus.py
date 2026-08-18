import os
import requests

PUSHPLUS_API = "https://www.pushplus.plus/send"

def send_pushplus(title: str, content: str, template: str = "html"):
    """
    发送 PushPlus 消息推送
    :param title: 消息标题
    :param content: 消息内容（支持 HTML）
    :param template: 模板类型：html / markdown / json
    """
    token = os.environ.get("PUSHPLUS_TOKEN", "")
    if not token:
        print("[PushPlus] PUSHPLUS_TOKEN 未设置，跳过推送")
        return

    payload = {
        "token": token,
        "title": title,
        "content": content,
        "template": template,
    }

    try:
        resp = requests.post(PUSHPLUS_API, json=payload, timeout=15)
        data = resp.json()
        if data.get("code") == 200:
            print(f"[PushPlus] 推送成功: {data.get('msg')}")
        else:
            print(f"[PushPlus] 推送失败: {data.get('msg')} (code: {data.get('code')})")
    except Exception as e:
        print(f"[PushPlus] 推送异常: {e}")
