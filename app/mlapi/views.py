from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Diamond
from .serializers import DiamondSerializer

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
    
    clarity_numeric = clarity_mapping.get(clarity, 0)  # Added default value in case of missing mapping
    cut_numeric = cut_mapping.get(cut, 0)
    color_numeric = color_mapping.get(color, 0)

    return clarity_numeric, cut_numeric, color_numeric

@api_view(['GET', 'POST'])
def mlapi_views(request):
    if request.method == "GET":
        return Response({'message': 'Diamond quality prediction API is working!'}, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serializer = DiamondSerializer(data=request.data)
        if serializer.is_valid():
            carat = float(serializer.validated_data.get('carat', 2.0))
            clarity = serializer.validated_data['clarity']
            cut = serializer.validated_data['cut']
            color = serializer.validated_data['color']
            depth = float(serializer.validated_data.get('depth', 55.0))
            table = float(serializer.validated_data.get('table', 54.0))
            
            # Additional processing (like ML predictions) can be added here
            clarity_numeric, cut_numeric, color_numeric = convert_to_numeric(clarity, cut, color)
            X = [carat, clarity_numeric, cut_numeric, color_numeric, depth, table] 
            print(f'X feature vector is:{X}')
            prediction=1
            # Save to database
            diamond = Diamond(carat=carat, clarity=clarity, cut=cut, color=color, depth=depth, table=table, prediction=prediction)
            diamond.save()

            return Response({'data': serializer.validated_data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

