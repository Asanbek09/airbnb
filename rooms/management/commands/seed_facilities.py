from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "This command tells me that he loves me"

    """def add_arguments(self, parser):

        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you?",
        ) """

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Pid parking off premises",
            "Elevator",
            "Parking",
            "Gym"
        ]
        for a in facilities:
            Facility.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Facilities created!"))