from django.urls import path
from .views import Principal, BloggerViews, login_view, register_view
urlpatterns = [
    path("", login_view, name="login"),
    path("blogger/", BloggerViews, name="Blogger"),
    path("registro/", register_view, name="registro"),
]
