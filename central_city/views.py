from django.http import JsonResponse

def index(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Bem vindo à Central City!'})

def herois(request):
    if request.method == 'GET':
        heroi = {
            'id': 1,
            'nome': 'Barry Allen',
            'codinome': 'Flash',
            'poder': 'Super velocidade',
            'profissao': 'Policial',
            'primeira_aparicao': 'Flash Comics #1 (1940)'
        }
        return JsonResponse(heroi)

def viloes(request):
    if request.method == 'GET':
        vilao = {
            'id': 1,
            'nome': 'Eobard Thawne',
            'codinome': 'Professor Zoom',
            'poder': 'Super velocidade',
            'profissao': 'Cientista',
            'primeira_aparicao': 'The Flash #139 (1963)'
        }
        return JsonResponse(vilao)