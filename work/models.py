from django.db import models
from django.contrib.auth.models import User    # already django ellam set cheyth vechitund jzt calll cheytha mathi user ne we get user page


class Taskmodel(models.Model):

    task_model=models.CharField(max_length=50)

    task_discription=models.TextField(null=False)

    created_date=models.DateField(auto_now_add=True)     # automatic aayitt innathe date vannolum auto_now_add koduthal

    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)     # rand table aayitann userum taskmodelum so randinem connect cheyyan vendittann foreign key ennalann aah user nte values athintethaya tableil povollu

    completed= models.BooleanField(default=False)       # task complete aayo illen ariyan aannu , default aayitt false koduthalan complete aayittilla enn varollu . then cheyth kazhinnitt true aakam
