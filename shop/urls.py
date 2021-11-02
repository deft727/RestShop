from django.urls import path
from .views import *


urlpatterns = [

    path('catgories/', CategoryListApiView.as_view()),
    path('smartphones/', SmartphoneListApiView.as_view()),

]
