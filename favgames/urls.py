from django.urls import path
from favgames.views.add_favgame import AddFavGameView
from favgames.views.delete_favgame import DeleteFavGameView
from favgames.views.get_favgames_from_user import GetFavGamesFromUser

urlpatterns = [
    path("favgames/add/<str:slug>", AddFavGameView.as_view(), name="add_favgame"),
    path("favgames/delete/<str:slug>/<int:position>", DeleteFavGameView.as_view(), name="delete_favgame"),
    path("favgames/user/<str:slug>", GetFavGamesFromUser.as_view(), name="get_favgames"),
]