from django.urls import path
from movies import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("movies", views.MovieModelViewSet, basename="Movies")
urlpatterns = [path('accounts/token', obtain_auth_token),
               path("user/signup", views.UserCreation.as_view()),
               path("user/signin", views.SigninView.as_view()),


               ] + router.urls
