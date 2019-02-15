from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home_page,name = 'home_page'),
    url('^register/', views.registration, name='register'),
    url('^spacing/', views.space, name='spacing'),
    url('^dailys/', views.daily, name='dailys'),
    url('^predict/', views.prediction, name='predict'),
    url('^fut/', views.future, name='fut'),

]