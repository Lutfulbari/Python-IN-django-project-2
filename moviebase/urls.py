from django.urls import path
from moviebase import views

urlpatterns =[
    path('',views.home,name="home"),
    path('movie/<slug:key>',views.oneMovie,name="oneMovie"),  
    path('actor/<slug:key>',views.oneActor,name="oneActor"),  
]