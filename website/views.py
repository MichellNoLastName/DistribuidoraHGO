from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request,"website/index.html",{})

def aboutus(request):
    return render(request,"website/aboutus.html",{})

def load_products(request,str_description):
    with connection.cursor() as cursor:
        cursor.execute("CALL sp_ObtenerArticulosLike(%s)",[str_description])
        result = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        # Convertir los resultados en una lista de diccionarios
        result_dict = [dict(zip(columns, row)) for row in result]
    return JsonResponse(result_dict,safe=False)
