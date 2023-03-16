from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path("about", views.about, name='about'),
    path('item/<int:id>', views.get_item, name='item-detail'),
    path('items', views.items_list, name='items-list')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
