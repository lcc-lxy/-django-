from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
# Create your views here.
def add_book(request):
    if request.method =='GET':
        return render(request,'bookstore/add_book.html')
    if request.method =='POST':
        dic = {}
        dic['bookname'] = request.POST.get('bookname')
        dic['pub'] = request.POST.get('pub')
        dic['price'] = request.POST.get('price')
        dic['market_price'] = request.POST.get('market_price')
        dic['act'] = request.POST.get('act')
        if not dic['act']:
            dic['act'] = True
        dic['info'] = '<script> alert("添加成功") </script> '
        Book.objects.create(title=dic['bookname'],pub=dic['pub'],price=dic['price'],marker_price=dic[
            'market_price'])
        return render(request, 'bookstore/add_book.html',dic)
def all_book(request):
    if request.method == 'GET':
        # dic = {}
        all_info = Book.objects.all()
        a1 = type(all_info)
        return render(request,'bookstore/all_book.html',locals())
def detail(request,title):
    try:
        book = Book.objects.get(title=title)
    except Exception as e:
        return HttpResponse('您当前查询有误')
    return render(request,'bookstore/update.html',locals())
def update_book(request,title):
    if request.method=='POST':
        m_price = request.POST.get('m_price')
        #查
        books = Book.objects.filter(title=title)
        if not books:
            return HttpResponse('当前页面查阅书籍不存在')
        if request.method != 'POST':
            return HttpResponse('当前请求异常')
        book = books[0]
        book.marker_price = m_price
        book.save()
        return HttpResponseRedirect('/bookstore/all_book')
        # return render(request,'bookstore/all_book')
def delete(request,title):
    try:
        auth = Book.objects.filter(title=title)
        auth.delete()
    except:
        return HttpResponse('请求失败1111')
    return HttpResponseRedirect('/bookstore/all_book')
