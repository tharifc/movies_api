from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from movies.serializer import MovieSerializer, ReviewSerializer, UserSerializer, LoginSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from movies.models import Movie, Review
from rest_framework import status
from rest_framework.decorators import action


# cinima  pass naseehajanna.8


class MovieModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    model = Movie
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get_queryset(self):
        return Movie.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data, context={'user': request.user})

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    @action(methods=["post"],detail=True)
    def add_review(self, request,*args, **kwargs):
        id = kwargs.get('pk')
        movie = Movie.objects.get(id=id)
        user = request.user
        serializer=ReviewSerializer(data=request.data,context={"user":user,"movie":movie})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)




class UserCreation(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SigninView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            uname = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            user = authenticate(request, username=uname, password=password)

            if user:
                login(request, user)
                return Response({"msg": "login success"})
            else:
                return Response({"msg": "invalid credentials"})
        else:
            return Response({"msg": "login success"})


class ReviewModelViewSet(ModelViewSet):
    model = Review
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
