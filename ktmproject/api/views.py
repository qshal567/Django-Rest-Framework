from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http  import HttpResponse
# Create your views here.
# Model Object - Single Student Data

# def student_data(request):
#     kushal = Student.objects.get(id=1)
#     print(kushal)
#     converting_to_serializer = StudentSerializer(kushal)
#     print( converting_to_serializer)
#     print( converting_to_serializer.data)
#     json_date = JSONRenderer().render( converting_to_serializer.data)
#     print(json_date)
#     return HttpResponse(json_date, content_type ='application/json')

# Query Set = All Student data

def student_list(request):
    kushal = Student.objects.all()
    converting_to_serializer = StudentSerializer(kushal, many= True)
    json_data = JSONRenderer().render( converting_to_serializer.data)
    return HttpResponse(json_data, content_type ='application/json')
