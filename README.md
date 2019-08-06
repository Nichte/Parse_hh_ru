# Parse_hh_ru

(you have to have requests, bl4 and matplotlib for correct working)

This project parse website hh.ru, make date base and create two histogramms on it

The main programm is main.py.
It runs all other programms, date base date and draw histogramms
 
File parsing.py parse website hh.ru.
It takes from html pages: profession, salary, number of vacansy, city

File make_sql.py create date base from parsing.py

File draw.py draw two histogramms (Average salary, Number of vacancy)

If you don't have date base: uncomment main() in file main.py and run it

