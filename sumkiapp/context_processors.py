from .forms import Searchform


def include_search_form(request):
	search_form = Searchform()
	return {'search_form': search_form}
