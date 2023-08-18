from django.http import HttpResponse
from django.shortcuts import render
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.




# items = [
#     {"id": 1, "name": "Кроссовки abibas", "quantity": 10},
#     {"id": 2, "name": "Куртка кожаная", "quantity": 5},
#     {"id": 3, "name": "Coca-cola 1 литр", "quantity": 20},
#     {"id": 4, "name": "Картофель фри", "quantity": 15},
#     {"id": 5, "name": "Кепка", "quantity": 8},
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
    author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}
    return HttpResponse(result)

def get_item(request, id):
    try:
        item = Item.objects.id
    return HttpResponse("Товар не найден")


def items_list(request):
    # result = "<h2>Список товаров</h2>"
    # for item in items:
    #     result += f"""<li><a href="/item/{item["id"]}">{item['name']}</li>"""
    # result += '</ol>'
    # return HttpResponse(result)
    items = Item.objects.all()
    context = {
        'items': items
        }
    return render(request, 'all_items.html', context)
