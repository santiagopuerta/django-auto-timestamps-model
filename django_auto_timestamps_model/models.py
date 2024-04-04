"""Auto-timestamps model"""

# Django models
from django.db import models


class AutoTimestampsModel(models.Model):
    """
    Auto-timestamps model

    Adds automatically timestamps in the creation and modification of an object.
    The class adds the following attributes to each table:
          + created_at(DateTime): Stores when the object was created.
          + updated_at(DateTime): Stores when the object was last modified.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Date Time when the object was created.'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text='Date Time when the object was last modified.'
    )

    class Meta:
        """Meta option."""

        abstract = True
