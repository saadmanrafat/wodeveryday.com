from rest_framework import serializers
from core.gym.models import Gym, GymDetails, GymLeaderboard


class GymSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gym
        fields = [
            'id',
            'website',
            'photo',
            'ready_to_link',
            'ordernum',
            'lat',
            'lon',
            'city',
            'name_search',
            'photo_version',
            'zip',
            'country_short_code',
            'bad_standing',
            'effective_date',
            'status',
            'address',
            'active',
            'state_code',
            'show_on_map',
            'kids',
            'name',
            'country',
            'org_type',
            'aid',
            'full_state',
            'continent',
            'name_slug'
        ]

class GymDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GymDetails
        fields = [
            'id',
            'gym_details_api_id',
            'data'
        ]


class GymLeaderboardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GymLeaderboard
        fields = [
            'id',
            'leaderboard_api_id',
            'data'
        ]
