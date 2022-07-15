from django.db import models
from datetime import datetime

class UndeleteManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)

    def get_deleted(self):
        return super().get_queryset().filter(is_deleted = True)



class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    objects = UndeleteManager()
    def delete(self):
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True
