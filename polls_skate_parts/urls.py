from django.urls import path

from . import views

urlpatterns = [
    path("", views.SkatePartsListView.as_view(), name="SkatePartsListView"),
]
