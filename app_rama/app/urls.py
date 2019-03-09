from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^pracownicy/(?P<masseur_id>[0-9]+)/$', views.masseur_detail, name='masseur_detail'),
    url(r'^zamow_masaz/$', views.order_massage, name='order_massage'),
    url(r'^aplikuj/$', views.polish_form_application, name='polish_form_application'),
    url(r'^podziekowania_za_aplikacje/$', views.thank_you_page_pl, name='thank_you_page_pl'),
    url(r'^posty_bloga/$', views.blog_list, name='blog_list'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
]