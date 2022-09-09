from rest_framework import serializers

from webapp.models import Seamstress, SewingMachines


class SeamstressSerializer(serializers.ModelSerializer):
    machine_name = serializers.SerializerMethodField()

    class Meta:
        model = Seamstress
        fields = ['name', 'surname', 'sewing_machines', 'machine_name', 'total', 'price_per_product', 'total_price']

    def get_machine_name(self, obj):
        serializer = SewingMachinesSerializer([obj], many=True)
        print(serializer.data)
        return serializer.data


class SewingMachinesSerializer(serializers.ModelSerializer):

    class Meta:
        model = SewingMachines
        fields = ['name']


