from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from gum.models import CreatePost

   
class Command(BaseCommand):
    help = 'Create posts from Faker'

    def add_arguments(self, parser) -> str:
        parser.add_argument('argm',type=int)
   
    
    def handle(self, *args, **options) :
        fake = Faker()
        num = options['argm']
        for i in range(int(num)):
            CreatePost.objects.create(
                title=fake.sentence(),
                message=fake.text(),
                pub_date=timezone.now(),
                author=fake.name())
        return "Success" 
 