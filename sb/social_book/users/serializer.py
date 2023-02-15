from rest_framework import serializers
from .models import CustomUser, Uploaded_Files

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {
           'password': {'write_only': True}
        }


    # Using Built-in function to hash the password
    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uploaded_Files
        fields = ['title','author','publish_year','price','cover']#what we want to serialize are written inside this

    def validate(self,data):
        if data['price'] < 50:
            raise serializers.ValidationError({'error': "Price can not be less tha 50."})
        
        return data