import requests
from bs4 import BeautifulSoup
url = 'https://www.oreilly.com/index.html'

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")
# pierwszym argumentem konstruktora klasy BeautifulSoup jest zawartośc dokumentu HTML
# drugim parametrem jest parser i nad nim się chwilę zatrzymamy

body = soup.body  # korzystając z tego skrótu można dostać się do konkretnego znacznika
div = body.find('div', {'class': 'textSection error-500'})  # szukamy div'ów klasy "textSection error-500"

print(div)

# div.table.extract()  # usuwamy zawartość znaczników <table>
# ul = div.ul.extract()  # usuwamy zawartość znaczników <ul>, którą możemy zapisać do zmiennej
# # teraz w zmiennej div nie ma tabeli oraz uporządkowanej listy
# print(type(div.find('table'))) # wynik: <class 'NoneType'>