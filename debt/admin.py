from django.contrib import admin
from debt.models import Debt, DebtAccount, PeriodicDebt

admin.site.register(Debt)
admin.site.register(PeriodicDebt)
admin.site.register(DebtAccount)
# Register your models here.
