from django.core.management.base import BaseCommand
from ...models import Trombinoscope, Project
class Command(BaseCommand):

	def handle(self, *args, **options):
		""" Generate thumnails for some models """
		for person in Trombinoscope.objects.all():
			person.photo.create_thumbnails()
		for project in Project.objects.all():
			project.image.create_thumbnails()

# EOF
