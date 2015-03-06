from operator import itemgetter
from django.shortcuts import render
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotModified
from django.db.models import Q
from geographyquiz.models import Questions, Answers
from django.core.mail import send_mail, BadHeaderError

def email_send(request):
    from_name = request.POST.get('shareName', '')
    subject = 'Your Mesa County Geography Quiz Results'
    from_email = 'gis@mesacounty.us'
    to_email = request.POST.get('Email', '')
    message = request.POST.get('message', '')
    if from_name and to_email and message:
        try:
            send_mail(subject, message, from_email, [to_email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, 'geographyquiz/email_confirmation_page.html')


def take_the_quiz(request):
    question_list = Questions.objects.order_by("?")[:10]
    answers = []
    for q in question_list:
        answers += Answers.objects.filter(question_id=q.id)
    context_dict = {'question':question_list, 'answers':answers}
    return render(request, 'geographyquiz/take_the_quiz.html', context_dict)

def submit_answers(request):
    answers = request.POST.lists()
    answers = [x for x in answers if not 'csrfmiddlewaretoken' in x]
    answers.sort(key=lambda x: int(x[1][0]))
    question_list=[]
    answer_list = []
    correct_answers = []
    wrong_answer_explanations = []
    explanations = []
    url = []
    yn = []
    right = 0
    righttxt = ''
    wrong = 0

    for x in answers:
        print x
        if x[1][1][-1:] == 'y':
            right += 1
        elif x[1][1][-1:] == 'n':
            wrong += 1
        question_list += Questions.objects.filter(id=int(x[0]))        
        answer_list += Answers.objects.filter(question_id=int(x[0])).filter(choice_text=x[1][1][:-2]).values_list('choice_text', flat=True)
        yn += x[1][1][-1:]
        explanations += Answers.objects.filter(question_id=int(x[0])).filter(choice_text=x[1][1][:-2]).values_list('explanation', flat=True)
        url += Answers.objects.filter(question_id=int(x[0])).filter(choice_text=x[1][1][:-2]).values_list('url', flat=True)

    answers = [list(x) for x in answers]

    answers = [' '.join(str(c) for c in lst) for lst in answers]


    if right >= 8:
        righttxt = "Great job! You answered " + str(right) + " out of 10 questions correctly!"
    elif right <= 7 and right > 6:
        righttxt = "Good job! You answered " + str(right) + " out of 10 questions correctly!"
    elif right <= 5 and right > 0:
        righttxt = "You only answered " + str(right) + " out of 10 questions correctly!<br><br> You might want to spend some time in the County Library's <a style='color:blue' href='http://guides.mesacountylibraries.org/c.php?g=119446&p=779175'>regional history room</a>."    
    elif right == 0:
        righttxt = "You didn't answer any questions correctly!<br><br> You might want to spend some time in the County Library's <a style='color:blue' href='http://guides.mesacountylibraries.org/c.php?g=119446&p=779175'>regional history room</a>."
    else:
        righttxt = "You answered " + str(right) + " out of 10 questions correctly!"

##    question_list = zip(question_list,correct_answers,wrong_answer_explanations, url, answers)
    question_list = zip(question_list,answer_list,yn,explanations,url)
    context_dict = {'questions':question_list, 'right':right, 'righttxt':righttxt}
    return render(request, 'geographyquiz/quiz_answers.html', context_dict)
    

