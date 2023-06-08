from bs4 import BeautifulSoup as bs
import requests
import csv

# Необходимо чтобы в запросе была информация о браузере. Формируем заголовок
header = {'accept': '*/*',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                        '(HTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

# Адрес для парсинга
url ='https://smart-lab.ru/q/'


def parse(url, header):
    g = 0

    request = requests.get(url, headers=header)
    array_A = []
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        table = soup.find_all('table', {'class': 'simple-little-table trades-table'})
        for tr in table:
            td = tr.find_all('tr', )
            for a in td:
                t = a.find_all('td', )
                g +=1
                if g > 2: # пропуск двух строчек которые нам не интересны
                    array_A.append([t[0].text, t[2].text, t[3].text, t[7].text, t[9].text])

    else:
        print('no connection')
    return array_A


def export_csv(data):

    # Пустой список
    repack = []
    # Заголовки полей будущей таблицы
    header_names = ['№', 'Название', 'Код', 'Цена', 'Что-то']

    # Работа с CSV файлом
    # Открытие
    # Запись заголовка

    with open('indexes.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=header_names)
        writer.writeheader()

        for stock in data:
            writer.writerow(dict(zip(header_names, stock)))


# Программа выполняется отсюда. Сначала парсим котировки, а затем сохраняем в CSV
kotirovki = parse(url, header)
export_csv(kotirovki)