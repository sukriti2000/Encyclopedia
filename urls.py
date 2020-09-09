from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.result,name="result"),
    path("links/<str:title>",views.links,name="links"),
    path("search",views.search,name="search"),
    path("new_page",views.add,name="add"),
    path("randoms",views.randoms,name="randoms"),
    path("form",views.form,name="form"),
    path("links/edit_entries/<str:title>",views.edit_entries,name="edit_entries"),
    path("edit_result",views.edit,name="edit_result")

]
