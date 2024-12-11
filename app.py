import requests
import time


def fetch_top_stories():
    # 変数にHTTPライブラリで、APIの情報を取得して代入する
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty")
    top_story_ids = response.json()

    for top_story_id in top_story_ids[:30]:
        time.sleep(1)  # ここで1秒止まる

        top_story_url = f"https://hacker-news.firebaseio.com/v0/item/{top_story_id}.json?print=pretty"
        top_story_response = requests.get(top_story_url)

        top_story_data = top_story_response.json()
        title = top_story_data.get("title", "None")
        url = top_story_data.get("url", "None")

        print(f"{{'title':'{title}', 'link':'{url}'}}")


if __name__ == "__main__":
    fetch_top_stories()
