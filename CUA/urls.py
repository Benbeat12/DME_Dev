from django.urls import path
from .views import SigUpView,ProfileListView,UpdateProfileView

urlpatterns = [
    path("Signup/", SigUpView.as_view(), name="signup"),
    path('user/<int:pk>/edit/',UpdateProfileView.as_view(),name='profil_update'),
    path("user/<int:pk>list/",ProfileListView.as_view(),name="profil_list"),
]

