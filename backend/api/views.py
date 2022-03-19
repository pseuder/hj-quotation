from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Product, Other
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

@csrf_exempt
def getOther(request):
    if request.method == 'GET':
        others = Other.objects.all()
        others = [{'id': other.id, 'name': other.name, 'unitPrice': other.unitPrice} for other in others]
        return HttpResponse(json.dumps(others))

@csrf_exempt
def getDatabaseTable(request):
    '''回傳資料庫資料表'''
    if request.method == 'GET':
        tables = [{'name': table.name, 'description': table.description} for table in User._meta.get_all_tables_with_content()]
        return HttpResponse(json.dumps(tables))

@csrf_exempt
def getUser(request):
    '''回傳使用者資料'''
    if request.method == 'GET':
        users = User.objects.all()
        users = [{'id': user.id, 'account': user.account, 'password': user.password} for user in users]
        return HttpResponse(json.dumps(users))

@csrf_exempt
def editUser(request):
    '''編輯使用者資料'''
    if request.method == 'POST':
        edituserData = json.loads(request.body)['edituserData']
        user = User.objects.get(id=edituserData['id'])
        user.account = edituserData['account']
        user.password = edituserData['password']
        user.save()
        return HttpResponse('success')

@csrf_exempt
def deleteUser(request):
    '''刪除使用者資料'''
    if request.method == 'POST':
        id = json.loads(request.body)['id']
        User.objects.get(id=id).delete()
        return HttpResponse('success')

@csrf_exempt
def editProduct(request):
    '''編輯商品資料'''
    if request.method == 'POST':
        editproductData = json.loads(request.body)['editproductData']
        product = Product.objects.get(id=editproductData['id'])
        product.brand = editproductData['brand']
        product.category = editproductData['category']
        product.name = editproductData['name']
        product.unitPrice = editproductData['unitPrice']
        product.save()
        return HttpResponse('success')

@csrf_exempt
def deleteProduct(request):
    '''刪除商品資料'''
    if request.method == 'POST':
        id = json.loads(request.body)['id']
        Product.objects.get(id=id).delete()
        return HttpResponse('success')


@csrf_exempt
def editOther(request):
    '''編輯其他資料'''
    if request.method == 'POST':
        editotherData = json.loads(request.body)['editotherData']
        other = Other.objects.get(id=editotherData['id'])
        other.name = editotherData['name']
        other.unitPrice = editotherData['unitPrice']
        other.save()
        return HttpResponse('success')

@csrf_exempt
def deleteOther(request):
    '''刪除其他資料'''
    if request.method == 'POST':
        id = json.loads(request.body)['id']
        Other.objects.get(id=id).delete()
        return HttpResponse('success')

@csrf_exempt
def addUser(request):
    '''新增使用者資料'''
    try:
        if request.method == 'POST':
            adduserData = json.loads(request.body)['adduserData']
            User.objects.create(account=adduserData['account'], password=adduserData['password'])
            newUserID = User.objects.get(account=adduserData['account'], password=adduserData['password']).id
            return HttpResponse(newUserID)
    except Exception as e:
        return HttpResponse(e)

@csrf_exempt
def addProduct(request):
    '''新增商品資料'''
    try:
        if request.method == 'POST':
            addproductData = json.loads(request.body)['addproductData']
            Product.objects.create(brand=addproductData['brand'], category=addproductData['category'], name=addproductData['name'], unitPrice=addproductData['unitPrice'])
            newProductID = Product.objects.get(brand=addproductData['brand'], category=addproductData['category'], name=addproductData['name'], unitPrice=addproductData['unitPrice']).id
            return HttpResponse(newProductID)
    except Exception as e:
        return HttpResponse(e)


@csrf_exempt
def addOther(request):
    '''新增其他資料'''
    try:
        if request.method == 'POST':
            addotherData = json.loads(request.body)['addotherData']
            Other.objects.create(name=addotherData['name'], unitPrice=addotherData['unitPrice'])
            newOtherID = Other.objects.get(name=addotherData['name'], unitPrice=addotherData['unitPrice']).id
            return HttpResponse(newOtherID)
    except Exception as e:
        return HttpResponse(e)

