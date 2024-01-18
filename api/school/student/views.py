from django.shortcuts import render
from rest_framework.decorators import api_view
from . models import Student
from. serializer import Student_serializer
from django.http import JsonResponse

# Create your views here.

@api_view(['POST'])
def add_student(request):
    print(request.data)
    serialize_data = Student_serializer(data=request.data)
    if serialize_data.is_valid():
        
        serialize_data.save()
        return JsonResponse({'msg':'data insert successfully','status':200})
    else:
        print(serialize_data.errors)
        print('data not valid')
        return JsonResponse({'msg':'erorr','status': 201})
    
@api_view(['GET'])
def load_student(request):
    students = Student.objects.all()
    serialize_data = Student_serializer(students,many=True)
    return JsonResponse(serialize_data.data,safe=False)

@api_view(['DELETE'])
def delete_student(request,sid):
    student = Student.objects.get(id=sid)
    student.delete()
    return JsonResponse({'msg':'delete successflly'})

@api_view(['PUT'])
def update_student(request,sid):
    student = Student.objects.get(id=sid)
    serialized_data = Student_serializer(student,data=request.data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'msg':'update successfully'})
    else:
        return JsonResponse({'msg':'errorr'})