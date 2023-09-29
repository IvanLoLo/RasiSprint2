from django.db import models
from django.utils import timezone

OPCIONES_GENERO = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

OPCIONES_ESTADO_CITA = (
    ('P', 'Programada'),
    ('C', 'Confirmada'),
    ('A', 'Atendida'),
    ('E', 'Cancelada'),
)

class Paciente(models.Model):
    cedula = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(choices=OPCIONES_GENERO, max_length=2)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"Paciente: {self.nombre} - Cédula: {self.cedula}"

class Doctor(models.Model):
    cedula = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"Dr. {self.nombre} - Cédula: {self.cedula}"

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default=None)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=None)
    especialidad = models.CharField(max_length=100)
    fecha = models.DateField(default=timezone.now)
    motivo = models.TextField(blank=True, null=True)
    estado_cita = models.CharField(choices=OPCIONES_ESTADO_CITA, max_length=20)

    def __str__(self):
        return f"Cita para {self.paciente.nombre} con el Dr. {self.doctor.nombre} el {self.fecha} - Especialidad: {self.especialidad}"
