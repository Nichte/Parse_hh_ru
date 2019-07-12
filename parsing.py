import requests
from bs4 import BeautifulSoup as bs
from re import sub

def number_vacancy(base_url):
    global session
    global headers
    req = session.get(base_url, headers=headers)
    soup = bs(req.content, 'html.parser')
    k_vo = soup.find('h1', attrs= {'class':'header HH-SearchVacancyDropClusters-Header'}).text
    preority = ''

    #take from title only digits
    for i in k_vo:
        if i.isdigit():
            preority += i
            continue
        elif i == 'в':
            break
    return int(preority)


def del_chars(string):
    check = 1

    #Delete from salary all symbol besides of '-'
    #Currency conversion
    for i in string:
        if i == 'S':
            check = 63
        elif i == 'R':
            check = 71
        if not i.isdigit() and i not in '-':
            string = string[:string.index(i)] + string[string.index(i)+1:]
    return [check * i for i in map(int, string.split('-'))]


def hh_parse(base_url, jobs):

    #Take from html page vacancy only
    global session
    global headers
    request = session.get(base_url, headers = headers)
    soup = bs(request.content, 'html.parser')
    proposols = soup.find_all('div',attrs={'data-qa':'vacancy-serp__vacancy-compensation'})

    for proposol in proposols:
        for i in del_chars(sub('[отдо руб.]', '', proposol.text)):
            jobs.append(i)


def number_pages(jobs,job):
    global session
    global headers
    base_url = 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&only_with_salary=true&text='+job+'&page=0'
    request = session.get(base_url, headers = headers)
    soup = bs(request.content, 'html.parser')

    # find number of pages
    numbers = soup.find_all('a', attrs={'class':'bloko-button HH-Pager-Control'})
    try:
        number = int(numbers[len(numbers)-1].text)
    except IndexError:
        number = 1
    # Fill in JOBS by first page
    proposols = soup.find_all('div',attrs={'data-qa':'vacancy-serp__vacancy-compensation'})
    for proposol in proposols:
        for i in del_chars(sub('[отдо руб.]', '', proposol.text)):
            jobs.append(i)

    return number


headers = {'accept':'*/*',
           'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
session = requests.Session()

#This code take from proposals only necessary skills
#requer = proposol.find('div',attrs={'data-qa':'vacancy-serp__vacancy_snippet_requirement'}).text
