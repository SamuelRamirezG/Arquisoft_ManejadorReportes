from generarreportes.models import Reporte
from generarreportes.models import Pago
def get_reporte(rep_pk):
    reporte = Reporte.objects.all()
    return reporte 


