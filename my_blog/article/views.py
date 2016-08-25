from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article


def detail(request, my_args):
	articles = Article.objects.all()[int(my_args)]
	str = ("title = %s, categry = %s, content = %s" % (articles.title, articles.category, articles.content))

	return HttpResponse(str)


def test(request):
	return render(request, 'test.html', {'current_time': datetime.now()})


def home(request):
	# 获取全部的Article对象
	post_list = Article.objects.all()
	return render(request, 'home.html', {'post_list' : post_list})
