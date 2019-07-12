import matplotlib.pyplot as plt
import pylab
import sqlite3 as sq

def draw():
    #Take files from DB
    conn = sq.connect('professions.db')
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM professions")
    dates = cur.fetchall()

    #Draw first Histogamm (Average salary)
    pylab.subplot (1, 2, 1)
    pylab.title ("Average salary")
    x=0

    for i in dates:
        plt.bar(x, i[2], width = 20, label = i[0]+' '+i[1]+'.')
        x+=20

    #Draw second Histogamm (Number of vacancies) 
    pylab.subplot (1, 2, 2)
    pylab.title ("Number of vacancies")
    x=0
    for i in dates:
        plt.bar(x, i[3], width = 20, label = i[0]+' '+i[1]+'.')
        x+=20

    plt.legend(loc='upper right')
    plt.show()

    cur.close()
    conn.close()
