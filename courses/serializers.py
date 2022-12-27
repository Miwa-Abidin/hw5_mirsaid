from rest_framework import serializers

from .models import Lesson, Student, Mentor

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

class StudentSerializer(serializers.Serializer):
    stud_name = serializers.CharField(max_length=30)
    date_birth = serializers.CharField(max_length=30)

    def save(self, **kwargs):
        print('Creating new student')
        return super().save(**kwargs)

    def create(self, validated_data):
        message = Student.objects.create(**validated_data)
        return message

    def update(self, instance, validated_data):
        instance.save(**validated_data)

        return instance

class MentorSerializer(serializers.Serializer):
    ment_name = serializers.CharField(max_length=30)
    experiense = serializers.CharField(max_length=30)

    def save(self, **kwargs):
        print('Creating new mentor')
        return super().save(**kwargs)

    def create(self, validated_data):
        message = Mentor.objects.create(**validated_data)
        return message

    def update(self, instance, validated_data):
        instance.save(**validated_data)

        return instance



