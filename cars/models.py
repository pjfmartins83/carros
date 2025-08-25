from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField("Modelo", max_length=200)
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name="car_brand", verbose_name="Marca"
    )
    factory_year = models.IntegerField("Ano de Fabricação", blank=True, null=True)
    model_year = models.IntegerField("Ano do Modelo", blank=True, null=True)
    plate = models.CharField("Placa", max_length=10, blank=True, null=True)
    value = models.DecimalField(
        "Valor (R$)", max_digits=12, decimal_places=2, blank=True, null=True
    )
    photo = models.ImageField("Foto", upload_to="cars/", blank=True, null=True)
    bio = models.TextField("Descrição", blank=True, null=True)

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"

    def __str__(self):
        return self.model


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.cars_count} - {self.cars_value}"
