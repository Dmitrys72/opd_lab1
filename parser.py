import requests
from bs4 import BeautifulSoup

def parse():
    url = 'https://www.pepper.ru/'
    headers = {
        'authority': 'ocular.pepper.ru',
        'accept': '*/*',
        'accept-language': 'ru,en;q=0.9',
        'origin': 'https://www.pepper.ru',
        'referer': 'https://www.pepper.ru/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    count = 0
    promos = soup.find_all('div', class_='threadGrid thread-clickRoot')
    for promo in promos:
        title = promo.find('a')['title']
        link = promo.find('a')['href']
        description = promo.find('span', class_='cept-vote-temp vote-temp vote-temp--hot').text.strip()



        print(f'Название: {title}')
        print(f'Градусы: {description}')
        print(f'Ссылка: {link}\n')
        count += 1
        if count == 6:
            break