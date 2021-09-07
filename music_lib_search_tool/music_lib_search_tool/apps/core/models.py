from urllib.parse import urlparse, urlunparse
import uuid
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import FieldError
import datetime

class UrlBase(models.Model):
    """
    A replacement for get_absolute_url()
    Models extending this mixin should have either get_url or get_url_path implemented.
    http://code.djangoproject.com/wiki/ReplacingGetAbsoluteUrl
    """
    class Meta:
        abstract = True

    def get_url(self):
        if hasattr(self.get_url_path, "dont_recurse"):
            raise NotImplementedError
        try:
            path = self.get_url_path()
        except NotImplementedError:
            raise
        return settings.WEBSITE_URL + path
    get_url.dont_recurse = True

    def get_url_path(self):
        if hasattr(self.get_url, "dont_recurse"):
            raise NotImplementedError
        try:
            url = self.get_url()
        except NotImplementedError:
            raise
        bits = urlparse(url)
        return urlunparse(("", "") + bits[2:])
    get_url_path.dont_recurse = True

    def get_absolute_url(self):
        return self.get_url()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print("save() from UrlBase called")

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        print("delete() from UrlBase called")

    def test(self):
        print("test() from UrlBase called")

class CreationModificationDateBase(models.Model):
    """
    Abstract base class with a creation and modification date and time
    """

    created = models.DateTimeField(
        _("Creation Date and Time"),
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        _("Modification Date and Time"),
        auto_now=True,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print("save() from CreationModificationDateBase called")
    save.alters_data = True

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        print("delete() from CreationModificationDateBase called")



class UuidBase(models.Model):
    """
    Abstract base class with a UUID
    """

    uuid = models.UUIDField(
        _("Object UUID"),
        default=uuid.uuid4,
        db_index=True,
        unique=True
    )

    class Meta:
        abstract = True

class ArchiveBase(models.Model):
    """
    Abstract base class with archive system
    """

    archived = models.BooleanField(default=False)
    archived_datetime = models.DateTimeField(
        blank=True,
        null=True
    )

    def archive(self):
        self.archived = True
        self.archived_datetime = datetime.datetime.now()

    class Meta:
        abstract = True