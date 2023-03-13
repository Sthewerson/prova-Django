from django.contrib import admin
from .models import Aluno, Professor, Disciplina, PlanoAula, Atividade, DisciplinaAluno, AtividadeAluno, Frequencia, FrequenciaAluno

class DisciplinaAlunoInline(admin.TabularInline):
    model = DisciplinaAluno

class AtividadeAlunoInline(admin.TabularInline):
    model = AtividadeAluno

class AtividadeInline(admin.TabularInline):
    model = Atividade

class DisciplinaInline(admin.TabularInline):
    model = Disciplina


class PlanoAulaInline(admin.TabularInline):
    model = PlanoAula

class FrequenciaInline(admin.TabularInline):
    model = Frequencia

class FrequenciaAlunoInline(admin.TabularInline):
    model = FrequenciaAluno

class AlunoAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'cpf', 'rg', 'matricula']
    inlines = [DisciplinaAlunoInline, AtividadeAlunoInline, FrequenciaAlunoInline]

class ProfessorAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'cpf', 'rg', 'codigo']
    inlines = [DisciplinaInline]
    

class DisciplinaAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'codigo', 'id_professor__nome']
    raw_id_fields = ['id_professor']
    inlines = [PlanoAulaInline, DisciplinaAlunoInline, AtividadeInline , FrequenciaInline ]



class AtividadeAdmin(admin.ModelAdmin):
    search_fields = ['atividade', 'tipo', 'disciplina__nome']
    raw_id_fields = ['id_disciplina', 'id_plano_aula']



class DisciplinaAlunoAdmin(admin.ModelAdmin):
    search_fields = ['id_aluno__nome', 'id_disciplina__nome']
    raw_id_fields = ['id_aluno', 'id_disciplina']
    inlines = []



class FrequenciaAdmin(admin.ModelAdmin):
    search_fields = ['id_materia__nome']
    raw_id_fields = ['id_materia']
    inlines = [FrequenciaAlunoInline,]

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(PlanoAula)
admin.site.register(Atividade, AtividadeAdmin)
admin.site.register(DisciplinaAluno, DisciplinaAlunoAdmin)
admin.site.register(AtividadeAluno)
admin.site.register(Frequencia, FrequenciaAdmin)
admin.site.register(FrequenciaAluno)
