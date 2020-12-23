from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^predict/', views.predictnote),
    url(r'^predictfile/', views.predict_file),
]