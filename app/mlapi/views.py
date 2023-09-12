from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def convert_to_numeric(clarity, cut, color):
    # Define mappings for label encoding
    clarity_mapping = {
        'IF': 0, 'VVS1': 1, 'VS1': 2, 'SI1': 3, 'I1': 4
    }
    cut_mapping = {
        'Poor': 0, 'Fair': 1, 'Good': 2, 'Very Good': 3, 'Excellent': 4
    }
    color_mapping = {
        'J': 0, 'I': 1, 'H': 2, 'G': 3, 'F': 4, 'E': 5, 'D': 6, 'C': 7, 'B': 8, 'A': 9
    }
    
    clarity_numeric = clarity_mapping[clarity]
    cut_numeric = cut_mapping[cut]
    color_numeric = color_mapping[color]

    return clarity_numeric, cut_numeric, color_numeric

# Create your views here.
@api_view(['GET', 'POST'])
def mlapi_views(request):
    if request.method == "GET":
        return Response({'message': 'Diamond quality prediction API is working!'}, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        # Accessing the form data
        carat = request.POST.get('carat')
        clarity = request.POST.get('clarity')
        cut = request.POST.get('cut')
        color = request.POST.get('color')
        depth = request.POST.get('depth')
        table = request.POST.get('table')
        clarity, cut, color = convert_to_numeric(clarity, cut, color)
        print(f"Carat: {carat}, Clarity: {clarity}, Cut: {cut}, Color: {color}, Depth: {depth}, Table: {table}")
        X = [carat, clarity, cut, color, depth, table]
        Y = predict(X)
    return Response({'data': request.data})
