from django.contrib.auth import get_user_model
from rest_framework import serializers

from dj_rest_auth.serializers import UserDetailsSerializer

CustomUser = get_user_model()

class CustomUserDetailSerializer(UserDetailsSerializer):
    """
    CustomUserDetailSerializer
    """
    # location = serializers.StringRelatedField()
    avatar = serializers.ImageField(max_length=None, allow_empty_file=False)
    class Meta:
        model = CustomUser
        fields = ['pk', 
                'username', 
                'email', 
                'first_name', 
                'last_name', 
                'bio', 
                'date_of_birth', 
                'location',
                'website', 
                'avatar',
        ]
        read_only_fields = ('username', )



