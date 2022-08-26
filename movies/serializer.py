from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from movies.models import Movie, Review
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet, ModelViewSet


class MovieSerializer(ModelSerializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    average_rating = serializers.CharField(read_only=True)
    content_count = serializers.CharField(read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "user", "movie_name", "movie_year", "movie_director", "movie_image", "average_rating",
                  "content_count"]

    def create(self, validated_data):
        user = self.context.get('user')
        return Movie.objects.create(**validated_data, user=user)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ReviewSerializer(ModelSerializer):
    user = serializers.CharField(read_only=True)

    # movie = serializers.CharField(read_only=True)

    class Meta:
        model = Review
        exclude = ["movie"]

    def create(self, validated_data):
        user = self.context.get('user')
        movie = self.context.get('movie')
        # print("hereeee",movie)
        return Review.objects.create(user=user, movie=movie, **validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
