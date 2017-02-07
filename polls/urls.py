from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'polls'
urlpatterns = [
	# ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

	# ex: /polls/choices/
    url(r'^choices/$', views.all_choices, name='All Choices'),
	# ex: /polls/1/choices/
    url(r'^(?P<question_id>[0-9]+)/choices/$', views.choices, name='Choices'),
	# ex: /polls/1/choices/1
    url(r'^(?P<question_id>[0-9]+)/choices/(?P<choice_id>[0-9]+)/$', views.choice, name='Choice'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
