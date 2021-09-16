from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    list_display = ["id", "email", "get_full_name", "username", "is_staff"]
    search_fields = [
        "email",
        "cnpj",
        "state",
    ]
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        (
            _("Personal info"),
            {
                "fields": (
                    "cnpj",
                    "cell_phone",
                    "service_provider",
                    "service_user",
                )
            },
        ),
        (
            "Localização",
            {
                "fields": (
                    "postal_code",
                    "address",
                    "number",
                    "complement",
                    "district",
                    "state",
                    "city",
                )
            },
        ),
    )
