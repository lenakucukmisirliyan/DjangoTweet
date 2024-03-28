from django.urls import path
from . import views

app_name = 'tweetapp'   #reverse yapabilmek için

urlpatterns = [
    path('', views.listtweet, name='listtweet'),        # www.blabla.com/tweetapp/
    path('addtweet/', views.addtweet, name='addtweet'), # www.blabla.com/tweetapp/addtweet/
    path('addtweetbyform', views.addtweetbyform, name="addtweetbyform"),
    path('addtweetbymodelform', views.addtweetbymodelform, name="addtweetbymodelform"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('deletetweet/<int:id>', views.deletetweet, name='deletetweet'),
]
