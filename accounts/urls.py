from django.urls import path
from .views import SignUpView, update_name

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('update_name/', update_name, name='update_name'),
]
