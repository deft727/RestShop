from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import CategorySerializer,\
                        SmartphoneSerializer,\
                        NotebookSerializer,\
                        CustomerSerializer
from .models import *
from rest_framework.filters import SearchFilter


class CategoryListApiView(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SmartphoneListApiView(ListAPIView):

    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()
    filter_backends = [SearchFilter]
    search_field = ['price', 'title']

    # def get_queryset(self):
    #     # print(self.request.query_params)
    #     qs = super().get_queryset()
    #     price, title = self.request.query_params.get('price'), self.request.query_params.get('title')
    #     if price and title:
    #         search_params = {'price__iexact': price, 'title__iexact':title}
    #         return qs.filter(**search_params)
    #     return qs


class NotebookListApiView(ListAPIView):

    serializer_class = NotebookSerializer
    queryset = Notebook.objects.all()
    filter_backends = [SearchFilter]
    search_field = ['price', 'title']


class SmartphoneDetail(RetrieveAPIView):

    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()
    lookup_field = 'id'


class CustomersListApiView(ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
