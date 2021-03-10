
from rest_framework.views import APIView
from djangotemplate.models import Author
from djangotemplate.api.serializers import AuthorSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class AuthorListView(APIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self,request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid()
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    @action(detail=False,methods=["post"])
    def create(self,validated_data):
       pass

    def update(self, instance,validated_data):
        pass 

    def validate(self,data):
        pass 

    class Meta:
        fields = "__all__"
