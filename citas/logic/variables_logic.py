from ..models import Doctor, Paciente, Cita
from datetime import timedelta
from django.utils.dateparse import parse_date
from django.core.cache import cache

def get_citas():
    """
    Get all citas
    :return: cita object list
    """
    citas = Cita.objects.all()
    return citas

def get_citas_by_mes(mes):
    citas = -1
    is_redis_available = False
    fecha = parse_date(mes+'-01')
    try:
        citas = cache.get(mes)
        is_redis_available = True
        if citas is None: raise Exception
        print("Cache")
    except:
        print("DB")
        citas = Cita.objects.filter(fecha__year=fecha.year, fecha__month=fecha.month).count()
        citas /= 4
        if is_redis_available: cache.set(mes, citas, 60*60*24)
    return citas

def get_citas_by_fecha(fecha):
    fecha_inicial = parse_date(fecha)
    citas = -1
    is_redis_available = False
    try:
        citas = cache.get(fecha_inicial)
        is_redis_available = True
        if citas is None: raise Exception
        print("Cache")
    except:
        print("DB")
        fecha_final = fecha_inicial + timedelta(days=7)
        citas = Cita.objects.filter(fecha__gte=fecha, fecha__lt=fecha_final).count()
        if is_redis_available: cache.set(fecha_inicial, citas, 60*60*24)
    return citas

def get_citas_by_especialidad(especialidad):
    """
    Get all citas by especialidad
    :return: cita object list
    """
    citas = Cita.objects.filter(especialidad=especialidad)
    return citas

def get_cita(id):
    """
    Get cita by id
    :param id: cita id
    :return: cita object
    """
    cita = Cita.objects.get(pk=id)
    return cita

def create_cita(cita):
    """
    Create a new cita
    :param cita: cita data
    :return: cita object
    """
    cita['paciente'] = Paciente.objects.get(pk=cita['paciente'])
    cita['doctor'] = Doctor.objects.get(pk=cita['doctor'])
    cita = Cita.objects.create(**cita)
    return cita

def create_paciente(paciente):
    """
    Create a new paciente
    :param paciente: paciente data
    :return: paciente object
    """
    print(paciente)
    paciente = Paciente.objects.create(**paciente)
    return paciente

def create_doctor(doctor):
    """
    Create a new doctor
    :param doctor: doctor data
    :return: doctor object
    """
    doctor = Doctor.objects.create(**doctor)
    return doctor


def update_cita(var_pk, new_var):
    """
    Update cita by id
    :param var_pk: cita id
    :param new_var: cita data
    :return: cita object
    """
    cita = get_cita(var_pk)
    cita.especialidad = new_var['especialidad']
    cita.fecha = new_var['fecha']
    cita.motivo = new_var['motivo']
    cita.estado_cita = new_var['estado_cita']
    cita.save()
    return cita


def get_doctor():
    """
    Get all doctores
    :return: doctor object list
    """
    doctores = Doctor.objects.all()
    return doctores

def get_paciente():
    """
    Get all pacientes
    :return: paciente object list
    """
    pacientes = Paciente.objects.all()
    return pacientes