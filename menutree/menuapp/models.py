from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def children(self):
        return self.menu_set.all()

    def get_elder_ids(self):
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.id]
        else:
            return []
