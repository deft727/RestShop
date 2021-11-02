from django.urls import path
from .views import *


urlpatterns = [
    path('customers/', CustomersListApiView.as_view()),
    path('categories/', CategoryListApiView.as_view()),
    path('smartphones/', SmartphoneListApiView.as_view()),
    path('notebooks/', NotebookListApiView.as_view()),
    path('smartphones/<str:id>/',  SmartphoneDetail.as_view())
]
