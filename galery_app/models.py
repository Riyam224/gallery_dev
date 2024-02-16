from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Gallery(models.Model):
    title =  models.CharField(_("title"), max_length=50)
    image = models.ImageField(_("image"), upload_to='images/', blank=True, null=True)


    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Gallerys")

    def __str__(self):
        return self.title

  