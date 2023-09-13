from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal

class Diamond(models.Model):
    
    # Carat
    carat = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        validators=[
            MinValueValidator(Decimal('0')),
            MaxValueValidator(Decimal('5'))
        ]
    )
    
    # Clarity
    CLARITY_CHOICES = [
        ('I1', 'I1'),
        ('SI1', 'SI1'),
        ('VS1', 'VS1'),
        ('VVS1', 'VVS1'),
        ('IF', 'IF'),
    ]
    clarity = models.CharField(
        max_length=5, 
        choices=CLARITY_CHOICES, 
        default='I1'
    )
    
    # Cut
    CUT_CHOICES = [
        ('Poor', 'Poor'),
        ('Fair', 'Fair'),
        ('Good', 'Good'),
        ('Very Good', 'Very Good'),
        ('Excellent', 'Excellent'),
    ]
    cut = models.CharField(
        max_length=10, 
        choices=CUT_CHOICES, 
        default='Poor'
    )
    
    # Color
    COLOR_CHOICES = [
        ('J', 'J'),
        ('I', 'I'),
        ('H', 'H'),
        ('G', 'G'),
        ('F', 'F'),
        ('E', 'E'),
        ('D', 'D'),
        ('C', 'C'),
        ('B', 'B'),
        ('A', 'A'),
    ]
    color = models.CharField(
        max_length=2, 
        choices=COLOR_CHOICES, 
        default='J'
    )
    
    # Depth
    depth = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        validators=[
            MinValueValidator(Decimal('55')),
            MaxValueValidator(Decimal('70'))
        ],
        default=55
    )
    
    # Table
    table = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        validators=[
            MinValueValidator(Decimal('54')),
            MaxValueValidator(Decimal('64'))
        ],
        default=54
    )

    def __str__(self):
        return f"Diamond {self.pk} - {self.carat} carat"
