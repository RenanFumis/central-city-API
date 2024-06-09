from django.http import JsonResponse

def index(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Bem vinda à Central City!'})

def herios(request):
    pass
