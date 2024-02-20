from django.views.generic import ListView
from .models import SkateParts


class SkatePartsListView(ListView):
    model = SkateParts
    context_object_name = 'my_parts'
