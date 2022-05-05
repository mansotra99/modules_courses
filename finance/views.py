from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from .models import *
from .serializers import *
from .constants import *


class GetModulesView(APIView):
    def get(self, request):
        
        module_id = request.query_params.get('module_id')
        user_id = request.query_params.get('user_id')

        user = User.objects.filter(id=user_id).last()
        module_qs = Module.objects.filter(id=module_id)
        
        if not module_qs.exists() or not user:
            return Response({"Success":False,"Message":"Invalid Module or User"}, status=HTTP_404_NOT_FOUND)
        return Response({"Success":True, "data":MouduleSerializer(module_qs.last(), user.id).data}, status=HTTP_200_OK)


class GetChaptersView(APIView):
    def get(self, request):
        module_id = request.query_params.get('module_id')

        chapter_qs = Chapter.objects.filter(module_id=module_id)
        if not chapter_qs.exists():
            return Response({"Success":False,"Message":"Invalid Module"}, status=HTTP_404_NOT_FOUND)
        return Response({"Success":True, "data":ChapterSerializer(chapter_qs, many=True).data}, status=HTTP_200_OK)


class HeaderDetailsView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')

        user = User.objects.filter(id=user_id).last()

        if not user:
            return Response({"Success":False,"Message":"Invalid User"}, status=HTTP_404_NOT_FOUND)
        
        total_points = user.total_points
        completed_count = UserModule.objects.filter(user_id=user_id, module_status=STATUS_CHOICES.COMPLETED).count()
        started_count = UserModule.objects.filter(user_id=user_id, module_status=STATUS_CHOICES.STARTED).count()
        pending_count = UserModule.objects.filter(user_id=user_id, module_status=STATUS_CHOICES.PENDING).count()

        data = {
            'completed_count':completed_count,
            'started_count':started_count,
            'pending_count':pending_count,
            'total_points': total_points
        }
        return Response({"Success":True, "data":data}, status=HTTP_200_OK)


class GetQuestionsView(APIView):
    def get(self, request):
        module_id = request.query_params.get('module_id')
        quiz_qs = Quiz.objects.filter(module_id=module_id)
        if not quiz_qs.exists():
            return Response({"Success":False,"Message":"Invalid Module"}, status=HTTP_404_NOT_FOUND)
        return Response({"Success":True, "data":QuizSerializer(quiz_qs, many=True).data}, status=HTTP_200_OK)
        


class VerifyAnswersView(APIView):
    def post(self, request):
        
        question_id = request.query_params.get('question_id')
        selected_option_id = request.query_params.get('selected_option_id')

        quiz = Quiz.objects.filter(id=question_id)
        if not quiz.exists():
            return Response({"Success":False,"Message":"Invalid Question"}, status=HTTP_404_NOT_FOUND)
        
        return Response({"Success":False,"Correct":selected_option_id==quiz.correct_option,"Explanation":quiz.explanation}, status=HTTP_200_OK)