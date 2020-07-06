from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import status
import time
from django.http import JsonResponse

# Create your views here.

@api_view(['POST'])
def CreateAdmin(request):
	adminserializer = AdminSerializer(data=request.data) 
	if adminserializer.is_valid():
		adminserializer.save()
		return Response(status=status.HTTP_200_OK)
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def CreateUser(request):
	userserializer = UserSerializer(data=request.data) 
	if userserializer.is_valid():
		userserializer.save()
		return Response(status=status.HTTP_200_OK)
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def CreateQuiz(request):
	quizserializer = QuizSerializer(data=request.data)
	if quizserializer.is_valid():
		quizserializer.save()
		return Response(status=status.HTTP_200_OK)
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def AddQuestions(request):
	serializer =QuestionSerializer(data=request.data)
	
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data,status=status.HTTP_200_OK)
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def Check(request,id,pk):
	user_id= User.objects.get(id=id)
	ques_id=Question.objects.get(id=pk)
	exist=Attempt.objects.filter(user=user_id,qid=ques_id)
	msg={'user':str(user_id),'quesid':str(ques_id)}
	current=time.strftime(r"%Y-%m-%d %H:00:00+00:00", time.localtime()) 
	if not exist:
		return Response(msg,status=HTTP_200_OK)
	else:
		return Response(status=HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def UserAttempt(request,id,pk):
	user_id= User.objects.get(id=id)
	ques_id=Question.objects.get(id=pk)
	status=ques_id.quiz_id.status
	print('status='+str(status))
	current=time.strftime(r"%Y-%m-%d %H:00:00+00:00", time.localtime())
	if str(status)==str(current):

		serializer =AttemptSerializer(data=request.data)
		if serializer.is_valid():
			
			serializer.save()
			return Response(serializer.data,status=HTTP_200_OK)
		else:
			return Response(status=HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def ViewQuestions(request,pk):
	questions =Question.objects.filter(quiz_id=pk)
	serializer = QuestionSerializer(questions, many=True)
	
	return Response(serializer.data,status=HTTP_200_OK)

@api_view(['GET'])
def ViewAnswers(request,pk):
	answers =Question.objects.filter(quiz_id=pk)
	serializer =AnswerSerializer(answers, many=True)
	
	return Response(serializer.data,status=HTTP_200_OK)

@api_view(['GET'])
def ViewUser(request):
	users =User.objects.all()
	serializer =UserSerializer(users, many=True)
	return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def ViewAdmin(request):
	admins =Admin.objects.all()
	serializer = AdminSerializer(admins, many=True)
	return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def ViewQuiz(request):
	quizes =Quiz.objects.all()
	current=time.strftime(r"%Y-%m-%d %H:00:00+00:00", time.localtime()) 
	print(current)
	for quiz in quizes:
		if str(quiz.status)==str(current):
			quiz.status="Live"
			print(quiz.status)
		elif str(quiz.status)>str(current):
			quiz.status="Upcoming"
			print(quiz.status)
		else:
			quiz.status="Past"
			print(quiz.status)
	serializer = QuizSerializer(quizes, many=True)
	return Response(serializer.data,status=status.HTTP_200_OK)









