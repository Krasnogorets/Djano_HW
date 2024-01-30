import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def log(view):
    def wrapper(request, *args, **kwargs):
        res = view(request, *args, **kwargs)
        logger.info(f' функция {view.__name__} вернула {res.content.decode("utf-8")}')
        return res

    return wrapper


html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Main</title>
</head>
<body>
<h2>Главная</h2>
<h3>предварительный макет сайта на Django</h3>
</body>
</html>"""

html1 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About</title>
</head>
<body>
<h2>Обо мне</h2>
<h3>Филипп, начинающий программист на Python, 46 лет))</h3>
<p>hfhfhjfjjfjffjjfjfjfkfkkfkf</p>
</body>
</html>"""


@log
def index(request):
    return HttpResponse(html)

@log
def about(request):
    return HttpResponse(html1)


