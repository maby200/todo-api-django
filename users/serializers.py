from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # read_only_fields = 'created_at', # aunque auto_now_add = True 
                                        # ya hace que sea modo lectura