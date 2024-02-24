from django.urls import path

from .views import shape_view

urlpatterns = [
    path("shape-list/", shape_view.ShapeList.as_view(), name="shape-list"),
]
