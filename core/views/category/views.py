from django.shortcuts import render

from core.models import Category


def category_list(request):
    data = {
        'title': 'Cateogry List',
        'categories': Category.objects.all(),
    }
    return render(request, 'category/list.html', data)
