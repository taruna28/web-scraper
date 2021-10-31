import requests
from bs4 import BeautifulSoup
import string
import os

titles = []
pages_num = int(input())
type_inp = str(input())
# https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page=2
# https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page=
# https://www.nature.com/nature/articles?sort=PubDate&year=2020
url = 'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page='  # 'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page=2'  # https://www.nature.com/nature/articles
cwd = os.getcwd()
print(cwd)

for p in range(1, pages_num + 1):
    r = requests.get(url + str(p))
    print(url + str(p))
    dir_path = f'\Page_{p}'
    abs_path = str(cwd + dir_path)
    print(abs_path)
    if not os.path.exists(abs_path):
        os.makedirs(abs_path)
        os.chdir(abs_path)
    else:
        os.chdir(abs_path)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        print(soup)
        articles = soup.find_all('article')
        # print(articles)
        # print((articles))
        for article in articles:
            article_type = article.find('span', class_='c-meta__type').text
            if article_type == type_inp:
                # dir_path = f'\Page_{p}'
                # abs_path = str(cwd + dir_path)
                # print(abs_path)
                # if not os.path.exists(abs_path):
                #     os.makedirs(abs_path)
                #     os.chdir(abs_path)
                # else:
                #     os.chdir(abs_path)
                title = article.find('a', {'data-track-action': 'view article'}).text
                for punc in string.punctuation:
                    title = title.replace(punc, '')
                formatted = title.maketrans(' ', '_')
                content_url = 'https://www.nature.com' + article.find('a')['href']
                # print(content_url)
                r2 = requests.get(content_url)
                soup = BeautifulSoup(r2.content, 'html.parser')
                body = soup.find('div', class_='c-article-body').text.strip()
                # body_txt = body.text.strip()
                # print(title.translate(formatted))
                # print(body)
                file = open(f'{title.translate(formatted)}.txt', 'w', encoding='utf-8')
                file.write(body)
                file.close()
                # print(title)
                # print(content_url)
                # else:
                #     os.makedirs(dir_path)
                #     os.listdir

                # os.makedirs(dir_path)
                # os.chdir(dir_path)
                # print(os.getcwd())
                # title = article.find('a', {'data-track-action': 'view article'}).text
                # for punc in string.punctuation:
                #     title = title.replace(punc, '')
                # formatted = title.maketrans(' ', '_')
                # content_url = 'https://www.nature.com' + article.find('a')['href']
                # r2 = requests.get(content_url)
                # soup = BeautifulSoup(r2.content, 'html.parser')
                # body = soup.find('div', class_='c-article-body').text.strip()
                # # body_txt = body.text.strip()
                # file = open(f'{title.translate(formatted)}.txt', 'w', encoding='utf-8')
                # file.write(body)
                # file.close()

    else:
        print(f'The URL returned {r.status_code}')

#  Stage 4

# r = requests.get(url)
# if r.status_code == 200:
#     soup = BeautifulSoup(r.content, 'html.parser')
#     articles = soup.find_all('article')
#
#     # print(articles[5].prettify)
#     for article in articles:
#         article_type = article.find('span', class_='c-meta__type')
#         if article_type.text == 'News':
#             # titles.append(article.find('a', {'data-track-action' : 'view article'}).text)
#             title = article.find('a', {'data-track-action': 'view article'}).text
#             for punc in string.punctuation:
#                 title = title.replace(punc, '')
#             formatted = title.maketrans(' ', '_')
#             content_url = 'https://www.nature.com' + article.find('a')['href']
#             r2 = requests.get(content_url)
#             soup = BeautifulSoup(r2.content, 'html.parser')
#             body = soup.find('div', class_='c-article-body').text.strip()
#             # body_txt = body.text.strip()
#             file = open(f'{title.translate(formatted)}.txt', 'w', encoding='utf-8')
#             file.write(body)
#             file.close()
