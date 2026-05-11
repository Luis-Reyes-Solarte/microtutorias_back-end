from django.db import models


# Create your models here.
class Booking(models.Model):
    """
    Modelo de reserva para una tutoría.
    Representa la relación entre un estudiante y una tutoría específica,
    junto con el estado de la reserva.

    Parameters
    ----------
    models : Class
        Super clase de django.db.models.Model que proporciona
        funcionalidades para definir modelos de datos.
    """

    STATUS_CHOICES = [
        ("PENDING", "Pendiente"),
        ("ACCEPTED", "Aceptada"),
        ("COMPLETED", "Completada"),
        ("CANCELLED", "Cancelada"),
    ]

    student = models.ForeignKey("users.User", on_delete=models.CASCADE)
    tutoring = models.ForeignKey("tutoring.TutoringAd", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
