from django.db import models
from django.db.models.indexes import Index
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Suggestion(models.Model):
    s_id = models.AutoField(primary_key=True)
    suggestion = models.TextField(_('Sugerencia'),max_length=520)

    