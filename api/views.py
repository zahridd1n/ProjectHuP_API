from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions

from . import serializers
from main import models


@api_view(['get'])
def index(request):
    """home sahifada chiquvchi content"""
    data = models.Home.objects.filter().order_by('-id')[0]
    data_serializer = serializers.HomeSerializer(data)
    return Response(data_serializer.data)


class PortfolioList(generics.ListAPIView):
    """portfolio sahifada chiquvchi content"""
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer


class TeamList(generics.ListAPIView):
    """our team list ko'rinishida  chiquvchi content"""
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer


@api_view(['post'])
def message_create(request):
    name = request.data.get('name')
    phone = request.data.get('phone')
    content = request.data.get('content')
    if name and phone and content:
        models.Message.objects.create(name=name, phone=phone, content=content)
        return Response('messeg muvafaqiyatli yaratildi', status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class VacancyList(generics.ListAPIView):
    """vacansyalarni list qib chiqaruvchi sahifa"""
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancyListSerializer


class VacancyDetail(generics.RetrieveAPIView):
    """vacansyani detail qib chiqaruvchi sahifa"""
    queryset = models.Vacancy.objects.all()
    serializer_class = serializers.VacancyDetailSerializer


@api_view(['post'])
def vacancy_resume(request):
    full_name = request.data.get('full_name')
    phone = request.data.get('phone')
    cv = request.data.get('cv')
    if full_name and phone and cv:
        models.Resume.objects.create(full_name=full_name, phone=phone, cv=cv)
        return Response('Resume muvafaqiyatli yaratildi', status=status.HTTP_201_CREATED)
    return Response('Resume yaratilmadi qaytadan urinib ko\'ring', status=status.HTTP_400_BAD_REQUEST)
