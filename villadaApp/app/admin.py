from django.contrib import admin

from .models import Curso
from .models import Directivo
from .models import Preceptor
from .models import Alumno
from .models import PadreTutor
from .models import Formulario
from .models import SolicitudReunion
from .models import ComunicadoCurso
from .models import ComunicadoCiclo
from .models import ComunicadoGeneral

# Register your models here.
admin.site.register(Curso)
admin.site.register(Directivo)
admin.site.register(Preceptor)
admin.site.register(Alumno)
admin.site.register(PadreTutor)
admin.site.register(Formulario)
admin.site.register(SolicitudReunion)
admin.site.register(ComunicadoCurso)
admin.site.register(ComunicadoCiclo)
admin.site.register(ComunicadoGeneral)
