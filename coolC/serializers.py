from rest_framework import serializers
from coolC.models import Measure

class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Measure 
        fields=('id','Mvt','Temp','Date','Time','TempExt')
