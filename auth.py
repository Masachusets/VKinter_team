# -*- coding: utf-8 -*-
import vk_api
from pprint import pprint
from VKtoken import access_token


session = vk_api.VkApi(token=access_token)
vk = session.get_api()


def processing_photos(user_id):
    photos = vk.photos.getAll(access_token=access_token,
                              owner_id=user_id,
                              extended=1,
                              count=200,
                              photo_sizes=0)
    best_three_photos = sorted(photos['items'], key=lambda x: x['likes']['count'])[-3:]
    pprint()

def processing_applicant(user_id):
    user = vk.users.get(user_id=[user_id], fields='bdate,city,country,sex')[0]
    photos = user['id']
    # return f"{user['first_name']} {user['last_name']}\n"


def search_applicants(age, user_sex, city_id):
    offset = 0
    while offset < 30:
        offset += 1
        applicants = vk.users.search(city=city_id,
                                     sex=user_sex % 2 + 1,
                                     age_from=age - 2,
                                     age_to=age + 2,
                                     has_photo=1,
                                     offset=offset,
                                     count=1)

        yield applicants['items'][0]


if __name__ == '__main__':
    # user = vk.users.get(user_id=['angelinuska'], fields='bdate,city,country,sex')[0]

    # processing_applicant('loggvi')
    processing_photos(151171819)
    # user_city = user['city']['id']
    # user_sex = user['sex']
    # for i in search_applicants(20, user_sex, user_city):
    #     pprint(i)
