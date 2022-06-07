from django.urls import path
from . import views
urlpatterns = [
    path("whatsapp/api",views.whatsAppGet)
]