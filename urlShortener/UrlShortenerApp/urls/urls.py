from django.urls import path
from .apis import UrlCreateApi

urlpatterns = [
    path('url/', UrlCreateApi.as_view(), name='add-url'),
   
]