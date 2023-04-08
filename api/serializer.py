from api.models import Article
from rest_framework.serializers import ModelSerializer


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','content','image']

