from django.urls import path
from smarthulk import views

urlpatterns = [
    path('',views.index,),
    path('meditation',views.meditation,),
    path('emotion',views.emotion,),
    path('diary',views.diary,),
]