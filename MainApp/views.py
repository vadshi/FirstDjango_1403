from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    context = {
        "name": 'Петров Николай Иванович',
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)


def about(request):
    author = {
        "name": "Иван",
        "middle": "Петрович",
        "surname": "Иванов",
        "phone": "8-923-600-01-02",
        "email": "vasya@mail.ru"
    }
    result = f"""
    Имя: <b>{author["name"]}</b><br>
    Отчество: <b>{author["middle"]}</b><br>
    Фамилия: <b>{author["surname"]}</b><br>
    Телефон: <b>{author["phone"]}</b><br>
    Email: <b>{author["email"]}</b><br>
    <a href='/'> Home </a>
    """
    return HttpResponse(result)

# url /item/1
# url /item/2


def get_item(request, id):
    """ По указанному id функция возвращает имя и кол-во через шаблон """
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Item with id={id} not found')
    else:
        context = {
            'item': item
        }
        return render(request, "item-page.html", context)


def items_list(request):
    """ Функция для отображения списка товаров """
    items = Item.objects.all()
    context = {
        "items": items
    }
    # Аргументы render: Запрос(request), Имя файла-шаблона, Контекст(чем заполняем)
    return render(request, "items-list.html", context)
