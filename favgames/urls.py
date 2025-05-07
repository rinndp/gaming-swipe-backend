from django.urls import path

from favgames.views import GetPlayedGamesFromUser, DeletePlayedGameView, AddPlayedGameView
from favgames.views.add_favgame import AddFavGameView
from favgames.views.delete_favgame import DeleteFavGameView
from favgames.views.get_favgames_from_user import GetFavGamesFromUser

urlpatterns = [
    path("favgames/add/<str:slug>", AddFavGameView.as_view(), name="add-favgame"),
    path("favgames-played/add/<str:slug>", AddPlayedGameView.as_view(), name="add-favgame-played"),
    path("favgames/delete/<str:slug>/<int:position>", DeleteFavGameView.as_view(), name="delete-favgame"),
    path("favgames-played/delete/<str:slug>/<int:position>", DeletePlayedGameView.as_view(), name="delete-favgame-played"),
    path("favgames/user/<str:slug>", GetFavGamesFromUser.as_view(), name="get-favgames"),
    path("favgames-played/user/<str:slug>", GetPlayedGamesFromUser.as_view(), name="get-favgames-played"),
]