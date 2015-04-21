from rest_framework import serializers
from lessons.models import Step, Activity, Tag

class StepSerializer(serializers.ModelSerializer):

	class Meta:
		model = Step
		fields = ('id', 'description', 'teachingnote', 
			'imagepath', 'sequence')


class TagSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tag
		fields = ('id', 'description')


class ActivitySerializer(serializers.ModelSerializer):

	steps = StepSerializer(many=True, required=False)
	tags = TagSerializer(many=True, required=False)
	class Meta:
		model = Activity
		fields = ('id', 'title', 'level', 'language', 'votecount', 'steps', 'tags')