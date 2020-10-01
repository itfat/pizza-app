from django.db import models

# Create your models here.

class Cart(models.Model):
    Large = 'L'
    Medium = 'M'
    Small = 'S'
    size_choices = [
        (Large,'Large'),
        (Medium, 'Medium'),
        (Small, 'Small')
    ]
    Tandoori = 'Tandoori'
    HotnSpicy = 'HotnSpicy'
    Chicken = 'Chicken'
    Pepperoni = 'Pepperoni'
    Fajita = 'Fajita'
    AllCheese = 'AllCheese'
    Margherita = 'Margherita'
    Veggie = 'Veggie'
    category_choices = [
        (Tandoori, 'Tandoori'),
        (HotnSpicy, 'Hot n Spicy'),
        (Chicken, 'Chicken'),
        (Pepperoni, 'Pepperoni'),
        (Fajita, 'Fajita'),
        (AllCheese, 'All Cheese'),
        (Margherita, 'Margherita'),
        (Veggie, 'Veggie')
    ]
    # name = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices= category_choices, default= None)
    size = models.CharField(max_length=10, choices= size_choices, default= None)
