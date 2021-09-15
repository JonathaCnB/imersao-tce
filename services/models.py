from django.db import models
from users.models import User


class Service(models.Model):
    service = models.CharField("Serviço", max_length=255)
    description = models.TextField()
    responsible = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_service",
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"
        db_table = "service"

    def __str__(self):
        return f"{str(self.id)} - {str(self.service)}"
