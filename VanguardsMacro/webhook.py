import requests
import time
import json
import datetime


webhook_url = "https://discord.com/api/webhooks/1433437014610673694/3rVtv0_KxlRTMYs6hOOTrHmZ94LznHXfbuJNssXWD1-jtdpjpvvkz4R00v_KrVnX2_S9"

def send_webhook(win:int,lose:int,run_time: str, rewards: int, task_name: int, img, rewardsmin: int | None=None, rewardsmax: int | None=None):

    
    win_ratio = (win/(win+lose))*100
    rewards = str(rewards)
    if rewardsmin and rewardsmax is not None:
        rewards = f"{rewardsmin}-{rewardsmax}"
    payload = {
        
    "username": "Loxer's Automation",
    "avatar_url": "https://i.pinimg.com/736x/97/10/48/97104879f559410dcdb09999d1910f2e.jpg",
    "embeds": [
        {
        "title": "Loxer's Automation",
        "description": "",
        "color": 3447003,
        "fields": [
            {
            "name": "🕒 Run Time",
            "value": run_time,
            "inline": True
            },
            {
            "name": "⚔️ Wins",
            "value": win,
            "inline": True
            },
            {
            "name": "📈 Success Rate",
            "value": f"{win_ratio:.2f}%",
            "inline": True
            },
            {
            "name": "🔁 Total Runs",
            "value": win+lose,
            "inline": True
            },
            {
            "name": "💰 Rewards",
            
                "value": f"{rewards} collected",
            "inline": True
            },
            {
            "name": "⚙️ Current Task",
            "value": task_name
            }
        ],
        "image": {
            "url": "attachment://screenshot.png",
        },
        "thumbnail": {
            "url": "https://media1.tenor.com/m/m0KNx_D9YKoAAAAC/dio-the-world.gif",
        },
        "footer": {
            "text": f"Loxer's Automation | Run time: {run_time}",
            "icon_url": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDRlMno0eXBhM2Uyb2hoYzJlYnJ6dW05NWQwdTE0dHd6MW9saXJ3eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6UL3rqweR5Y2Jcrnqb/giphy.gif"
        },
        "timestamp": datetime.datetime.utcnow().isoformat()
        }
    ]
    }
    files = {
        "file": ("screenshot.png", img, "image/png")  # name must match attachment:// name
   
    }

    

    response = requests.post(webhook_url, data={"payload_json": json.dumps(payload)}, files=files)
    #print(response.status_code, response.text)

