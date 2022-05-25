from rest_framework import serializers
from product.models import Product
from basket.models import Order


class OrderSerializer(serializers.Serializer):
    product = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate(self, attrs):
        data = {}
        try:
            product = Product.objects.get(pk=attrs['product'])
        except Product.DoesNotExist:
            raise serializers.ValidationError('Product is not found')
        quantity = attrs['quantity']
        data['quantity'] = quantity
        data['product'] = product.pk
        return data

    def save(self, **kwargs):
        data = self.validated_data
        user = kwargs['user']
        product = Product.objects.get(pk=data['product'])
        Order.objects.create(
            product=product,
            user=user,
            quantity=data['quantity'],
        )
