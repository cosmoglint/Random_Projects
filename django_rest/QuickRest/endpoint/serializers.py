from django.contrib.auth.models import User, Group
from rest_framework import serializers


<<<<<<< HEAD
class userSerializer(serializers.HyperlinkedModelSerializer):
=======
class UserSerializer(serializers.HyperlinkedModelSerializer):
>>>>>>> e838fc0a0c602b2d7c5f0f40fb6791d499eca891
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
