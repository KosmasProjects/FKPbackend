from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'author', 'created_at', 'updated_at', 'image', 'fundacja_kochania_poznania', 'pomniki_poznania', 'wspolna_sprawa', 'cieliczko_pl', 'poznanskie_legendy']