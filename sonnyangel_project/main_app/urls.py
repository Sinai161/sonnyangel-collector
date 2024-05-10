from django.urls import path
from . import views
from django.conf import settings
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path("sonnyangel", views.sonnyangel_index, name="index"),
    path('sonnyangel/<int:sonnyangel_id>/', views.sonnyangel_detail, name='detail'),
    path('sonnyangel/create/', views.SonnyangelCreate.as_view(), name='sonnyangel_create'),
    path('sonnyangel/<int:pk>/update/', views.SonnyangelUpdate.as_view(), name='sonnyangel_update'),
    path('sonnyangel/<int:pk>/delete/', views.SonnyangelDelete.as_view(), name='sonnyangel_delete'),
    path('sonnyangel/<int:pk>/add_sonnyangel_feeding/', views.add_sonnyangel_feeding, name='add_sonnyangel_feeding'),
    path('sonnyangel/<int:pk>/assoc_accessories/<int:accessories_pk>/', views.assoc_accessories, name='assoc_accessories'),
    ## Accessories URLS ##
    path('accessories/', views.AccessoriesList.as_view(), name='accessories_index'),
    path('accessories/<int:pk>/',views.AccessoriesDetail.as_view(), name='accessories_detail'),
    path('accessories/create/', views.AccessoriesCreate.as_view(), name='accessories_create'),
    path('accessories/<int:pk>/update/', views.AccessoriesUpdate.as_view(), name='accessories_update'),
    path('accessories/<int:pk>/delete/', views.AccessoriesDelete.as_view(), name='accessories_delete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
