from gly.models import DestType

def add_to_variable_context(request):
    titletype = DestType.objects.all
    dict={'titletype':titletype}
    return dict
