from rest_framework import serializers

from .models import *

class AdminSerializer(serializers.ModelSerializer):
  class Meta():
    model = Admin
    fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta():
		model=User
		fields='__all__'

class QuizSerializer(serializers.ModelSerializer):
	class Meta():
		model=Quiz
		fields=( 'id','name','admin_id','status')

class QuestionSerializer(serializers.ModelSerializer):
	class Meta():
		model=Question
		fields=('__all__')

class AttemptSerializer(serializers.ModelSerializer):
	class Meta():
		model=Attempt
		fields=('__all__')

class AnswerSerializer(serializers.ModelSerializer):
	class Meta():
		model=Question
		fields=('id','answer')




