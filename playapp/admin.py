from django.contrib import admin
from .models import link,Task,OwnerTask,Video,Userinfo,MissionVM,UserInteraction,YouTubeVideoRead,askPay,sendPOSTDIGICEL





# Register your models here.
admin.site.register(Task)
admin.site.register(OwnerTask)
admin.site.register(Video)
admin.site.register(Userinfo)
admin.site.register(MissionVM)
admin.site.register(UserInteraction)
admin.site.register(YouTubeVideoRead)
admin.site.register(askPay)

admin.site.register(link)
admin.site.register(sendPOSTDIGICEL)