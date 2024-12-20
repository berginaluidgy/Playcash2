
from django.urls import path
from .views import AskDIDICELView, UserInteractionView, Views,linky,Tasklink,sendinfoTiktok,list_videos,RegisterView,ModelsUserafterToken,resendAllInfo,pullMoney
from .views import add_point,UserPointsListView,defineLINK,SHAREYUTUBECHANNEL,SHAREYUTUBEVIDEO, chooseMissionOne, admin_statistics, AddYouTubeChannel,issuccesViewYoutubevideo,requestMoneysend,DIGICELGET
from . import views
urlpatterns = [
    path('Views',Views),
     path('linky',linky),
      path('LinkTask',Tasklink),
        path('tiktokInfo',sendinfoTiktok),
 path('videos/', views.list_videos, name='list_videos'),
    path('videos/upload/', views.upload_video, name='upload_video'),
    path('videos/delete/<int:pk>/', views.delete_video, name='delete_video'),
        path('listVideos',views.list_videos),
      path('api/auth/register/', RegisterView.as_view(), name='register'),
       path('api/auth/freedom',ModelsUserafterToken , name='recupeInfo'),
         path('ACCESS/<int:keyGo>',resendAllInfo,name='ACCESS'),
    path('pullMoney/<int:Key>',pullMoney,name='Pull'),
        path('api/Mission',chooseMissionOne,name='PullMission'),
         path('admins/statistics/', admin_statistics, name='admin_statistics'),
    path('admins/add-youtube/', AddYouTubeChannel, name='add_youtube'),
 path('user-interaction/', UserInteractionView.as_view(), name='user-interaction'),
path('checkAndacceptVIEWS/', issuccesViewYoutubevideo, name='apiviewSTOP'),
path('YOUTUBE/MySharing--Link/reward/<int:keyUser>/<str:idvideo>', SHAREYUTUBEVIDEO, name='apiviewSTOP'),
path('YOUTUBE/MySharing--LinkCHANNEL/reward/<int:keyUser>/<str:idChannel>', SHAREYUTUBECHANNEL, name='apiviewSTOP'),

path('RequestMoney',requestMoneysend),
path('defineLINK/',defineLINK),
path('digicelget/',DIGICELGET),
  path('ask-didicel/', AskDIDICELView.as_view(), name='ask_didicel'),
    path('ask-didicel/<int:user_id>/', AskDIDICELView.as_view(), name='check_didicel'),

  path('api/user-points/', UserPointsListView.as_view(), name='user-points'),
 path('api/add-points/', add_point, name='add-points'),

]
