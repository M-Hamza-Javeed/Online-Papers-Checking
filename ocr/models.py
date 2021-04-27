from django.db import models


class OCRFILES(models.Model):
    file = models.FileField(blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} ({})'.format(self.file)
