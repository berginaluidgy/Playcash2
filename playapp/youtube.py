import random
import requests
from django.contrib.auth.models import User
from .models import YouTubeVideoRead,link
def videoLink(userid):

    try:
         # Récupérer l'utilisateur par ID
        user = User.objects.get(id=userid)
    except User.DoesNotExist:
        user = User.objects.get(id=11) 
        # Filtrer les vidéos pour cet utilisateur
    videos = YouTubeVideoRead.objects.filter(user=user)
    videos_list = list(videos)
    vid=[video.video_id for video in videos_list]
    url = "https://yt-api.p.rapidapi.com/channel/videos"
    groupe=['UCY0A59H5CZ7AoD6R1TGpd1w']
    result=[]
    for gr in groupe:
        querystring = {"id":gr}
        headers = {
            "x-rapidapi-key": "34c8d028dfmsh98004f4820b653cp12518cjsne4933e7505d1",
            "x-rapidapi-host": "yt-api.p.rapidapi.com"
        }
        
        response = requests.get(url, headers=headers, params=querystring)
        exp=response.json()
        # subs=exp['subscriberCountText']
        # subsNumber=exp['subscriberCount']
        # vCount=exp['videosCount']
        tableVieos=exp['data']
        print(exp)
        for tb in tableVieos:
            
 
            
            id=tb['videoId']
            isview=False
            if id in vid:
                isview=True


            title=tb['title']

            viewCount=tb['viewCount']
            len=tb['lengthText']
            vCInt=int(viewCount)
            resuSubs={
                'isview':isview,
                "title":title,
                "id":id,
                'videoID':'https://www.youtube.com/watch?v='+id,
                "viewCount":viewCount,
                "endView":100000,
                "len":len,
                "VCInt":vCInt,
                "pricepartial":random.randint(2,13),
                "pricetotal":random.randint(15,25),

            }
            result.append(resuSubs)
        return result 
        



def linkSUb(userid):
    try:
         # Récupérer l'utilisateur par ID
        user = User.objects.get(id=userid)
    except User.DoesNotExist:
        user = User.objects.get(id=11) 
        # Filtrer les vidéos pour cet utilisateur
    linkk = link.objects.filter(user=user)
    link_list = list(linkk)
    lin=[lk.link_url for lk in link_list]
    print(lin,'undeux')
    links = [
        "UCVEukooN7ci__E1Ng2H1eTQ", 'UC8UPeuldn_DH_HZvnpbXNFw', 'UC8eTYhTx-ioM-wNsiL3LRcA',
        'UChPGFU7DUz_4lZrCQWHRmhA', 'UCEZYoCqin-cZpHrZ8D-TB_Q', 'UCToxeYp9hpBRpWVCfwyjZIQ',
        'UCcROxxQG5yMHCaVqabR39Rw', 'UCfbN0N617pM9LtbSscd9HNg', 'UC9kM5GEC9EjOQKNNdnndM9g',
        'UCgdLQ3mHdtITEkn5o0GLUIQ', 'UC1mXBxzuYapBfUSG1Q8vlhQ', 'UCnXVAcbV0LaKyWayrBrlNoA',
        'UCD2zmWkWKVoO9WVV0-mxb3Q', 'UCJ6Vn7kBtyLxztQ7RcDLbKA', 'UCkNAPPtfCofcQJMsFe72YbA'
    ]
    url = "https://yt-api.p.rapidapi.com/channel/about"
    tb = []

    headers = {
        "x-rapidapi-key": "34c8d028dfmsh98004f4820b653cp12518cjsne4933e7505d1",
        "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }

    for idx, lk in enumerate(links):
        print(f"Traitement du lien {idx + 1} : {lk}")

        querystring = {"id": lk}
        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code != 200:
            print(f"Erreur API pour {lk} : {response.status_code}")
            continue

        res = response.json()

        # Extraction avec gestion des clés manquantes
        subscriber_count = res.get('subscriberCount', 0)
        issubs=False
        
        if ("https://www.youtube.com/channel/"+lk+"?sub_confirmation=1") in lin:
            issubs=True
  
        champ = {
            'issubs':issubs,
            'nbrS': subscriber_count,
            'nbrFocus': 100000,
            'subscash': random.randint(5, 10),
            'shareCash': random.randint(9, 20),
            'linked': f"https://www.youtube.com/channel/{lk}?sub_confirmation=1"
        }

        tb.append(champ)

    return tb