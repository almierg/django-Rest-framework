from django.urls import path
from haber_app.api import views as api_views

urlpatterns = [
    path('makaleler/', api_views.MakaleListCreateAPIView.as_view(), name='makale_listesi'),
    path('makaleler/<int:pk>/', api_views.MakaleDetailAPIView.as_view(), name='makale_detay'),
]









# urlpatterns = [
#     path('makaleler/', api_views.makale_list_create_api_view, name='makale_listesi'),
#     path('makaleler/<int:pk>/', api_views.makale_detail_api_view, name='makale_detay'),
# ]
