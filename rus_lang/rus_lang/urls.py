from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("rus_lang_ege.urls", namespace="rus_lang_ege")),

]
