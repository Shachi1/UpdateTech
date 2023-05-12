from django.urls import path
from .views import MyModelListCreateView, MyModelRetrieveUpdateDestroyView
from .views import generate_chart, show_query_result
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('data_insertion/', MyModelListCreateView.as_view(), name='mymodel-list'),
    path('data_manipulation/<int:pk>/', MyModelRetrieveUpdateDestroyView.as_view(), name='mymodel-detail'),
    path('report/', generate_chart, name='generate_chart'),
    # path('chart/', show_query_result, name='show_query_result'),
]
