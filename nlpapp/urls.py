from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('product', views.products, name='product'),
    path('consulting', views.consulting, name='consulting'),
    path('services', views.service, name='services'),
    path('training', views.training, name='training'),
    path('career', views.career, name='career'),
    path('internship', views.internship, name='internship'),
    path('contact', views.contact, name='contact'),
    path('internapply',views.intern_apply,name='internform'),
    path('thank', views.thank, name='thank'),#for contact
    path('ithank', views.ithank, name='ithank'),#for intern/CARERTR
    path('pay',views.payment,name='pay'),
    path('payfrm',views.payment_form,name='payform'),
    path('cnsl',views.cnsal_save,name='cnslsave'),
]