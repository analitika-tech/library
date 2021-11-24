from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

from backend.models import Book, Class, Student, Reservation, Issue




class Command(BaseCommand):
    help = "Creating Permission Groups"
    
    PERMISSIONS = ["add", "change", "delete", "view"]
    MODELS = [Book, Class, Student, Reservation, Issue]
    GROUPS = ["book", "class", "student", "reservation", "issue"]

    def handle(self, *args, **options):        
        for model, group in zip(self.MODELS, self.GROUPS):
            newGroup, created = Group.objects.get_or_create(name = f"{ group }-editing") # Creating the group if it doesn't exists
            
            for permission in self.PERMISSIONS:
                name = f"Can { permission.capitalize() } { model._meta.model_name }"
                codename = f"{ permission }_{ model._meta.model_name }"
                
                try:
                    model_add_permission = Permission.objects.get(codename = codename)
                    newGroup.permissions.add(model_add_permission)                        
                    self.stdout.write(f"Adding { codename } to Group: { newGroup.__str__() }")
                except Permission.DoesNotExist:
                    print(f"Permission with the name: { codename } does not exists")
                