from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.br.models import BRCNPJField, BRPostalCodeField, BRStateField


class User(AbstractUser):
    cnpj = BRCNPJField(
        "CNPJ",
        default="",
        blank=True,
        null=True,
    )
    postal_code = BRPostalCodeField(
        "CEP",
        default="",
    )
    state = BRStateField(
        "Estado",
        default="",
    )
    address = models.CharField(
        "Endereço",
        max_length=250,
        default="",
    )
    cell_phone = models.CharField(
        "Telefone Celular",
        max_length=250,
        default="",
        blank=True,
    )
    number = models.CharField(
        "Número",
        max_length=10,
        default="",
    )
    complement = models.CharField(
        "Complemento",
        max_length=20,
        default="",
        blank=True,
        null=True,
    )
    district = models.CharField(
        "Bairro",
        max_length=100,
        default="",
    )
    city = models.CharField(
        "Cidade",
        max_length=100,
        default="",
    )
    service_provider = models.BooleanField(default=False)
    service_user = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "user"

    def __str__(self):
        return f"{str(self.id)} - {str(self.email)}"
