import requests

r = requests.get('https://www.oreilly.com/index.html')  # obiekt klasy Response

html_text: str = r.text  # całość kodu HTML strony

json_text: dict = r.json()  # jeżeli wykonujemy request do API zwracającego JSON możemy wczytać to do pythonowego słownika w ten sposób

r.encoding = 'utf-8'  # możemy również wymusić dowolne kodowanie znaków

print(r)  # wynik: <Response [200]>
print(r.status_code)  # wynik: 200
# W ten sposób można sprawdzić kody 2xx, 4xx, 5xx.
# Zapisany kod nigdy nie będzie kodem oznaczającym przekierowanie
# Aby rozpoznać przekierowania (kody 3xx, głównie 301 i 302) należy użyć atrybutu history
status_code_history: list = r.history
# każde przekierowanie do czasu natrafienia na kod 2xx, 4xx lub 5xx znajduje się na tej liście
# zwrócona lista będzie pusta, jeżeli nie wystąpiły żadne przekierowania

post_request = requests.post('https://example.com/api', data={'username': 'estera'})



r = requests.get('https://www.reddit.com/r/python/new.json?sort=new')
print(r.text)  # wynik: '{"message": "Too Many Requests", "error": 429}'

headers = {'user-agent': 'kamil.kwapisz.pl'}
r = requests.get('https://www.reddit.com/r/python/new.json?sort=new', headers=headers)
print(r.status_code)  # wynik: 200


from user_agent import generate_user_agent
user_agent = generate_user_agent(os=('mac', 'linux', 'win'))
# losowo wygenerowany user-agent może wskazywać na jeden z podanych systemów operacyjnych
