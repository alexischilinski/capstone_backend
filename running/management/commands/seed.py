import os 
from django.core.management.base import BaseCommand
from ...models import Activity

def half_marathon():
    Activity(race="half", week=1, day=1, workout_type="run", distance="3 miles").save()
    Activity(race="half", week=1, day=2, workout_type="run", distance="2 miles").save()
    Activity(race="half", week=1, day=3, workout_type="crosstrain").save()
    Activity(race="half", week=1, day=4, workout_type="rest").save()
    Activity(race="half", week=1, day=5, workout_type="run", distance="2 miles").save()
    Activity(race="half", week=1, day=6, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=1, day=7, workout_type="rest").save()

    Activity(race="half", week=2, day=1, workout_type="run", distance="3 miles").save()
    Activity(race="half", week=2, day=2, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=2, day=3, workout_type="crosstrain").save()
    Activity(race="half", week=2, day=4, workout_type="rest").save()
    Activity(race="half", week=2, day=5, workout_type="run", distance="3 miles").save()
    Activity(race="half", week=2, day=6, workout_type="run", distance="5 miles").save()
    Activity(race="half", week=2, day=7, workout_type="rest").save()

    Activity(race="half", week=3, day=1, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=3, day=2, workout_type="run", distance="3 miles").save()
    Activity(race="half", week=3, day=3, workout_type="crosstrain").save()
    Activity(race="half", week=3, day=4, workout_type="rest").save()
    Activity(race="half", week=3, day=5, workout_type="run", distance="3 miles").save()
    Activity(race="half", week=3, day=6, workout_type="run", distance="6 miles").save()
    Activity(race="half", week=3, day=7, workout_type="rest").save()

    Activity(race="half", week=4, day=1, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=4, day=2, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=4, day=3, workout_type="crosstrain").save()
    Activity(race="half", week=4, day=4, workout_type="rest").save()
    Activity(race="half", week=4, day=5, workout_type="run", distance="3 miles").save()
    Activity(race="half", week=4, day=6, workout_type="run", distance="7 miles").save()
    Activity(race="half", week=4, day=7, workout_type="rest").save()

    Activity(race="half", week=5, day=1, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=5, day=2, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=5, day=3, workout_type="crosstrain").save()
    Activity(race="half", week=5, day=4, workout_type="rest").save()
    Activity(race="half", week=5, day=5, workout_type="run", distance="3 miles").save()
    Activity(race="half", week=5, day=6, workout_type="run", distance="8 miles").save()
    Activity(race="half", week=5, day=7, workout_type="rest").save()

    Activity(race="half", week=6, day=1, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=6, day=2, workout_type="run", distance="5 miles").save()
    Activity(race="half", week=6, day=3, workout_type="crosstrain").save()
    Activity(race="half", week=6, day=4, workout_type="rest").save()
    Activity(race="half", week=6, day=5, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=6, day=6, workout_type="run", distance="6 miles").save()
    Activity(race="half", week=6, day=7, workout_type="rest").save()

    Activity(race="half", week=7, day=1, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=7, day=2, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=7, day=3, workout_type="crosstrain").save()
    Activity(race="half", week=7, day=4, workout_type="rest").save()
    Activity(race="half", week=7, day=5, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=7, day=6, workout_type="run", distance="9 miles").save()
    Activity(race="half", week=7, day=7, workout_type="rest").save()

    Activity(race="half", week=8, day=1, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=8, day=2, workout_type="run", distance="5 miles").save()
    Activity(race="half", week=8, day=3, workout_type="crosstrain").save()
    Activity(race="half", week=8, day=4, workout_type="rest").save()
    Activity(race="half", week=8, day=5, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=8, day=6, workout_type="run", distance="6 miles").save()
    Activity(race="half", week=8, day=7, workout_type="rest").save()

    Activity(race="half", week=9, day=1, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=9, day=2, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=9, day=3, workout_type="crosstrain").save()
    Activity(race="half", week=9, day=4, workout_type="rest").save()
    Activity(race="half", week=9, day=5, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=9, day=6, workout_type="run", distance="10 miles").save()
    Activity(race="half", week=9, day=7, workout_type="rest").save()

    Activity(race="half", week=10, day=1, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=10, day=2, workout_type="run", distance="6 miles").save()
    Activity(race="half", week=10, day=3, workout_type="crosstrain").save()
    Activity(race="half", week=10, day=4, workout_type="rest").save()
    Activity(race="half", week=10, day=5, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=10, day=6, workout_type="run", distance="6 miles").save()
    Activity(race="half", week=10, day=7, workout_type="rest").save()

    Activity(race="half", week=11, day=1, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=11, day=2, workout_type="run", distance="5 miles").save()
    Activity(race="half", week=11, day=3, workout_type="crosstrain").save()
    Activity(race="half", week=11, day=4, workout_type="rest").save()
    Activity(race="half", week=11, day=5, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=11, day=6, workout_type="run", distance="11 miles").save()
    Activity(race="half", week=11, day=7, workout_type="rest").save()

    Activity(race="half", week=12, day=1, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=12, day=2, workout_type="run", distance="5 miles").save()
    Activity(race="half", week=12, day=3, workout_type="crosstrain").save()
    Activity(race="half", week=12, day=4, workout_type="rest").save()
    Activity(race="half", week=12, day=5, workout_type="run", distance="4 miles").save()
    Activity(race="half", week=12, day=6, workout_type="run", distance="6 miles").save()
    Activity(race="half", week=12, day=7, workout_type="rest").save()

    Activity(race="half", week=13, day=1, workout_type="run", distance="3 miles").save()
    Activity(race="half", week=13, day=2, workout_type="run", distance="3 miles").save()
    Activity(race="half", week=13, day=3, workout_type="rest").save()
    Activity(race="half", week=13, day=4, workout_type="run", distance="3 miles").save()
    Activity(race="half", week=13, day=5, workout_type="rest").save()
    Activity(race="half", week=13, day=6, workout_type="rest").save()
    Activity(race="half", week=13, day=7, workout_type="HALF MARATHON", distance="13.1 miles").save()

def clear_data():
    """Deletes all the table data"""
    Activity.objects.all().delete()

class Command(BaseCommand):
    def handle(self, *args, **options):
        # clear_data()
        half_marathon()
        print("completed")