from django.urls import path
from . import views

urlpatterns = [
    path('createuser/',views.CreateUser,name='createsuperuser'),
    path('createadmin/',views.CreateAdmin,name='createadmin'),
    path('viewusers/',views.ViewUser,name='viewusers'),
    path('viewadmins/',views.ViewAdmin,name='viewadmins'),
    path('createquiz/',views.CreateQuiz,name='createquiz'),
    path('viewquizes/',views.ViewQuiz,name='viewquizes'),
    path('addquestions/',views.AddQuestions,name='addquestions'),
    path('viewquestions/<str:pk>/',views.ViewQuestions,name='viewquestions'),
    path('viewanswers/<str:pk>/',views.ViewAnswers,name='viewanwers'),
    path('check/<str:id>/<str:pk>/',views.Check,name='check'),
    path('attempt/<str:id>/<str:pk>/',views.UserAttempt,name='attempt'),

]
