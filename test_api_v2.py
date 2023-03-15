from requests import get, put, delete, post
from pprint import pprint

url = 'http://localhost:8080/api/v2/'

pprint(get(url + 'users').json())  # все пользователи
pprint(get(url + 'users/1').json())  # верный запрос
pprint(get(url + 'users/999').json())  # несуществующий пользователь
pprint(get(url + 'users/q').json())  # неверный запрос


print(post(url + 'users',
           json={'surname': 'И',
                 'name': 'Петя',
                 'age': 22,
                 'position': 'уборщик',
                 'speciality': 'инженер',
                 'address': 'Советский Союз',
                 'email': 'a123@a2.com',
                 'password': '124'}).json()) # верный запрос

print(delete(url + 'users/999').json()) # несуществующий пользователь
print(delete(url + 'users/6').json())  # верный запрос