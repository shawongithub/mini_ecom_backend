from rest_framework import serializers
from django.contrib.auth.models import User


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['username','password']

    def save(self):
        account=User(
            username=self.validated_data['username']
        )
        password=self.validated_data['password']
        account.set_password(password)
        account.save()