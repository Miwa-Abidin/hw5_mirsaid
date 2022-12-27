from django.shortcuts import render
from rest_framework import viewsets
from . models import Lesson, Student, Mentor
from .my_generics import ListMixinApi, CreateMixinApi, RetrieveMixinApi, UpdateMixinApi, DeleteMixinApi, MyApiView
from rest_framework import generics

from . serializers import LessonSerializer, StudentSerializer, MentorSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class StudentCreateListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyApiView(RetrieveMixinApi, DeleteMixinApi, UpdateMixinApi, MyApiView):
    serializer_class = StudentSerializer
    model = Student

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer


class MentorRetrieveUpdateDestroyApiView(ListMixinApi, CreateMixinApi, RetrieveMixinApi, UpdateMixinApi, DeleteMixinApi, viewsets.ViewSetMixin, MyApiView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    model = Mentor
