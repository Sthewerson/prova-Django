from django.db import models


class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=8)
    matricula = models.CharField(max_length=8)
    telefone = models.CharField(max_length=11)
    email = models.CharField(max_length=255)

    class Meta:
        db_table = 'Aluno'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.nome


class Professor(models.Model):
    id_professor = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=8)
    codigo = models.CharField(max_length=8)
    email = models.CharField(max_length=255)
    telefone = models.CharField(max_length=11)

    class Meta:
        db_table = 'Professor'
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    id_disciplina = models.AutoField(primary_key=True)
    id_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=7)
    carga_horaria = models.IntegerField()
    ementa = models.TextField()

    class Meta:
        db_table = 'Diciplina'
        verbose_name = 'Diciplina'
        verbose_name_plural = 'Diciplinas'

    def __str__(self):
        return self.nome


class PlanoAula(models.Model):
    id_plano_aula = models.AutoField(primary_key=True)
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tema_aula = models.CharField(max_length=255)
    conteudo = models.TextField()
    METODO_CHOICES = (
        ('Teorica', 'Teorica'),
        ('Pratica', 'Pratica')
    )
    metodo = models.CharField(max_length=50, choices=METODO_CHOICES)
    dia = models.DateField()

    class Meta:
        db_table = 'PlanoAula'
        verbose_name = "Plano de aula"
        verbose_name_plural = 'Planos de aula'


class Atividade(models.Model):
    id_atividade = models.AutoField(primary_key=True)
    atividade = models.TextField()
    TIPO_CHOICES = (
        ('sala', 'Atividade de sala'),
        ('casa', 'Atividade de casa'),
        ('prova', 'Prova'),
    )
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    data_postagem = models.DateField()
    data_entrega = models.DateField()
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    id_plano_aula = models.ForeignKey(PlanoAula, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Atividades'
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return f'{self.tipo} - {self.atividade} - {self.id_disciplina.nome}'


class DisciplinaAluno(models.Model):
    id_matricula = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    id_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nota = models.FloatField(default=0.0)

    class Meta:
        db_table = 'DisciplinaAluno'
        verbose_name = 'Disciplina Aluno'
        verbose_name_plural = 'Disciplinas dos Alunos'

    def __str__(self):
        return f'{self.id_aluno.nome} - {self.id_aluno.nome}'


class AtividadeAluno(models.Model):
    id = models.AutoField(primary_key=True)
    id_atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nota = models.FloatField()

    class Meta:
        db_table = 'AtividadeAluno'
        verbose_name = 'Atividade do Aluno'
        verbose_name_plural = 'Atividades dos Alunos'

    def __str__(self):
        return f'{self.id_aluno.nome} - { self.id_atividade}'


class Frequencia(models.Model):
    id_frequencia = models.AutoField(primary_key=True)
    id_materia = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    dia = models.DateField()

    def __str__(self):
        return f"{self.id_materia.nome} - {self.dia}"


class FrequenciaAluno(models.Model):
    id = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    id_frequencia = models.ForeignKey(Frequencia, on_delete=models.CASCADE)
    presenca = models.CharField(max_length=1, default='T')

    class Meta:
        db_table = 'FrequenciaAluno'
        verbose_name = 'Frequencia de aluno'
        verbose_name_plural = 'Frequências de alunos'

    def __str__(self):
        return f"{self.id_aluno.nome} - {self.id_frequencia.id_materia.nome} - {self.id_frequencia.dia} - {self.presenca}"
