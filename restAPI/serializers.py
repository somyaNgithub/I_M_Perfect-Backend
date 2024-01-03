from rest_framework import serializers
from .models import CustomUser ,Question , Answers ,UserType, PasswordResetToken
from drf_extra_fields.fields import Base64ImageField
from .models import OTP




class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Set write_only to True for password field
    userType = serializers.ChoiceField(choices=UserType.choices(), required=False)
    avatar = Base64ImageField(required=False)
    
    class Meta:
        model = CustomUser
        fields =['U_id', 'userType','userName','password','fullName','age','gender','address','mobileNo', 'country','avatar']





        
#-----------------for use in other Serializer --------------------------------------------------# 
class CustomUtilsUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields =[ 'userType','userName','fullName','avatar']




# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['cat_id', 'name']




class QuestionSerializer(serializers.ModelSerializer):
    user = CustomUtilsUserSerializer(source='U_id', read_only=True)
    # categories = CategorySerializer(many=True)
    class Meta:
        model = Question
        fields = ['title', 'description', 'pub_date', 'U_id', 'like_count', 'dislike_count','Q_id','user']

    # Make pub_date optional
    extra_kwargs = {'pub_date': {'required': False},
	                'U_id': {'required': False},
                    #  'categories' : {'required': False }
	                }
    def create(self, validated_data):
        # The 'user' field is already included in the validated_data
        return Question.objects.create(**validated_data)




# ------------------------------------------answer Serializer ------------------------------------------------
class AnswersSerializer(serializers.ModelSerializer):
    user = CustomUtilsUserSerializer(source='U_id', read_only=True)
    class Meta:
        model = Answers
        fields = ['Answer','pub_date','updated_date','U_id','Q_id','like_count','dislike_count','A_id','user']
    extra_kwargs = {'pub_date': {'required': False},
	'user_id': {'required': False}
	}
    # def create(self, validated_data):
        # Set default user type if not provided
        # user_type = validated_data.get('userType', UserType.USER.value)
        # validated_data['userType'] = user_type
        # return super().create(validated_data)   




class OTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTP
        fields = ['otp', 'email']



class PasswordResetTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordResetToken
        fields = ['token', 'created_at']

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

