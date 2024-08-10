from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from users.models import CustomUser

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField( 
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "nickname",
            "gender",
            "password",
        ]

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data["email"],
            nickname=validated_data["nickname"],
            gender=validated_data["gender"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
        