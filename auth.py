# -*- coding: utf-8 -*-
import vk_api
from pprint import pprint
from VKtoken import access_token

session = vk_api.VkApi(token=access_token)
vk = session.get_api()
if __name__ == '__main__':
    pprint(vk.users.get(user_ids=[8206076], fields='bdate,city,country,sex,photo_max'))
