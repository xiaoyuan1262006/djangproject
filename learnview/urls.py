from django.conf.urls import include,url
from . import views
urlpatterns = [
    url('^$',views.index),
    url('^(\d+)$',views.detail),
    url('^getTest1$', views.getTest1),
    url('^getTest2$', views.getTest2),
    url('^getTest3$', views.getTest3),
    url('^session1$', views.session1),
    url('^session2$', views.session2),
    url('^session3$', views.session3),
    url('^session4$', views.session4),
    url('^uploadPic$',views.uploadPic),
    url('^uploadHandle$',views.uploadHandle)
]