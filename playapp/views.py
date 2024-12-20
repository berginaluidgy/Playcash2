
from .youtube import videoLink,linkSUb
from .tiktok import sendinfoTiktok
from rest_framework import generics, status
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view,throttle_classes
from rest_framework.response import Response
from .models import askPay, OwnerTask ,Userinfo,Task,Video,MissionVM,YouTubeVideoRead
import dropbox
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from .models import Video
from django.http import JsonResponse
from dropbox import Dropbox
from rest_framework.decorators import api_view
import os
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.throttling import SimpleRateThrottle
from .serializers import UserSerializer,AskPaySerializer

from .models import UserInteraction
from django.utils.timezone import now
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data['username'])
            user=serializer.save()
            Userinfobis=Userinfo.objects.create(user=user,userid=user.id,Username=serializer.validated_data['username'])
            Userinfobis.save()
            UserVM=MissionVM.objects.create(user=user,userid=user.id)
            UserVM.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ModelsUserafterToken(request):
    user = User.objects.get(id=4)  # Remplacez 1 par l'ID que vous voulez rechercher
    print(user.username, user.email)
    print()
    return Response({'free':{
        'email': user.email,
        'Username':user.username
    }})


DROPBOX_ACCESS_TOKEN = os.getenv("DROPBOX_ACCESS_TOKEN")

@api_view(['GET'])
def Views(request):
    rt=videoLink()
    return Response(rt)

# @api_view(['GET'])
# def ShareLink(request):
#     rt=videoLink()
#     return Response(rt)




@api_view(['GET'])
def linky(request):
    rt=linkSUb()
    return Response(rt)


@api_view(['GET'])
def Tasklink(request):
    OwnersModels=OwnerTask.objects.all()
    all=[]
    for task in OwnersModels:  
       taskD={
           "titre":task.titre,
           "progress":task.progression,
           "recompense":task.recompense
       }
       all.append(taskD)
       print(task.titre)

    
    return Response({"Task":all})   


@api_view(['GET'])
def tiktokInfo(request):
    sendInfo=sendinfoTiktok(name='taylorswift')
    return Response({"info":sendInfo})   


def refresh_access_token():
        
        APP_KEY = 'm6yit15q69uy2vf'
        APP_SECRET = 'ted12iwqcprmdud'
        REFRESH_TOKEN = 'tcxWZ-dUkcIAAAAAAAAAAQt_EwvI-rtXfbnCk_pwTHaTirzw2TuD_1fRegZGE02y'
        try:
                
                dbx2 = dropbox.Dropbox(
                app_key=APP_KEY,
                app_secret=APP_SECRET,
                oauth2_refresh_token=REFRESH_TOKEN
            )
        
        # La bibliothèque gère automatiquement le rafraîchissement du token
        # Vous pouvez vérifier que ça fonctionne en appelant une méthode de l'API
                dbx2.users_get_current_account()

                print(dbx2)
                print("Nouveau access token obtenu avec succès")
                return dbx2
        except Exception as e:
                print(f"Erreur lors du rafraîchissement du token : {e}")
                return None

dbx = refresh_access_token()

@api_view(['POST'])
def upload_video(request):
    file = request.FILES.get('video')
    name = request.data.get('name')
    id = request.data.get('userId')
    description = request.data.get('description')
    thumbnail_url = request.data.get('thumbnail_url')

    if not file:
        return Response({'error': 'No video file provided'}, status=status.HTTP_400_BAD_REQUEST)

    # Upload the file to Dropbox
    dropbox_path = f"/videos/{file.name}"
    try:
        dbx.files_upload(file.read(), dropbox_path, mute=True)
        link = dbx.sharing_create_shared_link_with_settings(dropbox_path).url
    except dropbox.exceptions.ApiError as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Create video entry in the database
    video = Video.objects.create(
        dropbox_id=dropbox_path,
        name=name,
        description=description,
        thumbnail_url=thumbnail_url,
        userid=id,
    )

    video_data = {
        "id": video.id,
        "dropbox_id": video.dropbox_id,
        "name": video.name,
        "description": video.description,
        "thumbnail_url": video.thumbnail_url,
        "created_at": video.created_at
    }

    return Response(video_data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def list_videos(request):
    videos = Video.objects.all()
    videos_data = [
        {
            "id": video.id,
            "dropbox_id": video.dropbox_id,
            "name": video.name,
            "description": video.description,
            "thumbnail_url": video.thumbnail_url,
            "created_at": video.created_at
        }
        for video in videos
    ]
    return Response(videos_data)

@api_view(['DELETE'])
def delete_video(request, pk):
    try:
        video = Video.objects.get(pk=pk)
        dbx.files_delete(video.dropbox_id)  # Supprime la vidéo de Dropbox
        video.delete()  # Supprime la vidéo de la base de données
        return Response({"message": "Video deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Video.DoesNotExist:
        return Response({'error': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)
    except dropbox.exceptions.ApiError as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['get'])
def resendAllInfo(request,keyGo):
   UserSell=Userinfo.objects.get(userid=keyGo)
   # TaskSell=Task.objects.get(idUser=keyGo)
   VideoSell=MissionVM.objects.get(user_id=keyGo)
   recapUserInfo={
       'Info': UserSell.isvideoMaker,
       'video_watch': UserSell.videowache,
       'CountSubs': UserSell.manysubs,
       'countshare': UserSell.manyshare,
       'ApllyForVideoM': UserSell.ApllyForVideoM,
        'countTask': UserSell.manyTask,
        'Telephone': UserSell.Telephone,
        'isvideoMaker': VideoSell.is_video_maker,
        'username':UserSell.Username,
        'Money':UserSell.money,
        
   }
   show=askPay.objects.filter(userid=keyGo)
    # print(show)
   seria=AskPaySerializer(show,many=True)
            # for inst in show:
   bigcont=[]
   for dt in seria.data:
      bigcont.append(dt)                        
      print(UserSell)

   # recapTask={
   #     'Task':TaskSell.titre,
   #     'status':TaskSell.status,
   #     'progression':TaskSell.progression,
   #     'recompense':TaskSell.recompense,
   #     'Type':TaskSell.Type,
   # }
   link={
       'ShareLink':str(request.get_host())+"/YOUTUBE/MySharing--Link/reward/"+str(keyGo)
   }

   return JsonResponse({'data':{'firstdegree':recapUserInfo,
                                # 'seconddegree':recapTask,
                                'third':link,
                                'all':bigcont,}})






@api_view(['post'])
def pullMoney(request,Key):

    NewMoney=request['NewMoney']
    if NewMoney >=1:
        data=Userinfo.objects.get(userid=Key)
        data.money=NewMoney
        data.save()
    else:
        return JsonResponse({'none':None})


    #update

@api_view(['get'])
def showMission(request,Key):
  
   data = [
    {
        "mission_name": "Monteur Novice",
        "description": "Réalisez 60 vidéos simples pour gagner 25 000 gourdes.",
        "total_videos": 60,
        "cash_reward": 25000,  # HTG
        "difficulty": "Facile"
    },
    {
        "mission_name": "Monteur Confirmé",
        "description": "Réalisez 85 vidéos intermédiaires avec des transitions basiques.",
        "total_videos": 85,
        "cash_reward": 35417,  # 85 * 416.67 HTG
        "difficulty": "Intermédiaire"
    },
    {
        "mission_name": "Monteur Avancé",
        "description": "Accomplissez 110 montages vidéo avec des effets avancés.",
        "total_videos": 110,
        "cash_reward": 45833,  # 110 * 416.67 HTG
        "difficulty": "Difficile"
    },
    {
        "mission_name": "Expert en Montage",
        "description": "Montez 135 vidéos complexes incluant des effets spéciaux.",
        "total_videos": 135,
        "cash_reward": 56250,  # 135 * 416.67 HTG
        "difficulty": "Expert"
    },
    {
        "mission_name": "Maître du Montage",
        "description": "Réalisez 160 montages professionnels pour atteindre le sommet.",
        "total_videos": 160,
        "cash_reward": 66667,  # 160 * 416.67 HTG
        "difficulty": "Maître"
    }]
   return JsonResponse({'none':None})


# @api_view(['POST '])
# def chooseMissionOne(request):
   
 
#    userid=request['userid']
#    is_video_maker=request['is_video_maker']
#    mission_name=request['mission_name']
#    description=request['description']
#    rewardMoney=request['rewardMoney']
#    missionModel=MissionVM.objects.create(rewardMoney=rewardMoney,description=description,userid=userid,is_video_maker=is_video_maker,mission_name=mission_name)
   


#    return JsonResponse({'none':None})




@api_view(['POST'])
def chooseMissionOne(request):
    print(request.data, request.data.get('userid',1),
         request.data.get('is_video_maker',True),
        request.data.get('mission_name','ii'),
        request.data.get('description','ii'),
         request.data.get('rewardMoney',1000),
        request.data.get('total_videos',80)
       )
    try:
        # Récupération des données du POST
        userid = request.data.get('userid')
        is_video_maker = request.data.get('is_video_maker')
        mission_name = request.data.get('mission_name')
        description = request.data.get('description')
        rewardMoney = request.data.get('rewardMoney')
        total_videos=request.data.get('total_videos')
        # Vérification si l'utilisateur existe déjà dans la base de données
        existing_mission = MissionVM.objects.filter(userid=userid, is_active=True).first()
        if existing_mission:
            return JsonResponse({
                'error': 'Une mission est déjà en cours pour cet utilisateur.',
                'current_mission': {
                    'mission_name': existing_mission.mission_name,
                    'description': existing_mission.description,
                    'rewardMoney': existing_mission.rewardMoney
                }
            }, status=400)
        
        # Création de la nouvelle mission
        user = User.objects.get(id=userid)
        print(user)
        missionModel = MissionVM.objects.create(
            user=user,
            userid=userid,
            is_video_maker=is_video_maker,
            mission_name=mission_name,
            description=description,
            rewardMoney=rewardMoney,
            total_videos=total_videos
        )
        
        # Réponse avec les détails de la mission créée
        return JsonResponse({
            'success': True,
            'message': 'Mission créée avec succès.',
            'mission': {
                'mission_name': missionModel.mission_name,
                'description': missionModel.description,
                'rewardMoney': missionModel.rewardMoney,
                'userid': missionModel.userid
            }
        }, status=201)
    
    except Exception as e:
        # Gestion des erreurs générales
        return JsonResponse({'error': str(e)}, status=500)




@api_view(['GET'])
def admin_statistics(request):
    # Nombre total d'utilisateurs
    total_users = Userinfo.objects.count()

    # Utilisateurs actifs
    active_users = Userinfo.objects.filter(manyTask__gt=0).count()

    # Vidéo Makers
    video_makers = Userinfo.objects.filter(isvideoMaker=True)
    video_makers_count = video_makers.count()

    # Utilisateurs ayant atteint 5000 gourdes
    users_5000_gourdes = Userinfo.objects.filter(money__gte=5000).count()

    # Nombre total de vidéos et leurs détails
    videos = Video.objects.all()
    total_videos = videos.count()
    video_details = [{"id": video.id, "title": video.name, "length": len(video.description), "author": video.userid} for video in videos]

    # Missions complétées
    completed_missions = MissionVM.objects.filter(is_active=False)
    completed_missions_count = completed_missions.count()
    most_missions_user = completed_missions.values("user__username").annotate(mission_count=Count("id")).order_by("-mission_count").first()

    return Response({
        "total_users": total_users,
        "active_users": active_users,
        "video_makers_count": video_makers_count,
        "users_5000_gourdes": users_5000_gourdes,
        "total_videos": total_videos,
        "video_details": video_details,
        "completed_missions_count": completed_missions_count,
        "most_missions_user": most_missions_user,
    })





class UserInteractionView(APIView):
    
    def post(self, request):
        action = request.data.get('action')
        video_id = request.data.get('video_id')
        userid = request.data.get('userid')
        user = User.objects.get(id=userid)
        
        if action == 'start':
            # Enregistre le temps de départ
            interaction = UserInteraction.objects.create(user=user, video_id=video_id)
            return Response({"message": "Start time recorded", "interaction_id": interaction.id})

        elif action == 'return':
            # Met à jour le temps de retour
            interaction_id = request.data.get('interaction_id')
            try:
                interaction = UserInteraction.objects.get(id=interaction_id, user=user)
                interaction.return_time = now()
                print(now(),interaction.return_time)
                watched_time = interaction.calculate_watched_time()

                interaction.save()
                print(watched_time/60)

                if (watched_time/60) < 3:  # Moins de 3 minutes
                    return Response({
                        "status": "failed",
                        "message": "Vous avez regardé moins que le temps demandé."
                    })
                return Response({
                    "status": "success",
                    "message": "Félicitations ! Vous avez regardé assez longtemps."
                })
            except UserInteraction.DoesNotExist:
                return Response({"error": "Interaction introuvable"}, status=404)
        else:
            return Response({"error": "Action non valide"}, status=400)




# class CustomThrottle(SimpleRateThrottle):
#     scope = 'anon'  # Doit correspondre au nom défini dans DEFAULT_THROTTLE_RATES
    
#     def get_cache_key(self, request, view):
#         # Utilisez l'adresse IP ou un autre identifiant unique
#         if request.user.is_authenticated:
#             return f"throttle_{self.scope}_{request.user.id}"
#         return f"throttle_{self.scope}_{self.get_ident(request)}"




@api_view(['POST'])
# @throttle_classes([CustomThrottle])
def issuccesViewYoutubevideo(request):
    from datetime import timedelta
    iduser=request.data.get('Userid')
    dataMoney=request.data.get('dataMny')
    idVideo=request.data.get('idVideo')
    videoT=request.data.get('video_title')
    videoURL=request.data.get('video_url')
    timeSPEND=request.data.get('TImeSpend')

    user = User.objects.get(id=iduser)  # Remplace par un utilisateur existant
    userinfos=Userinfo.objects.get(userid=iduser)
    yutubereach=YouTubeVideoRead.objects.filter(user=user)
    tabview=[]
    for view in yutubereach:
        idv=view.video_id
        tabview.append(idv)


    if any(idVideo==item for item in tabview):
        print('hi')
        return Response({'message': 'deja lue'})



    userinfos.money+=dataMoney
    userinfos.save()
    video = YouTubeVideoRead.objects.create(
        video_id=idVideo,
        video_title=videoT,
        video_url=videoURL,
        user=user,
        time_spent=timedelta(minutes=timeSPEND))
    print('succes',iduser,dataMoney,idVideo,videoT,videoURL,timeSPEND)

    return Response({'message': 'Success!'})




@api_view(['GET'])

def SHAREYUTUBEVIDEO(request,keyUser,idvideo):
    from django.http import HttpResponseRedirect, Http404
    try:
        user = Userinfo.objects.get(userid=keyUser)
        user.money+=20
        user.save()
        
        
    except User.DoesNotExist:
        # Si l'utilisateur n'existe pas, lever une erreur 404
        raise Http404("Utilisateur introuvable")

    return  HttpResponseRedirect(("https://www.youtube.com/watch?v="+idvideo))


@api_view(['GET'])

def SHAREYUTUBECHANNEL(request,keyUser,idChannel):
    from django.http import HttpResponseRedirect, Http404
    try:
        user = Userinfo.objects.get(userid=keyUser)
        user.money+=20
        user.save()
        
        
    except User.DoesNotExist:
        # Si l'utilisateur n'existe pas, lever une erreur 404
        raise Http404("Utilisateur introuvable")

    return  HttpResponseRedirect(("https://www.youtube.com/channel/"+idChannel+"?sub_confirmation=1"))




@api_view(['POST'])
# @throttle_classes([CustomThrottle])
def requestMoneysend(request):
    iduser=request.data.get('Userid')
    numero=request.data.get('phone')
    # dataMoney=request.data.get('dataMny')
    try:
        useraccount=Userinfo.objects.get(userid=iduser)
        realMoney=useraccount.money

        if realMoney>5000:
            
            user = User.objects.get(id=iduser) 
             # Remplace par un utilisateur existant
            useraccount.money = 0  # Mettez à jour le champ `money`
            useraccount.save()
            askPay.objects.create(user=user,userid=iduser,status='succes',NumeroT=numero)
            
            return Response({'status': 'Success!',
                             
                            'message':'Votre virement est en chemin' })
        else:
            # askPay.objects.create(user=user,userid=iduser,status='echec')
         
            return Response({'status': 'echec',
                            'message':'montant inferieur au seuil de paiment' })

    except Exception as e:
        return  Response({'status': 'echec!',
                            'message':{e} })



@api_view(['POST'])
def AddYouTubeChannel(request):
    print(request.data)
    # Récupérer le lien YouTube depuis les données POST
    link = request.data.get("youtube_link")
    print(link)
    if not link:
        return Response({"error": "Lien manquant"}, status=status.HTTP_400_BAD_REQUEST)

    # Expression régulière pour extraire l'ID de la chaîne
    else:
        match = re.search(r"(?:channel\/|user\/|\/c\/|\/)([a-zA-Z0-9_-]+)", link)

        return Response({"error": "ID de chaîne introuvable dans le lien fourni"}, status=status.HTTP_400_BAD_REQUEST)
 



from .models import link
@api_view(['POST'])
def defineLINK(request):
    # Récupération des données envoyées par le frontend
    link_url = request.data.get('link_url')
    userid = request.data.get('userid')
    money = request.data.get('money')

    # Vérification des données reçues
    if not link_url or not userid:
        return Response({'error': 'Lien ou ID utilisateur manquant.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Vérification que l'utilisateur existe
        user = User.objects.get(id=userid)

        # Vérification si l'utilisateur a déjà visité cette URL
        if link.objects.filter(user=user, link_url=link_url).exists():
            return Response({'message': 'Déjà visité'}, status=status.HTTP_200_OK)

        # Enregistrement du lien
        new_link = link.objects.create(link_url=link_url, user=user, userid=userid)
        new_link.save()
        userinfos=Userinfo.objects.get(userid=userid)
    
        userinfos.money+=money
        userinfos.save()
        return Response({'message': 'Succès'}, status=status.HTTP_201_CREATED)

    except User.DoesNotExist:
        return Response({'error': 'Utilisateur introuvable.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': f'Erreur serveur : {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





@api_view(['POST'])
def DIGICELGET(request):
     varis=request.data.get('isacctop')
     if varis ==True:
         return Response({'status':True})
     else:
         return Response({'status':False})




from .models import askDIDICEL, YouTubeVideoRead
from .serializers import AskDIDICELSerializer

class AskDIDICELView(APIView):
    def post(self, request):
        serializer = AskDIDICELSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Demande ajoutée avec succès"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, user_id):
        # Vérifier la date de la dernière demande pour cet utilisateur
        user_requests = askDIDICEL.objects.filter(userid=user_id)
        if user_requests.exists():
            last_request_date = user_requests.latest('date').date
        else:
            last_request_date = None

        # Compter le nombre de vidéos regardées par l'utilisateur
        video_count = YouTubeVideoRead.objects.filter(user__id=user_id).count()

        if video_count > 60:
            result = True
        else:
            result = False

        return Response({
            "last_request_date": last_request_date,
            "video_count": video_count,
            "can_request": result
        }, status=status.HTTP_200_OK)



@api_view(['get'])
def DIGICELGET(request):
     varis=request.data.get('isacctop')
     if varis ==True:
         return Response({'status':True})
     else:
         return Response({'status':False})





from rest_framework.generics import ListAPIView
from .models import UserPoints
from .serializers import UserPointsSerializer

class UserPointsListView(ListAPIView):
    """
    Retourne la liste des utilisateurs triés par points (du plus élevé au plus bas).
    """
    queryset = UserPoints.objects.all().order_by('-points')  # Tri décroissant
    serializer_class = UserPointsSerializer



REWARD_AMOUNT = 1000  # En gourdes
from datetime import datetime, timedelta
from django.utils import timezone 
@api_view(['POST'])
def add_point(request):
    """
    Endpoint qui ajoute un point à un utilisateur.
    Si c'est dimanche, il remet les points à zéro et retourne les 5 gagnants.
    """
    try:
        # Obtenir l'utilisateur depuis la requête
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({"error": "user_id est requis."}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.get(id=user_id)
        user_points, created = UserPoints.objects.get_or_create(user=user)

        # Ajouter un point à l'utilisateur
        user_points.points += 1
        user_points.save()

        # Vérifier si c'est dimanche
        now = timezone.now()
        if now.weekday() == 6:  # Dimanche = 6 dans datetime.weekday()
            # Obtenir les 5 meilleurs utilisateurs
            top_users = UserPoints.objects.order_by("-points")[:5]
            winners = []
            for rank, winner in enumerate(top_users, start=1):
                winners.append({
                    "rank": rank,
                    "username": winner.user.username,
                    "points": winner.points,
                    "reward": REWARD_AMOUNT
                })
            
            # Réinitialiser les points pour tous les utilisateurs
            UserPoints.objects.all().update(points=0, updated_at=now)

            return Response({
                "message": "C'est dimanche! Les points ont été remis à zéro.",
                "winners": winners
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "1 point ajouté avec succès!",
            "user": user.username,
            "total_points": user_points.points
        }, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({"error": "Utilisateur non trouvé."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)