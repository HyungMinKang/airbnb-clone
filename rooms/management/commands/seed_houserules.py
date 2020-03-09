from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "This command creates HouseRules"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you want me to tell you that I love ?"
    #     )

    def handle(self, *args, **options):
        house_rules = [
            "No Parties or Events",
            "Only registered Guests",
            "No eating or drinking in the bedrooms",
            "Do the dishes",
            "No smoking",
            "Fake Tan = BYO Sheets",
            "Turn of lights and AC/Heating when out of the property",
            "No Pets",
            "State check in and check out times",
            "Noise curfew",
            "Lost Key fee",
        ]
        for h in house_rules:
            HouseRule.objects.create(name=h)

        self.stdout.write(self.style.SUCCESS(f"{len(house_rules)} HouseRules created!"))
