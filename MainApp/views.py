from django.http import HttpResponse
from django.shortcuts import render
from MainApp.models import Item

# Create your views here.


author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 10},
    {"id": 2, "name": "Куртка кожаная", "quantity": 5},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 20},
    {"id": 4, "name": "Картофель фри", "quantity": 15},
    {"id": 5, "name": "Кепка", "quantity": 8},
]


def home(request):
    # text = """<h1>"Изучаем django"</h1>
    #           <strong>Автор</strong>: <i>Шиховцов В.В.</i>
    #             """
    # return HttpResponse(text)
    context = {
        "name": "Петров Иван Николаевич", 
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    result = f"""
    Имя: <b>{author['Имя']}</b><br>
    Отчество: <b>{author['Отчество']}</b><br>
    Фамилия: <b>{author['Фамилия']}</b><br>
    Телефон: <b>{author['телефон']}</b><br>
    Email: <b>{author['email']}</b><br>
    """
    return HttpResponse(result)

def get_item(request, id):
    for item in items:
        if item["id"] == id:
            result = f"""
            <h2>Имя: {item["name"]}</h2>
            <p> Количество: {item["quantity"]}</p>
            <p><a href="/items"> Назад к списку товаров</a></p>
            """
            return HttpResponse(result)
    return HttpResponse("Товар не найден")


def items_list(request):
    # result = "<h2>Список товаров</h2>"
    # for item in items:
    #     result += f"""<li><a href="/item/{item["id"]}">{item['name']}</li>"""
    # result += '</ol>'
    # return HttpResponse(result)
    context = {
        'items': items
        }
    return render(request, 'all_items.html', context)
