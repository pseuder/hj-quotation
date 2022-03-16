from django.db import models

class User(models.Model):#OK
    account = models.TextField(blank=True, null=False)
    password = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.account