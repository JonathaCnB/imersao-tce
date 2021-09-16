from django.db import models


class Schedule(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="schedule_user",
        blank=True,
        null=True,
    )
    service = models.ForeignKey(
        "services.Service",
        on_delete=models.CASCADE,
        related_name="schedule_service",
        verbose_name="Serviço",
    )
    date = models.DateField()
    hour = models.TimeField()
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"
        db_table = "schedule"

    @property
    def get_responsible(self):
        if self.service:
            return self.service.responsible.email

    @property
    def get_description_service(self):
        if self.service:
            return self.service.service

    def __str__(self):
        return f"{str(self.id)} - {str(self.service)}"


class Review(models.Model):
    schedule = models.ForeignKey(
        Schedule,
        verbose_name="Serviço",
        on_delete=models.SET_NULL,
        null=True,
    )
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        db_table = "review"

    def __str__(self):
        return f"{str(self.id)} - {str(self.schedule)}"
