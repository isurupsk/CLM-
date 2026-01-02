from rest_framework import serializers
from to_do_list.models import ActionItemList

#############################################################################
############################ action_item_list ###############################
#############################################################################   

class ActionItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionItemList
        fields = '__all__'
