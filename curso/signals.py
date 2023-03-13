from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import AtividadeAluno, DisciplinaAluno

## calculando a nota da somatória do aluno 
@receiver(post_save, sender=AtividadeAluno)
def calcula_nota(sender, instance, **kwargs):

    atividades = AtividadeAluno.objects.filter(
        id_aluno=instance.id_aluno, id_atividade__id_disciplina=instance.id_atividade.id_disciplina)

    total = 0

    for atividade in atividades:
        total += atividade.nota

    DisciplinaAluno.objects.filter(id_aluno=instance.id_aluno, disciplina=instance.id_atividade.id_disciplina)
