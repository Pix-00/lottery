import os
import random

from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(__file__)


def fetch(path):
    with open(path, 'rb') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'lxml')
    user_element_list = soup.find_all('a', {'class': 'user-name c-pointer'})
    user_list = list()
    with open(f'{BASE_DIR}/output/users_list.txt', 'wb') as f:
        for user_element in user_element_list:
            user_list.append(user_element.text)
            f.write(f'{user_element.text}\n'.encode('utf-8'))
    return user_list


def dereplicate(source):
    result = list(set(source))
    result.sort()
    with open(f'{BASE_DIR}/output/dereplicated_user_list.txt', 'wb') as f:
        for user in result:
            f.write(f'{user}\n'.encode('utf-8'))
    return result


def select(seed, user_list):
    random.seed(seed)
    return random.sample(user_list, k=2)


if __name__ == '__main__':
    final_result = select(
        '2019-10-05T04:00:00',
        dereplicate(fetch(f'{BASE_DIR}/web/SCP配音团的动态-哔哩哔哩.html')))
    print(final_result)
