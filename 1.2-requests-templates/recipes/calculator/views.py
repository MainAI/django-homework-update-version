from django.conf import settings
from django.shortcuts import render

DATA = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        }
    }


def recipe_choose(request, recipe_name):
    msg = f'Свяжитесь с администратором {settings.ADMIN_EMAIL}'
    recipe_temp = {}
    recipe = DATA.get(recipe_name, -1)
    servings = int(request.GET.get("servings", 1))
    if servings >= 1 and recipe != -1:
        for k, v in recipe.items():
            recipe_temp[k] = v * servings
    context = {'recipe_name': recipe_name, 'recipe': recipe_temp, 'msg': msg}
    return render(request, "calculator/index.html", context)



