from django.urls  import path
from .views import UserCreationView, LogoutView
urlpatterns = [
    path('', UserCreationView.as_view(), name='sign-up'),
    path('log-out', LogoutView.as_view(), name='log-out'),

]