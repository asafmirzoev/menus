from django.db.models import QuerySet

from menu.models import Category


def generate_menu(menu_id: int, categories: QuerySet[Category], url: str, nesting: int = 0, parents_id: list = []) -> str:
    
    html: str = '<div class="list-group well">'
    color: str = generate_hex_color()

    nesting += 1
    for category in categories:
        parents_id.append(str(category.pk))

        category_url: str = f'/{menu_id}/' + '-'.join(parents_id)
        active = category_url in url

        html += f'<a href="#item-{"-".join(parents_id)}" data-url="{category_url}" class="list-group-item ml-{nesting} {"collapsed" if active else ""}" aria-expanded="{"true" if active else "false"}" data-toggle="collapse" style="background-color: {color}; text-decoration: none; color: #fff">{ category.name } <i class="fas fa-arrow-down"></i></a><div class="list-group collapse {"show" if active else ""}" id="item-{"-".join(parents_id)}">'
        html += generate_menu(menu_id, category.category_set.all(), url, nesting, parents_id)
        html += '</div>'

        parents_id.remove(str(category.pk))
    html += '</div>'
    return html


def generate_hex_color() -> str:
    import random
    color = '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
    return color