from django.conf.urls import patterns, url
from geographyquiz import views

urlpatterns = patterns('',
        url(r'^$', views.take_the_quiz, name='take_the_quiz'),
        url(r'^answers/$', views.submit_answers, name='submit_answers'),
        url(r'^answers/email-sent/', views.email_send, name='email_send'),
        )
