from django.http import HttpResponseRedirect
from django.shortcuts import render
import pandas as pd
from keras import backend as K
from Proyecto_RNP_2019_FN import rnp
from pandocfilters import Null
from pyparsing import empty
from Proyecto_RNP_2019_FN import rnp
from Proyecto_RNP_2019_FN import settings
from Proyecto_RNP_2019_FN import rnp
# Create your views here.
def predictor(request):
    return render(request, 'predictor/predictor.html')




def rtaPrediccion(request):
    if request.method == 'GET':
        return render(request, 'predictor/rtaPrediccion.html')
    elif (request.method == 'POST'):
        modelo_cargado = settings.cargarModelo()
        programa = int(request.POST['programa'])
        periodoIngreso = int(request.POST['periodoIngreso'])
        periodoFinal = int(request.POST['periodoFinal'])
        ciudadResidencia = int(request.POST['ciudadResidencia'])
        ciudadOrigen = int(request.POST['ciudadOrigen'])

        if (request.POST['sexo'] == "F"):
            sexoF = int(1)
            sexoM = int(0)
        else:
            sexoF = int(0)
            sexoM = int(1)

        if (request.POST['modalidad'] == "D"):
            jorDiurna = int(1)
            jorExtendida = int(0)
        else:
            jorDiurna = int(0)
            jorExtendida = int(1)

        edad = int(request.POST['edad'])
        promedioActual = float(request.POST['promedioUltimoCursado'])
        promedioAcumulado = float(request.POST['promedioAcumulado'])

        print("programa: ", programa)
        print("periodoIngreso: ", periodoIngreso)
        print("periodoFinal: ", periodoFinal)
        print("ciudadResidencia: ", ciudadResidencia)
        print("ciudadOrigen: ", ciudadOrigen)
        print("sexoF: ", sexoF)
        print("sexoM: ", sexoM)
        print("jorDiurna: ", jorDiurna)
        print("jorExtendida: ", jorExtendida)
        print("edad: ", edad)
        print("promedioActual: ", promedioActual)
        print("promedioAcumulado: ", promedioAcumulado)

        # CON 12 ENTRADAS
        dicValoresIngresados = {'ID_PROGRAMA': [programa], 'ID_PERIODO_INGRESO': [periodoIngreso],
                                'ID_PERIODO_FINAL': [periodoFinal], 'JORNADA_DIURNA': [jorDiurna],
                                'JORNADA_EXTENDIDA': [jorExtendida], 'SEXO_F': [sexoF],
                                'SEXO_M': [sexoM], 'CIUDAD_ORIGEN_MAP': [ciudadOrigen],
                                'CIUDAD_RESIDENCIA_MAP': [ciudadResidencia], 'EDAD': [edad],
                                'PROMEDIO_ACUMULADO': [promedioAcumulado],
                                'PROMEDIO_SEMESTRE_FINAL': [promedioActual]}

        data = pd.DataFrame(dicValoresIngresados)
        predictions = modelo_cargado.predict(data, batch_size=32, verbose=1, steps=None)

        # limpiar session en keras
        K.clear_session()
        resultado = int(predictions[0][0] * 100)
        msj = ""
        if (resultado <= 40):
            if (resultado <= 10):
                resultado = 10
            icono = "bien"
            clase = "progress-bar progress-bar-striped bg-success"
            msj = "¡Tranquilo, actualmente no hay riesgo de deserción!"
            return render(request, 'predictor/rtaPrediccion.html', {'resultado': resultado, 'clase': clase, 'icono': icono, 'msj':msj})
        elif (resultado >= 41 and resultado <= 80):
            clase = "progress-bar progress-bar-striped bg-warning"
            icono = "adv"
            msj = "¡Atención, por el momento parece no haber riesgo de deserción!"
            return render(request, 'predictor/rtaPrediccion.html', {'resultado': resultado, 'clase': clase, 'icono': icono, 'msj':msj})
        elif (resultado >= 81):
            clase = "progress-bar progress-bar-striped bg-danger"
            icono = "pel"
            msj = "¡Cuidado, Posible desertor!"
            return render(request, 'predictor/rtaPrediccion.html', {'resultado': resultado, 'clase': clase, 'icono': icono, 'msj':msj})



def torta(request):
    return render(request, 'predictor/graf_torta.html')

def barras(request):
    return render(request, 'predictor/graf_barras.html')

def linea(request):
    return render(request, 'predictor/graf_area.html')