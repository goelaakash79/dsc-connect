from django.urls import path
from .views import DscList, DscDetail #api_root

urlpatterns = [
	path('v1/dsc/<int:pk>/',DscDetail.as_view()),
	path('v1/dsc/', DscList.as_view()),
	#path('', views.api_root),
]
