from django.core.management.base import BaseCommand
from faker import Faker
from gum.models import CreateUsers

   
class Command(BaseCommand):
    help = 'Create users from Faker'
   
    def add_arguments(self, parser) -> None:
        parser.add_argument('argm',type=int)



    def handle(self, *args, **options) :
        fake = Faker()
       
        nam = options['argm']
        for i in range(nam):
            CreateUsers.objects.create(name=fake.name(),
            password=fake.password(),mail=fake.email())
        return "Success"
 