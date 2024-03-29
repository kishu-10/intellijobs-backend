from django.forms import ValidationError
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        request = self.context.get('request')
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        user = dict()
        if not self.user.is_email_verified:
            raise ValidationError(
                {'message': 'Please verify your email address.'})
        if not self.user.has_profile:
            raise ValidationError(
                {'message': 'Please complete the registration process for your profile.'})
        if self.user.user_type == "Organization" and self.user.org_profile.verification_status!="Verified":
            raise ValidationError(
                {'message': "Your company's registration has not been verified."})
        try:
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
            user['id'] = self.user.id
            user['uuid'] = self.user.user_uuid
            user['username'] = self.user.username
            user['email'] = self.user.email
            user["user_type"] = self.user.user_type
            user["verified_email"] = self.user.is_email_verified
            if self.user.user_type == "Candidate":
                user['name'] = self.user.user_profile.get_full_name()
            elif self.user.user_type == "Organizaiton":
                user['name'] = self.user.org_profile.name
            else:
                user['name'] = "Staff User"
            if self.user.user_type == "Candidate":
                if self.user.user_profile.display_picture:
                    user['picture'] = request.build_absolute_uri(
                        self.user.user_profile.display_picture.url)
            elif self.user.user_type == "Organization":
                if self.user.org_profile.display_picture:
                    user['picture'] = request.build_absolute_uri(
                        self.user.org_profile.display_picture.url)
            data['user'] = user
        except User.DoesNotExist:
            pass
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
