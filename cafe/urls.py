# For static Images uploaded
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="CafeHome"),
    path("entry/", views.entry, name="CafeEntry"),
    path("add-sale/", views.add_sale, name="AddSale"),
    path("del-sale/", views.del_sale, name="DeleteSale"),
    path("search-sale/", views.search_sale, name="SearchSale"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)