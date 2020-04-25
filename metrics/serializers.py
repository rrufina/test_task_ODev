from rest_framework import serializers

class CurrencySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=3)
    rate = serializers.IntegerField()
    date = serializers.DateField()

class MetricsSerializer(serializers.Serializer):
    std_dev = serializers.FloatField()
    avg = serializers.FloatField()

class RangeSerializer(serializers.Serializer):
    currency = serializers.CharField(max_length=3)
    metrics = MetricsSerializer()

class CorrelationSerializer(serializers.Serializer):
    currency1 = serializers.CharField(max_length=3)
    currency2 = serializers.CharField(max_length=3)
    base = serializers.CharField(max_length=3)
    correlation = serializers.FloatField()