import vk_api
import time
import random

token = "6cd04ef05746111757c23d3fdd31bcc7c5c1f1b1ec9b85ec068abd783181254f1e05a8dcc6622abe64a63"

vk = vk_api.VkApi(token=token)

vk._auth_token()

while True:
    try:
        # check messages
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        # if the number of messages
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            # text
            if body.lower() == "hello":
                vk.method("messages.send",
                          {"peer_id": id, "message": "Hello", "random_id": random.randint(1, 2147483647)})

            else:
                vk.method("messages.send",
                          {"peer_id": id, "message": "What?", "random_id": random.randint(1, 2147483647)})

    except Exception:
        print('Try to find mistakes!')
        time.sleep(3)
