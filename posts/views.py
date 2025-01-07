from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Posts
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


@api_view(http_method_names=["GET","POST"])
def homepage(request:Request):
    if request.method =="POST":
        data= request.data
        response= {"sent":"This is the message sent","data":data}
        return Response(data=response,status=status.HTTP_201_CREATED)

    response= {"message":"Hello World"}
    return Response(data=response,status=status.HTTP_200_OK)

@api_view(http_method_names=["GET","POST"])
def all_posts(request:Request):
    posts= Posts.objects.all()

    if request.method == "POST":
        data =request.data
        serializer= PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response={
                "message":"This is working",
                "data":serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    serializer= PostSerializer(instance=posts,many=True)
    
    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail(request:Request,post_id:int):
    post = get_object_or_404(Posts,pk=post_id)
    serializer= PostSerializer(instance=post)
    serializer=serializer.data
    return Response(data=serializer,status=status.HTTP_200_OK)
    