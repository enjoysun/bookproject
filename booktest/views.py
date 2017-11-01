#encoding:utf-8
from django.shortcuts import render
from django.http import  *
from .models import *

joinurl="booktest"
# Create your views here.
def index(request):
    booklist=Book.objects.all()
    contest={"list":booklist}
    return render(request,"{0}/Index.html".format(joinurl),contest)
def bookdetail(request,bid):
    book=Book.objects.get(pk=bid)#注意filter和get区别：filter返回queryset对象   get返回model对象
    detaillist=book.hero_set.all()#一对多关系查询对应多个子信息，可直接小写类名_set.all()
    context={"detaillist":detaillist,"booklist":book}
    return render(request,'{0}/bookdetail.html'.format(joinurl),context)
