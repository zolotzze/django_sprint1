from django.shortcuts import render


def about(request):
    """
    Отображает страницу "О проекте".

    Args:
        request: Запрос от клиента.

    Returns:
        HTTP-ответ с отображением страницы "О проекте".
    """
    return render(request, template_name='pages/about.html')


def rules(request):
    """
    Отображает страницу "Наши правила".

    Args:
        request: Запрос от клиента.

    Returns:
        HTTP-ответ с отображением страницы "Наши правила".
    """
    return render(request, template_name='pages/rules.html')
