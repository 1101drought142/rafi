from dataclasses import dataclass
from django.db.models.query import QuerySet
from .models import Category

@dataclass
class FormatCategory:
    value: Category
    children: list[Category]

def create_category_tree(list_of_categories : QuerySet) -> list[FormatCategory]:
    result = []
    pre_formated_result = [FormatCategory(category, []) for category in list_of_categories]
    for category in pre_formated_result:
        if category.value.father_category is None:
            result.append(category)
        else:
            for seccat in pre_formated_result:
                if (seccat.value.id == category.value.father_category.id):
                    seccat.children.append(category)
    return result