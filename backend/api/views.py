from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Product
import json, sys
sys.path.append("..")

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

@csrf_exempt
def getProduct(request):
    '''回傳商品資料'''
    if request.method == 'GET':
        products = Product.objects.all()
        products = [{'id': product.id, 'brand': product.brand, 'category': product.category, 'name': product.name, 'unitPrice': product.unitPrice} for product in products]
        return HttpResponse(json.dumps(products))