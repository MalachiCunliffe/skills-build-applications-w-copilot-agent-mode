from djongo import models

class User(models.Model):
    id = models.ObjectIdField(primary_key=True)  # Use ObjectIdField for MongoDB compatibility
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True)  # Use ObjectIdField for MongoDB compatibility
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True)  # Use ObjectIdField for MongoDB compatibility
    name = models.CharField(max_length=100)
    description = models.TextField()

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True)  # Use ObjectIdField for MongoDB compatibility
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True)  # Use ObjectIdField for MongoDB compatibility
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    duration = models.IntegerField()