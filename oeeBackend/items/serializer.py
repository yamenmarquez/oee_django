from rest_framework.serializers import ModelSerializer
from .models import Item

class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ('pk', 'item_code', 'item_name')