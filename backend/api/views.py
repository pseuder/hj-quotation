from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Product, Other, Unit, Attachment
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
            newUserID = User.objects.latest('id').id + 1
            User.objects.create(id=newUserID, account=adduserData['account'], password=adduserData['password'])
            return HttpResponse(newUserID)
    except Exception as e:
        return HttpResponse(e)

@csrf_exempt
def addProduct(request):
    '''新增商品資料'''
    try:
        if request.method == 'POST':
            addproductData = json.loads(request.body)['addproductData']
            newProductID = Product.objects.latest('id').id + 1
            Product.objects.create(id=newProductID, brand=addproductData['brand'], category=addproductData['category'], name=addproductData['name'], unitPrice=addproductData['unitPrice'])
            return HttpResponse(newProductID)
    except Exception as e:
        return HttpResponse(e)


@csrf_exempt
def addOther(request):
    '''新增其他資料'''
    try:
        if request.method == 'POST':
            addotherData = json.loads(request.body)['addotherData']
            newOtherID = Other.objects.latest('id').id + 1
            Other.objects.create(id=newOtherID, name=addotherData['name'], unitPrice=addotherData['unitPrice'])
            return HttpResponse(newOtherID)
    except Exception as e:
        return HttpResponse(e)

@csrf_exempt
def getUnit(request):
    '''回傳單位資料'''
    if request.method == 'GET':
        units = Unit.objects.all()
        units = [{'id': unit.id, 'name': unit.name} for unit in units]
        return HttpResponse(json.dumps(units))

@csrf_exempt
def addUnit(request):
    '''新增單位資料'''
    if request.method == 'POST':
        addunitData = json.loads(request.body)['addunitData']
        try:
            newUnitID = Unit.objects.latest('id').id + 1
        except Exception as e:
            newUnitID = 1
        Unit.objects.create(id=newUnitID, name=addunitData['name'])
        return HttpResponse(newUnitID)

@csrf_exempt
def deleteUnit(request):
    '''刪除單位資料'''
    if request.method == 'POST':
        id = json.loads(request.body)['id']
        Unit.objects.get(id=id).delete()
        return HttpResponse('success')

@csrf_exempt
def getAttachment(request):
    '''回傳附件資料'''
    if request.method == 'GET':
        attachments = Attachment.objects.all()
        attachments = [{'id': attachment.id, 'name': attachment.name, 'remark': attachment.remark} for attachment in attachments]
        return HttpResponse(json.dumps(attachments))


@csrf_exempt
def addAttachment(request):
    '''新增附件資料'''
    if request.method == 'POST':
        addattachmentData = json.loads(request.body)['addattachmentData']
        try:
            newAttachmentID = Attachment.objects.latest('id').id + 1
        except Exception as e:
            newAttachmentID = 1
        Attachment.objects.create(id=newAttachmentID, name=addattachmentData['name'], remark=addattachmentData['remark'])
        return HttpResponse(newAttachmentID)

@csrf_exempt
def deleteAttachment(request):
    '''刪除附件資料'''
    if request.method == 'POST':
        id = json.loads(request.body)['id']
        Attachment.objects.get(id=id).delete()
        return HttpResponse('success')

@csrf_exempt
def editAttachment(request):
    '''編輯附件資料'''
    if request.method == 'POST':
        editattachmentData = json.loads(request.body)['editattachmentData']
        attachment = Attachment.objects.get(id=editattachmentData['id'])
        attachment.name = editattachmentData['name']
        attachment.remark = editattachmentData['remark']
        attachment.save()
        return HttpResponse('success')