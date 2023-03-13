from rest_framework import viewsets
from .models import Aluno, Professor, Disciplina, PlanoAula, Atividade, DisciplinaAluno, AtividadeAluno, Frequencia, FrequenciaAluno
from .serializers import AlunoSerializer, ProfessorSerializer, DisciplinaSerializer, PlanoAulaSerializer, AtividadeSerializer, DisciplinaAlunoSerializer, AtividadeAlunoSerializer, FrequenciaSerializer, FrequenciaAlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class PlanoAulaViewSet(viewsets.ModelViewSet):
    queryset = PlanoAula.objects.all()
    serializer_class = PlanoAulaSerializer

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer

class DisciplinaAlunoViewSet(viewsets.ModelViewSet):
    queryset = DisciplinaAluno.objects.all()
    serializer_class = DisciplinaAlunoSerializer

class AtividadeAlunoViewSet(viewsets.ModelViewSet):
    queryset = AtividadeAluno.objects.all()
    serializer_class = AtividadeAlunoSerializer

class FrequenciaViewSet(viewsets.ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer

class FrequenciaAlunoViewSet(viewsets.ModelViewSet):
    queryset = FrequenciaAluno.objects.all()
    serializer_class = FrequenciaAlunoSerializer
