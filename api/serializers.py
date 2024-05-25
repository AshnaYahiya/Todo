from rest_framework import serializers
from work.models import User,Taskmodel


class Registration(serializers.ModelSerializer):
    class Meta:
        model=User

        fields=['id','username','email','password','first_name','last_name']
        read_only_fields=['id']      # id automatic vannam actually ath databaseilund pakshee ath api yil kaanan, athayath id read cheyyan read_only kodukunnu


    def create(self,validated_data):    # ith odelserializer clssil already defined aayitullathan validated data athinne overridde cheyipichu create_user aakii
        return User.objects.create_user(**validated_data)   # password encrypted aakan
    

class todoserializer(serializers.ModelSerializer):

    user=serializers.StringRelatedField(read_only=True)     # user=1,2,3 etc aanu varolu name varillla userude name varan aayitt inghne kodukanam user is connected with User throught foreing key  so it has username,password,email etc so we call user=

    class Meta:
        model=Taskmodel
        fields="__all__"      # taskname,description maathram user kodukunathann bakki ellam automatic generate avvanam athin venditt read_only koduthu ennale ath avide varoluu automatic generate cheytath
        read_only_fields=['id','created_data','user','completed']  

