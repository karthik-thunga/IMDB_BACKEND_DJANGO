from rest_framework import serializers
from core.watch_it.models import Content, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.ReadOnlyField(source = 'review_user.username')
    class Meta:
        model = Review
        exclude = ['content']

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        exclude = ['total_rating']
    rating = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    def get_rating(self, obj):
        total_rating = obj.total_rating
        count_rating = obj.count_rating
        if not (total_rating or count_rating):
            return 0
        return total_rating/count_rating
    
    def validate_release_year(self, year):
        if year < 1900:
            raise serializers.ValidationError("Movie release year must be after 1900")
        return year 
    

class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"
    
    content_list = ContentSerializer(many=True, read_only=True)


    # def create(self, validated_data):
    #     return Content.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.release_year = validated_data.get('release_year', instance.release_year)
    #     instance.released = validated_data.get('released', instance.released)
    #     instance.c_type = validated_data.get('c_type', instance.c_type)
    #     instance.lang = validated_data.get('lang', instance.lang)
    #     instance.save()
    #     return instance