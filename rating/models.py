from pyexpat import model
from django.db import models
from product.models import NewProduct
from django.contrib.auth import get_user_model

User = get_user_model()

class Mark():
    one = 1
    two = 2
    three = 3 
    four = 4
    five = 5

    marks = (
    (one, 'Bad!'),
    (two, 'Not that bad!'),
    (three, 'Normal!'),
    (four, 'Good!'),
    (five, 'Excellent!'),
    )

class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    product = models.ForeignKey(NewProduct, on_delete=models.CASCADE, related_name='ratings')
    mark = models.PositiveSmallIntegerField(choices=Mark.marks)

    def __str__(self) -> str:
        return f'{self.mark}-> {self.product}'

    class Meta:
        unique_together = ('owner', 'product')

