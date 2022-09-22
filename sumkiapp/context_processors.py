from .forms import Searchform
from .models import ProductCategory


def include_search_form(request):
    search_form = Searchform()
    return {'search_form': search_form}

def header_context(request):
    categories = ProductCategory.objects.all()
    return {'header_categories': categories}
