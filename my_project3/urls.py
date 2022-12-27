
from django.contrib import admin
from django.urls import path
from courses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/student/', views.StudentCreateListView.as_view()),
    path('api/student/<int:pk>/', views.StudentRetrieveUpdateDestroyApiView.as_view()),
    path('api/lesson/', views.LessonViewSet.as_view({'post': 'create', 'get': 'list'})),
    path('api/mentor/', views.MentorViewSet.as_view({'post': 'create', 'get': 'list'})),
    path('api/lesson/<int:pk>/', views.LessonViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    })),
    path('api/mentor/<int:pk>/', views.MentorRetrieveUpdateDestroyApiView.as_view({
        "get": "retrieve",
        "put": "update",
        "delete": "destroy"
    })),
]
