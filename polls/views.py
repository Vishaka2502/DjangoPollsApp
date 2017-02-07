from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'polls/index.html', context)
    if request.method == 'GET':
        serializer = QuestionSerializer(latest_question_list, many=True)
        return Response(serializer.data)#, status=None, template_name=None, headers=None, content_type='application/xml')

    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, template_name=None, headers=None, content_type='application/xml')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        latest_question_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def all_choices(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    latest_choices_list = Choice.objects.all()
    # for choices in latest_question_list:
    #     for choice in choices.choice_set.all():
    #         latest_choices_list.append(choice)
    if request.method == 'GET':    
        serializer = ChoiceSerializer(latest_choices_list, many=True)
        return Response(serializer.data)

        # context = {'latest_choices_list': latest_choices_list}
        # return render(request, 'polls/choices.html', context)

    elif request.method == 'POST':
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        latest_choices_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def detail(request, question_id):
  
    question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})
    if request.method == 'GET':    
        serializer = QuestionSerializer(question, many=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def choices(request, question_id):

    choices = Choice.objects.filter(question = question_id)  
    # question = get_object_or_404(Question, pk=question_id)
    # choices = question.choice_set.all()
    # context = {'choices': choices}
    # return render(request, 'polls/choice.html', context)
    if request.method == 'GET':    
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        choices.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def choice(request, question_id, choice_id):
    choices = Choice.objects.filter(question=question_id)
    ch = choices[int(choice_id)-1]
    # question = get_object_or_404(Question, pk=question_id)
    # choices = question.choice_set.all()
    if request.method == 'GET':    
        serializer = ChoiceSerializer(ch, many=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(['GET', 'POST'])
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# @api_view(['GET', 'POST'])
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/vote.html', {'question': question})
