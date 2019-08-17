from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime

token = "6cd04ef05746111757c23d3fdd31bcc7c5c1f1b1ec9b85ec068abd783181254f1e05a8dcc6622abe64a63"
vk_session = vk_api.VkApi(token=token)  # authorization

session_api = vk_session.get_api()  # new events
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('message came in: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))  # time
            print('message: ' + str(event.text))