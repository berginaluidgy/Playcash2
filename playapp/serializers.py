from rest_framework import serializers
from .models import Video, askDIDICEL, askPay

from django.contrib.auth.models import User
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'dropbox_id', 'name', 'description', 'thumbnail_url', 'created_at']


# accounts/serializers.py



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email','id']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


from .models import Userinfo, MissionVM, Video

class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userinfo
        fields = ['userid', 'Username', 'isvideoMaker', 'money', 'manyTask', 'videowache']

class MissionVMSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionVM
        fields = ['mission_name', 'completed_videos', 'progress', 'rewardMoney', 'is_active']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['name', 'description', 'created_at', 'userid']
class AskPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = askPay
        fields = '__all__'



class AskDIDICELSerializer(serializers.ModelSerializer):
    class Meta:
        model = askDIDICEL
        fields = '__all__'