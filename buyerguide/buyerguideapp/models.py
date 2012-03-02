from django.db import models


class Group(models.Model):
   name = models.CharField(max_length=30)
   email = models.CharField(max_length=50)

   def __unicode__(self):
      return self.name

   class Meta:
      ordering = ['name']

class Publication(models.Model):
   name = models.CharField(max_length=30)
   description = models.TextField()
   group = models.ForeignKey(Group)

   def __unicode__(self):
      return self.name

   class Meta:
      ordering = ['name']

