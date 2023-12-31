from rest_framework import serializers
from .models import Venue, Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True
    )
    
    venue_id = serializers.PrimaryKeyRelatedField(
        queryset=Venue.objects.all(),
        source='venue'
    )
    
    class Meta:
       model = Event
       fields = ('id', 'venue_id', 'name', 'date', 'time', 'ticket_price', 'city', 'state', 'venue', 'image_url', 'event_description')


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = EventSerializer(
        many=True,
        read_only=True
    )

    venue_url = serializers.ModelSerializer.serializer_url_field(
        view_name='venue_detail'
    )

    class Meta:
       model = Venue
       fields = ('id', 'venue_url', 'name', 'location', 'capacity', 'website_url', 'events', 'image_url', 'venue_description')


# test
# test 2