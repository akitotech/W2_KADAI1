import requests
import time

# 変数にHTTPライブラリで、APIの情報を取得して代入する
response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
top_story_ids = response.json()

for top_story_id in top_story_ids[:30]:
    top_story_url = f"https://hacker-news.firebaseio.com/v0/item/{top_story_id}.json?print=pretty"
    top_story_response = requests.get(top_story_url)

    top_story_data = top_story_response.json()
    title = top_story_data.get("title", "None")
    url = top_story_data.get("url", "None")


for i in range(30):
    time.sleep(1)  # ここで1秒止まる
    print(i)

    print(f"{{'title':{title} 'link':{url}}}")
