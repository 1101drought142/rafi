from django.views.generic import ListView
from .models import Category, Item
from .logic import create_category_tree

class CategoryListView(ListView):
    model = Category
    template_name = 'categoty_tree.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        objects = context["object_list"]
        category_tree = create_category_tree(objects)
        context["category_tree"] = category_tree
        return context