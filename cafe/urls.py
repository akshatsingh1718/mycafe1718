# For static Images uploaded
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="CafeHome"),
    path("entry/", views.entry, name="CafeEntry"),
    path("add-sale/", views.add_sale, name="AddSale")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)