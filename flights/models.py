from django.db import models

# Create your models here.
class Airport(models.Model):
    """

    """
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    """
    Two step creating database manipulation,
    1. Create Migrate - creating and applying how changes affect database
    2. Migrate - Applying them to the database.

    After making migrations this will create model called Flight  
    migrations folder contain instructions to make migrations

    from flights.models import Flight
    f = Flight(origin='jfk', destination='lhr', duration=415)
    f.save()
    Flight.objects.all()

    Flight.first()
    Flight.delete()

    """
    """
    origin = models.CharField(max_length=64)
    destination=models.CharField(max_length=64)
    duration=models.IntegerField()
    
    """
    """
    Airport.objects.filter(city="New York")
    Airport.objects.filter(city="New York").first()
    """
    origin=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination=models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration=models.IntegerField()
    

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination} duration is {self.duration}"
    
    def is_valid_flight(self):
        return self.origin != self.destination and self.duration > 0

class Passenger(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    flights=models.ManyToManyField(Flight,blank=True,related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"

