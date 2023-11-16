from ..models import Doctor, Paciente, Cita
from datetime import timedelta, datetime
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
    except:
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
    except:
        fecha_final = fecha_inicial + timedelta(days=7)
        citas = Cita.objects.filter(fecha__gte=fecha, fecha__lt=fecha_final).count()
        if is_redis_available: cache.set(fecha_inicial, citas, 60*60*24)
    return citas

def get_citas_by_especialidad(especialidad):
    """
    Get all citas by especialidad
    :return: cita object list
    """
    citas = Cita.objects.filter(especialidad=especialidad.capitalize())
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
    date_obj = datetime.strptime(cita['fecha'], "%Y-%m-%d")
    cita['fecha'] = date_obj.date()
    cita = Cita.objects.create(**cita)
    return cita

def create_paciente(paciente):
    """
    Create a new paciente
    :param paciente: paciente data
    :return: paciente object
    """
    date_obj = datetime.strptime(paciente['fecha_nacimiento'], "%Y-%m-%d")
    paciente['fecha_nacimiento'] = date_obj.date()
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


def get_doctors():
    """
    Get all doctores
    :return: doctor object list
    """
    doctores = Doctor.objects.all()
    return doctores

def get_doctor(id):
    """
    Get doctor by id
    :param id: doctor id
    :return: doctor object
    """
    doctor = Doctor.objects.get(pk=id)
    return doctor

def get_pacientes():
    """
    Get all pacientes
    :return: paciente object list
    """
    pacientes = Paciente.objects.all()
    return pacientes

def get_paciente(id):
    """
    Get paciente by id
    :param id: paciente id
    :return: paciente object
    """
    paciente = Paciente.objects.get(pk=id)
    return paciente
