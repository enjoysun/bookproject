from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.index),
    url(r'^bookdetail/book=(?P<bid>[0-9]{1,})/$',views.bookdetail)
]