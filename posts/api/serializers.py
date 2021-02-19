from rest_framework import serializers
from likes import services as likes_services
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'body',
            'is_fan',
            'total_likes',
        )

    def get_is_fan(self, obj) -> bool:
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)
