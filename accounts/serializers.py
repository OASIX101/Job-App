from rest_framework import serializers

class LogOutSerializer(serializers.Serializer):

    refresh_token = serializers.CharField(max_length=255)


class LogInSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)