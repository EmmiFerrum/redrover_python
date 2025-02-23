from requests import request
from http import HTTPStatus
from config import BASE_URL
# API, который использовался для написания автотестов: <https://reqres.in/>
print(BASE_URL)
single_user_response = {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": BASE_URL+'/img/faces/2-image.jpg',
    },
    "support": {
        "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    },
}


def test_single_user():
    response = request(
        method="GET",
        # Можем вынести основной адрес в отдельную переменную
        # и использовать вместо "https://reqres.in/"
        url=BASE_URL+'/api/users/2',
    )

    # Как минимум необходимо проверить статус код и ответ.
    assert response.status_code == 200
    # Можем сравнивать отдельно каждое поле,
    # но лучше всего сравнить все данные сразу
    # В данном случае данные статичные и нам не нужно что то дополнительно получать или генерировать.
    assert response.json() == single_user_response


# Для большей читаемости можем написать первые кастомные assertions.
# Или использовать готовую библиотеку для сравнений. 

# Кастомный пример
def should_be_equal(first, second):
    assert first == second, "Значения не совпадают"

def test_register():
    response = request(
        method="POST",
        url= BASE_URL+'/api/register',
        # Отправляем JSON так как этого требуте наше api. 
        # Так же с помощью requests можем отправлять data, files и params при необходимости.
        json={"email": "eve.holt@reqres.in", "password": "pistol"},
    )

    # Можем использовать HTTPStatus или просто указать статус код как число. 
    # HTTPStatus.OK или 200
    should_be_equal(response.status_code, HTTPStatus.OK) 
    should_be_equal(response.json(), {"id": 4, "token": "QpwL5tke4Pnpja7X4"})

# На данном этапе уже понятно, что тестовые данные стоит хранить отдельно от тестов.  
list_of_users_response = {
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [
        {
            "id": 7,
            "email": "michael.lawson@reqres.in",
            "first_name": "Michael",
            "last_name": "Lawson",
            "avatar": BASE_URL+'/img/faces/7-image.jpg'
        },
        {
            "id": 8,
            "email": "lindsay.ferguson@reqres.in",
            "first_name": "Lindsay",
            "last_name": "Ferguson",
            "avatar": BASE_URL+'/img/faces/8-image.jpg'
        },
        {
            "id": 9,
            "email": "tobias.funke@reqres.in",
            "first_name": "Tobias",
            "last_name": "Funke",
            "avatar": BASE_URL+'/img/faces/9-image.jpg'
        },
        {
            "id": 10,
            "email": "byron.fields@reqres.in",
            "first_name": "Byron",
            "last_name": "Fields",
            "avatar": BASE_URL+'/img/faces/10-image.jpg'
        },
        {
            "id": 11,
            "email": "george.edwards@reqres.in",
            "first_name": "George",
            "last_name": "Edwards",
            "avatar": BASE_URL+'/img/faces/11-image.jpg'
        },
        {
            "id": 12,
            "email": "rachel.howell@reqres.in",
            "first_name": "Rachel",
            "last_name": "Howell",
            "avatar": BASE_URL+'/img/faces/12-image.jpg'
        }
    ],
    "support": {
        "url": BASE_URL+'/#support-heading',
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}


def test_list_of_users():
    response = request(
        method="GET",
        # Передаем query string или строку запроса ?page=2
        url= BASE_URL+'/api/users?page=2',
        # Так же можно передать таким образом. 
        # params={"page": 2},
        # Пагинация: Обычно используется для указания на то, какую страницу данных хотят получить. 
        # Например, при разбиении списка результатов на страницы.
        # page=2: параметр для второй страницы.

    )

    should_be_equal(response.status_code, HTTPStatus.OK)
    should_be_equal(response.json(), list_of_users_response)