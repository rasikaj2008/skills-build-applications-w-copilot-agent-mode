import os
import django

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
    django.setup()

    from django.contrib.auth import get_user_model
    from octofit_tracker import models as octo_models

    # Delete existing data
    get_user_model().objects.all().delete()
    octo_models.Team.objects.all().delete()
    octo_models.Activity.objects.all().delete()
    octo_models.Leaderboard.objects.all().delete()
    octo_models.Workout.objects.all().delete()

    # Create Teams
    marvel = octo_models.Team.objects.create(name='Marvel')
    dc = octo_models.Team.objects.create(name='DC')

    # Create Users (Super Heroes)
    users = [
        {'email': 'ironman@marvel.com', 'username': 'IronMan', 'team': marvel},
        {'email': 'captain@marvel.com', 'username': 'CaptainAmerica', 'team': marvel},
        {'email': 'batman@dc.com', 'username': 'Batman', 'team': dc},
        {'email': 'superman@dc.com', 'username': 'Superman', 'team': dc},
    ]
    user_objs = []
    for u in users:
        user = get_user_model().objects.create_user(email=u['email'], username=u['username'], password='password', team=u['team'])
        user_objs.append(user)

    # Create Activities
    activities = [
        {'user': user_objs[0], 'type': 'Run', 'duration': 30},
        {'user': user_objs[1], 'type': 'Swim', 'duration': 45},
        {'user': user_objs[2], 'type': 'Bike', 'duration': 60},
        {'user': user_objs[3], 'type': 'Yoga', 'duration': 50},
    ]
    for a in activities:
        octo_models.Activity.objects.create(user=a['user'], type=a['type'], duration=a['duration'])

    # Create Workouts
    workouts = [
        {'name': 'Morning Cardio', 'suggestion': 'Run 5km'},
        {'name': 'Strength', 'suggestion': 'Pushups and Pullups'},
    ]
    for w in workouts:
        octo_models.Workout.objects.create(**w)

    # Create Leaderboard
    for team in [marvel, dc]:
        octo_models.Leaderboard.objects.create(team=team, score=100)

    print('octofit_db database populated with test data.')

if __name__ == '__main__':
    main()
