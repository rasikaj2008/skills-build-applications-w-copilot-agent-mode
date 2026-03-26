from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', suggestion='Do 10 pushups')
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=20)
        self.leaderboard = Leaderboard.objects.create(team=self.team, score=50)

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_user(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.team, self.team)

    def test_workout(self):
        self.assertEqual(self.workout.suggestion, 'Do 10 pushups')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Run')
        self.assertEqual(self.activity.duration, 20)

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.score, 50)
        self.assertEqual(self.leaderboard.team, self.team)
