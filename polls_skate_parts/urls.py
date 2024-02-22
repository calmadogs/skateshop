from django.urls import path

from . import views

urlpatterns = [
    path("skate-parts/", views.SkatePartsListView.as_view(), name="skate-parts-list"),
]
