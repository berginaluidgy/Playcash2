from django.db import models
import datetime
from django.contrib.auth.models import User
    
class Task(models.Model):
    titre = models.CharField(max_length=200)
      # Corrected from charfiled to CharField
    status= models.CharField(max_length=200)
    progression=models.IntegerField()
    idUser= models.CharField(max_length=200)
    recompense=models.IntegerField()
    key= models.CharField(max_length=200,unique=True)
    Type= models.CharField(max_length=200)

    def __str__(self):
        return self.titre


class OwnerTask (models.Model):
    titre = models.CharField(max_length=200)
      # Corrected from charfiled to CharField
    status= models.CharField(max_length=200,default=0)
    progression=models.IntegerField(default=0)
    idUser= models.CharField(max_length=200,default=0)
    recompense=models.IntegerField(default=0)
    date=models.DateField(default=datetime.date.today)  
    NbreParticipant=models.IntegerField()
    NbreAchevement=models.IntegerField()
    Type= models.CharField(max_length=200)
    Key= models.CharField(max_length=200)
    def __str__(self):
        return self.titre
        

class TiktokMission(models.Model):
    titre = models.CharField(max_length=200)
      # Corrected from charfiled to CharField
    status= models.CharField(max_length=200)
    progression=models.IntegerField()
    idUser= models.CharField(max_length=200)
    recompense=models.IntegerField()
    key= models.CharField(max_length=200,unique=True)


# class TiktokEstimation(models.Model):
    



class Video(models.Model):
    dropbox_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    thumbnail_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    userid=models.IntegerField(000)

    def __str__(self):
        return self.name


class Userinfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userinfo")
    userid=models.IntegerField(default=000)
    isvideoMaker=models.BooleanField(default=False)
    videowache=models.IntegerField(default=0)
    videowash=models.IntegerField(default=0)
    Username = models.CharField(max_length=255, unique=True)
    manysubs=models.IntegerField(default=0)
    manyshare=models.IntegerField(default=0)
    ApllyForVideoM=models.BooleanField(default=False)
    manyTask=models.IntegerField(default=0)
    Telephone=models.IntegerField(default=0)
    money=models.IntegerField(default=0)



class MissionVM(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="mission_vm")
    userid = models.IntegerField(default=0)
    is_video_maker = models.BooleanField(default=False)

    # Informations sur la mission
    mission_name = models.CharField(max_length=255)  # Nom de la mission
    description = models.TextField(blank=True, null=True)  # Description de la mission
    total_videos = models.IntegerField(default=0)  # Nombre total de vidéos à monter
    completed_videos = models.IntegerField(default=0)  # Nombre de vidéos complétées par l'utilisateur

    # Statut de la mission
    is_active = models.BooleanField(default=True)  # La mission est-elle en cours ?
    start_date = models.DateTimeField(auto_now_add=True)  # Date de début de la mission
    end_date = models.DateTimeField(null=True, blank=True)  # Date de fin prévue
    completion_date = models.DateTimeField(null=True, blank=True)  # Date de fin réelle de la mission

    # Progression et récompenses
    progress = models.FloatField(default=0.0)  # Progression en pourcentage
    rewardMoney = models.IntegerField(default=0)  # Points ou récompenses pour l'accomplissement de la mission

    def __str__(self):
        return f"{self.user.username} - {self.mission_name}"

    def update_progress(self):
        """
        Met à jour la progression de la mission en fonction des vidéos complétées.
        """
        if self.total_videos > 0:
            self.progress = (self.completed_videos / self.total_videos) * 100
            if self.completed_videos >= self.total_videos:
                self.is_active = False  # Marque la mission comme terminée
                self.completion_date = datetime.timezone.now()
        self.save()




class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=255)
    start_time = models.DateTimeField(auto_now_add=True)
    return_time = models.DateTimeField(null=True, blank=True)
    watched_time = models.FloatField(null=True, blank=True)  # Temps regardé en secondes

    def calculate_watched_time(self):
        if self.start_time and self.return_time:
            self.watched_time = (self.return_time - self.start_time).microseconds
            return self.watched_time
        return None


class YouTubeVideoRead(models.Model):
    video_id = models.CharField(max_length=100, unique=True, verbose_name="ID de la vidéo YouTube")
    video_title = models.CharField(max_length=255, verbose_name="Titre de la vidéo YouTube")
    video_url = models.URLField(max_length=500, verbose_name="Lien de la vidéo YouTube")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilisateur qui a lu la vidéo")
    read_at = models.DateTimeField(auto_now_add=True, verbose_name="Date et heure de lecture")
    time_spent = models.DurationField(verbose_name="Temps passé à lire la vidéo")
    def formatted_time_spent(self):
        total_seconds = int(self.time_spent.total_seconds())
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes} minutes et {seconds} secondes"
    class Meta:
        verbose_name = "Vidéo lue"
        verbose_name_plural = "Vidéos lues"
        ordering = ["-read_at"]

    def __str__(self):
        return f"{self.video_title} - {self.user.username}"


class askPay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilisateur qui a lu la vidéo")
    userid=models.IntegerField()
    date=models.DateField(default= datetime.datetime.now)
    status=models.CharField(default='',max_length=256)
    NumeroT=models.IntegerField(default=0)



class link(models.Model):
    link_url = models.CharField(max_length=255, verbose_name="Titre de la vidéo YouTube")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilisateur qui a lu la vidéo")
    userid=models.IntegerField()
    


class sendPOSTDIGICEL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilisateur qui a lu la vidéo")
    userid=models.IntegerField()
    nbrV=models.IntegerField()
    isacctop=models.BooleanField()
    
    


class askDIDICEL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilisateur qui a lu la vidéo")
    userid=models.IntegerField()
    date=models.DateField(default= datetime.datetime.now)
    status=models.CharField(default='',max_length=256)
    NumeroT=models.IntegerField(default=0)
