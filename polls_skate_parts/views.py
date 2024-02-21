from django.views.generic import ListView, DetailView
from .models import SkateParts


class SkatePartsListView(ListView):
    """
    ListView: To display a list of objects.
    """
    model = SkateParts
    context_object_name = 'my_parts'


class SkatePartsDetailView(DetailView):
    """
    DetailView: To display details of a single object.
    """
    model = SkateParts
    context_object_name = 'my_part'
