from rest_framework import serializers
from feed.models import Post,Comment,Like,Follow
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post_obj = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    owner_obj = serializers.ReadOnlyField(source='owner_obj.username')
    post_obj = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'

    def validate(self, data):
        request = self.context.get('request')
        post_obj = self.context.get('view').kwargs.get('pk')

        if Like.objects.filter(
            owner_obj=request.user,
            post_obj_id=post_obj
        ).exists():
            raise serializers.ValidationError(
                "You have already liked this post."
            )

        return data

class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='follower.username')

    class Meta:
        model = Follow
        fields = '__all__'

    def validate_following(self, value):
        request = self.context.get('request')

        if value == request.user:
            raise serializers.ValidationError("You cannot follow yourself.")
        return value

    def validate(self, data):
        request = self.context.get('request')
        following = data.get('following')

        if Follow.objects.filter(follower=request.user,following=following).exists():
            raise serializers.ValidationError("You are already following this user.")

        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']