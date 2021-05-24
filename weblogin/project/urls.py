
from django.urls import path

from . import views

urlpatterns = [

        path('', views.index, name="index"),
        path('login', views.login_func, name='login_details'),
        path("logout", views.logout_view, name="logout"),
        path('register', views.register, name='register'),
        path('dashboard', views.patient_func, name='patient_details'),
        path('dashboard1', views.oxygen_func, name='oxygen_details'),
        path('dashboard2', views.plasma_func, name='plasma_details'),
        path('patientlist', views.load_pat, name='pat'),
        path('oxygen', views.load_oxy, name='oxy'),
        path('plasma', views.load_plas, name='plas'),
        path('FAQs', views.FAQs, name='FAQs'),
        path('contactus', views.contactus, name='contact'),
        path('about', views.about, name='about'),
        path('bedsdelhi', views.bedsdelhi, name='beds'),
        path('delhiplasmaofficial', views.delhiplasma, name="delhiplasma"),
        path(r'^deletedata/(?P<id>)/(?P<id_type>)/',views.deletedata, name="deletedata")
]
