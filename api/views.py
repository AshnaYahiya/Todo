from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import Registration,User,todoserializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import authentication,permissions
from work.models import Taskmodel

class Userregister(APIView):
    def post(self,request,*args,**kwargs):
        serializer=Registration(data=request.data)
        if serializer.is_valid():
            serializer.save()          #c u
        return Response(serializer.data)
#============================================================================================
 
class Todoviewsetview(ViewSet):
    # authentication_classes=[authentication.BasicAuthentication]    # oro tym u,p kodukanam
    authentication_classes=[authentication.TokenAuthentication]      # otta thavana token kodutha mathi
    permission_classes=[permissions.IsAuthenticated]


    def list(self,request,*args,**kwargs):
        qs=Taskmodel.objects.all()
        serializer=todoserializer(qs,many=True)
        return Response(serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=todoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
        return Response(serializer.data)

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Taskmodel.objects.get(id=id)
        if qs.user==request.user:               # login cheytha userude mathram task delete aakan aanu condition koduthekunath allatha paksham nmk ellam delete aakan sathikum ath fault alle 
            qs.delete()                         # qs inte ollil user ind taskmodel tableil indu ath so qs.user
            return Response({"message":"Todo object deleted"})
        else:
            return Response({"message":"not allowed"})

    def update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Taskmodel.objects.get(id=id)
        serializer=todoserializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Taskmodel.objects.get(id=id)
        serializer=todoserializer(qs)
        return Response(serializer.data)
    
# ============================================ MODEL SET VIEW =========================================================
# ===================================  another method for APIview  it is simple bcz c,u,d,r already set in the Modelsetview class=======================================================================

class Todomodelviewset(ModelViewSet):
    queryset=Taskmodel.objects.all()
    serializer_class=todoserializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)            # user nte name varan aayittgit 

    # def get_queryset(self):
    #     return Taskmodel.objects.filter(user=self.request.user)     # ivar ivide r,u,d,c okke view ezhuthiitund pakshee athil login cheytha userude kaanan padolunn olla conditions venamenghil nml cheyyanam athinn vendit already avr cheyth vechekana class ne override cheyyanam.get_queryset enn ollath already olla method aanuz



# router.register('todomodel',Todomodelviewset,basename='api')

