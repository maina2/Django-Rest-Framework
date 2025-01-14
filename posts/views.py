from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view,APIView
from rest_framework import status,generics,mixins
from .models import Posts
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


class PostListCreateView(generics.GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin                
        ):
    serializer_class= PostSerializer
    queryset=Posts.objects.all()
    def get(self,request:Request,*args, **kwargs):
        return self.list(request,*args,*kwargs)
    def post(self,request:Request,*args, **kwargs):
        return self.create(request,*args,*kwargs)

class PostUpdateDeleteMixins(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=PostSerializer
    queryset= Posts.objects.all()
    def get(self,request:Request,*args, **kwargs):
        return self.retrieve(request,*args,*kwargs)
    def put(self,request:Request,*args, **kwargs):
        return self.update(request,*args,*kwargs)
    def delete(self,request:Request,*args, **kwargs):
        return self.destroy(request,*args,*kwargs)
class PostListCreateView(APIView):
    
    def get(self,request:Request, *args, **kwargs):
        posts= Posts.objects.all()
        serializer= PostSerializer(instance=posts,many=True)
        serializer=serializer.data

        return Response(data=serializer,status=status.HTTP_200_OK)
    def post(self,request:Request,*args, **kwargs):
        data= request.data
        serializer= PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response= {
                "message":"Created succesfully",
                "data":serializer.data
            }
            return Response(data=response,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_404_NOT_FOUND)

class UpdateView(APIView):
    def put(self,request:Request,post_id:int,*args, **kwargs):
        post= get_object_or_404(Posts,pk=post_id)
        data=request.data
        serializer= PostSerializer(instance=post,data=data)
        if serializer.is_valid():
            serializer.save()
            response= {
                "message":"This has been updated",
                "data":serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_304_NOT_MODIFIED)

class DeleteView(APIView):
    pass

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

@api_view(http_method_names=["PUT"])
def updatePost(request:Request,post_id:int):
    post= get_object_or_404(Posts,pk=post_id)
    data= request.data
    serializer= PostSerializer(instance=post,data=data)
    
    if serializer.is_valid():
        serializer.save()

        response={
            "message":"succesful Edit",
            "data":serializer.data
        }
        return Response(data=response,status=status.HTTP_200_OK) 
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=["DELETE"])
def DeletePost(request:Request,post_id:int):
    post= get_object_or_404(Posts,pk=post_id)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)