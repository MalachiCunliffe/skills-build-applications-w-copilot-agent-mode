from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(id=1, email="user1@example.com", name="User One", age=20)
        user2 = User.objects.create(id=2, email="user2@example.com", name="User Two", age=25)

        # Create test teams
        team1 = Team.objects.create(id=1, name="Team Alpha")
        team1.members.set([user1, user2])

        # Create test activities
        activity1 = Activity.objects.create(id=1, name="Running", description="Running activity")
        activity2 = Activity.objects.create(id=2, name="Cycling", description="Cycling activity")

        # Create test leaderboard entries
        Leaderboard.objects.create(id=1, user=user1, score=100)
        Leaderboard.objects.create(id=2, user=user2, score=150)

        # Create test workouts
        Workout.objects.create(id=1, user=user1, activity=activity1, duration=30)
        Workout.objects.create(id=2, user=user2, activity=activity2, duration=45)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))