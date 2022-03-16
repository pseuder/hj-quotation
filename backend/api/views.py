from django.shortcuts import render
from .models import User
# Create your views here.
from django.http import HttpResponse
import json
import sys
sys.path.append("..")#為了呼叫上級py檔案函式
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt


#-------------------login------------------------#
@csrf_exempt
def login(request):
    '''登入資料核對及回傳資料'''
    if request.method == 'GET':
        account = request.GET['account']
        password = request.GET['password']
        if User.objects.filter(account=account, password=password):
            return HttpResponse('success')
        else: 
            return HttpResponse('fail')