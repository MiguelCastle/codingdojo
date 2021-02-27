from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Borrower
from .serializers import UserSerializer, WalletSerializer, BorrowerSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from rest_framework.parsers import JSONParser


class UserViewSet(viewsets.ViewSet):

    queryset = User.objects

    def create(self, request):
        data = JSONParser().parse(request)
        print(data)
        # we need to check to see what kind of user we have
        g = data.pop("group")
        if g == 'lender':
            print('creating lender')
            serializer_class = UserSerializer(data=data)
            lender_group = Group.objects.get(name='lender')
            if serializer_class.is_valid():
                u = serializer_class.save()
                # print(u) this returns the username value
                # adding user to the client group RIGHT NOW AT LEAST
                lender_group.user_set.add(u)
                b = data.pop("balance")
                walletSerializer = WalletSerializer(data={'balance': b, 'user': u})
                if walletSerializer.is_valid():
                    walletSerializer.create(validated_data=walletSerializer.initial_data)
                return HttpResponse('lender created')
        # print(serializer_class.initial_data)
        elif g == 'borrower':
            print('printing borrower')
            serializer_class = UserSerializer(data=data)
            borrower_group = Group.objects.get(name='borrower')
            if serializer_class.is_valid():
                u = serializer_class.save()
                borrower_group.user_set.add(u)
                r = data.pop("reason")
                d = data.pop("description")
                a = data.pop("amount_needed")
                borrowerSerializer = BorrowerSerializer(data={'user': u, 'reason': r, 'description': d, 'amount_needed': a})
                if borrowerSerializer.is_valid():
                    borrowerSerializer.create(validated_data=borrowerSerializer.initial_data)
                    walletSerializer = WalletSerializer(data={'balance': 0, 'user': u})
                    if walletSerializer.is_valid():
                        walletSerializer.create(validated_data=walletSerializer.initial_data)
                return HttpResponse('borrower created')

        return JsonResponse(serializer_class.errors, status=400)
    
    def get(self, request, id=None):
        # print(id)
        # print(User.objects.all())
        # for user in User.objects.all():
        #     print(user)
        print(User.objects.get(username=str(id)))
        return HttpResponse('Got users ' + str(id))

class BorrowerViewSet(viewsets.ViewSet):

    def list(self, request, id):
        print(request.query_params)
        print( Borrower.objects.all())
        # id = self.kwargs['id']
        print('looking  for - ' + id)
        # queryset = Borrower.objects.get(pk=id)
       # print(queryset)
        serializer_class = BorrowerSerializer(queryset, many=True)
        return HttpResponse(serializer_class.data)

