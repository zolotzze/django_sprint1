from django.shortcuts import render
from django.http import Http404

# Список постов
posts: list = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
    },
]

# Создаем словарь из списка постов
POSTS = {post['id']: post for post in posts}


def index(request):
    """
    Отображает главную страницу блога.

    Args:
        request: Запрос от клиента.

    Returns:
        HTTP-ответ с отображением главной страницы блога и списком постов.
    """
    context = {'posts': posts[::-1]}

    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    """
    Отображает детали конкретного поста блога.

    Args:
        request: Запрос от клиента.
        post_id: Идентификатор поста.

    Returns:
        HTTP-ответ с отображением деталей конкретного поста блога.
    """
    post = POSTS.get(post_id)

    if post is None:
        raise Http404(f'Пост под номером {post_id} не существует')

    context = {'post': post}

    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """
    Отображает посты определенной категории блога.

    Args:
        request: Запрос от клиента.
        category_slug: Уникальный идентификатор категории.

    Returns:
        HTTP-ответ с отображением постов определенной
        категории блога.
    """
    return render(request, template_name='blog/category.html',
                  context={'category_slug': category_slug}
                  )
