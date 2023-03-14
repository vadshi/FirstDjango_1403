from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path("about", views.about),
    path('item/<int:id>', views.get_item),
    path('items', views.items_list)
]
