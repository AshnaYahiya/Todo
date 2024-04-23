from django import forms
from work.models import User,Taskmodel



class Register(forms.ModelForm):
    class Meta:

        model= User
        fields=['username',"first_name","last_name","email","password"]
        widgets={
            'username':forms.TextInput(attrs={'class':"form-control","placeholder":"enter the username"}),
            'first_name':forms.TextInput(attrs={'class':'form-control',"placeholder":"enter the firstname"}),
            'last_name':forms.TextInput(attrs={'class':"form-control","placeholder":"enter the last name"}),
            'email':forms.TextInput(attrs={'class':'form-control',"placeholder":"enter the email"}),
            'password':forms.TextInput(attrs={'class':"form-control",'placeholder':"enter secure password"})
            
        }
        
# ================================== ==================
class Taskform(forms.ModelForm):
    class Meta:

        model=Taskmodel
        fields=['task_model','task_discription']
        widgets={
            'task_model':forms.TextInput(attrs={'class':"form-control","placeholder":"enter the task"}),
            'task_discription':forms.Textarea(attrs={'class':'form-control','column':20,"row":5,"placeholder":"enter the discription"})
        }


class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()