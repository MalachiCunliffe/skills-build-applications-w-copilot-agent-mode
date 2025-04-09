from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com", name="Test User", age=25)

    def test_user_creation(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.age, 25)

class TeamModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="teamuser@example.com", name="Team User", age=30)
        self.team = Team.objects.create(name="Test Team")
        self.team.members.add(self.user)

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Test Team")
        self.assertIn(self.user, self.team.members.all())

class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(name="Running", description="Running activity")

    def test_activity_creation(self):
        self.assertEqual(self.activity.name, "Running")
        self.assertEqual(self.activity.description, "Running activity")

class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="leaderboarduser@example.com", name="Leaderboard User", age=28)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.user, self.user)
        self.assertEqual(self.leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="workoutuser@example.com", name="Workout User", age=35)
        self.activity = Activity.objects.create(name="Cycling", description="Cycling activity")
        self.workout = Workout.objects.create(user=self.user, activity=self.activity, duration=60)

    def test_workout_creation(self):
        self.assertEqual(self.workout.user, self.user)
        self.assertEqual(self.workout.activity, self.activity)
        self.assertEqual(self.workout.duration, 60)