from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Wallet, Borrower
# "id": 3,
# "password": "1234",
# "last_login": null,
# "is_superuser": false,
# "username": "testin2g1",
# "first_name": "",
# "last_name": "",
# "email": "",
# "is_staff": true,
# "is_active": true,
# "date_joined": "2021-02-25T07:50:39.679350Z",
# "groups": [],
# "user_permissions": []
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class WalletSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Wallet
        fields = ['balance', 'user']

class BorrowerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Borrower
        fields = ['user', 'reason', 'description', 'amount_needed']