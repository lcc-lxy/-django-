from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^add_book',views.add_book),
    url(r'^all_book',views.all_book),
    url(r'^detail/(\S+)/',views.detail),
    url(r'^update_book/(\S+)',views.update_book),
    url(r'^delete/(\S+)',views.delete)
]