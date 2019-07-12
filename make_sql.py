import sqlite3 as sq
from parsing import *
from paint import *

def construct(jobs, city, job, base_url):
    #Build all values together
    minn = 1000000
    maxx = 0
    summ = 0

    #Find minimal and maximal salary
    for i in jobs:
        if i < minn and i>=5000:
            minn = i
        if i > maxx:
            maxx = i
        summ += i

    middle_pay = summ//len(jobs)
    variation = str(minn)+' - '+str(maxx)
    if city == 1:
        town = 'Moscow'
    else:
        town = 'SaintP'

    prof = job
    if prof =='C%2B%2B':
        prof = 'C++'

    vacansy = number_vacancy(base_url)
    return (prof, town, middle_pay, vacansy, variation)


def main():
    conn = sq.connect('professions.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE professions ('Profession' text, 'City' text, 'Average salary' int, 'Number of vacansy' int , 'Salary difference' text)")
    variaty = ['Python','1C','Java','Javascript','C%2B%2B']

    # Fill DB
    for job in variaty:
        print(job)
        for city in range(1,3):
            print('#',city,'#')
            jobs = [] #not Steve
            link = 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=' + str(city) + '&clusters=true&enable_snippets=true&only_with_salary=true&text='+job+'&page='
            for page in range(1, number_pages(jobs, job)):
                print('page:',page)
                base_url = link + str(page)
                hh_parse(base_url, jobs)
            
            cur.execute("INSERT INTO professions VALUES(?, ?, ?, ?, ?)",construct(jobs, city, job, base_url))
            conn.commit()
    
    cur.close()
    conn.close()
