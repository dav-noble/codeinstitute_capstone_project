from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Plan(models.Model):
    EMPTY = "EM"
    GREAT_HALL = "GH"
    MARKET = "MK"
    MONASTERY = "MN"
    LONGPHORT = "LP"
    PRIMARY = [
        (EMPTY, 'Empty'),
        (GREAT_HALL, 'Great Hall'),
        (MARKET, 'Market'),
        (MONASTERY, 'Monastery'),
        (LONGPHORT, 'Longphort'),
    ]

    BENEDICTINE_ABBEY = "BA"
    FARM = "FM"
    ORCHARD = "OR"
    PASTURE = "PA"
    HUNTING = "HN"
    FISHING = "FI"
    WOOD = "WD"
    GOLD = "GD"
    TIN = "TN"
    IRON = "IN"
    SILVER = "SL"
    COPPER = "CP"
    LEAD = "LD"
    CLOTH = "CL"
    SALT = "SA"
    BEACH_PORT = "BP"
    POTTERY = "PT"
    SECONDARY = [
        (EMPTY, "Empty"),
        (BENEDICTINE_ABBEY, "Benedictine Abbey"),
        (FARM, "Farm"),
        (ORCHARD, "Orchard"),
        (PASTURE, "Pasture"),
        (HUNTING, "Hunting"),
        (FISHING, "Fishing"),
        (WOOD, "Wood"),
        (GOLD, "Gold"),
        (TIN, "Tin"),
        (IRON, "Iron"),
        (SILVER, "Silver"),
        (COPPER, "Copper"),
        (LEAD, "Lead"),
        (CLOTH, "Cloth"),
        (SALT, "Salt"),
        (BEACH_PORT, "Beach Port"),
        (POTTERY, "Pottery"),
    ]

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="province_plans"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    primary_building = models.CharField(max_length=2, choices=PRIMARY, default=EMPTY)
    secondary_building_1 = models.CharField(max_length=2, choices=SECONDARY, default=EMPTY)
    secondary_building_2 = models.CharField(max_length=2, choices=SECONDARY, default=EMPTY)
    secondary_building_3 = models.CharField(max_length=2, choices=SECONDARY, default=EMPTY)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | created by {self.author}"