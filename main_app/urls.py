from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='finches_index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='finches_detail'),
    path('finches/create/', views.FinchesCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update/', views.FinchesUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete/', views.FinchesDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('stuffs/', views.StuffsIndex.as_view(), name='stuffs_index'),
    path('stuffs/create/', views.StuffsCreate.as_view(), name='stuffs_create'),
    path('stuffs/<int:pk>/', views.StuffsDetail.as_view(), name='stuffs_detail'),
    path('stuffs/<int:pk>/update', views.StuffsUpDate.as_view(), name='stuffs_update'),
    path('stuffs/<int:pk>/delete', views.StuffsDelete.as_view(), name='stuffs_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('finches/<int:finch_id>/assoc_stuff/<int:stuff_id>/', views.assoc_stuff, name='assoc_stuff'),
]