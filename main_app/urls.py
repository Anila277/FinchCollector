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
    path('stuffs/', views.StuffWithFinchIndex.as_view(), name='stuffwithfinch_index'),
    path('stuffs/create/', views.StuffWithFinchCreate.as_view(), name='stuffwithfinch_create'),
    path('stuffs/<int:pk>/', views.StuffWithFinchDetail.as_view(), name='stuff_detail'),
    path('stuffs/<int:pk>/update', views.StuffWithFinchUpDate.as_view(), name='stuffwithfinch_update'),
    path('stuffs/<int:pk>/delete', views.StuffWithFinchDelete.as_view(), name='stuffwithfinch_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('finches/<int:finch_id>/assoc_stuff/<int:stuff_id>/', views.assoc_stuff, name='assoc_stuff'),
]