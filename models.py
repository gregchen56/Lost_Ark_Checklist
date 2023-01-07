from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    session_key = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.username

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    char_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.char_name

class CharDaily(models.Model):
    char = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rested = models.PositiveSmallIntegerField(
        default=0,
        validators=[MaxValueValidator(10)]
    )
    completed = models.BooleanField()
    img_name = models.CharField(max_length=100, blank=True, editable=False)

    def __str__(self) -> str:
        return f"{self.char} - {self.name} - {self.rested}"

class CharWeekly(models.Model):
    char = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    completed = models.BooleanField()
    img_name = models.CharField(max_length=100, blank=True, editable=False)

    def __str__(self) -> str:
        return self.name

class RosterDaily(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    completed = models.BooleanField()
    img_name = models.CharField(max_length=100, blank=True, editable=False)

    def __str__(self) -> str:
        return self.name

class RosterWeekly(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    completed = models.BooleanField()
    img_name = models.CharField(max_length=100, blank=True, editable=False)

    def __str__(self) -> str:
        return self.name