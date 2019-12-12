import os
import random

from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(__file__)


class Lottery():
    def __init__(self, seed):
        self.seed = seed
        self.seed_ = seed.replace(':', '-')
        self.names = None
        try:
            os.makedirs(f'{BASE_DIR}/output/{self.seed_}')
        except FileExistsError:
            pass

    def fetch(self):
        with open(f'{BASE_DIR}/web/{self.seed_}.html', 'rb') as f:
            html = f.read()
        soup = BeautifulSoup(html, 'lxml')
        user_elements = soup.find_all('a', {'class': 'user-name c-pointer'})
        names = list()
        with open(f'{BASE_DIR}/output/{self.seed_}/users_list.txt', 'wb') as f:
            for element in user_elements:
                names.append(element.text)
                f.write(f'{element.text}\n'.encode('utf-8'))
        self.names = self._dereplicate(names)

    def _dereplicate(self, source):
        result = list({name: 1 for name in source}.keys())
        with open(f'{BASE_DIR}/output/{self.seed_}/dereplicated_user_list.txt',
                  'wb') as f:
            for user in result:
                f.write(f'{user}\n'.encode('utf-8'))
        return result

    def select(self, k):
        random.seed(self.seed)
        return random.sample(self.names, k=k)


if __name__ == '__main__':
    lottery = Lottery('2019-12-12T04:00:00')
    lottery.fetch()
    print(lottery.select(k=5))
