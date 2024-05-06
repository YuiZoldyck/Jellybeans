from django.urls import path
from .views import indexPageView, addFlavorView, createPageView, updatePageView, submitChanges, deletePageView

urlpatterns = [
    path('', indexPageView, name="index"),
    path('create/', createPageView, name="create"),
    path('edit/<int:sid>', updatePageView , name='edit'),
    path('addflavor/', addFlavorView, name="add"),
    path('submitchanges/<int:sid>', submitChanges, name='submit'),
    path('delete/<int:sid>', deletePageView, name='delete'),

]
