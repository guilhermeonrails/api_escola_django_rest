from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ("B", "Básico"),
        ("I", "Intermediário"),
        ("A", "Avançado")
    )
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao

class Matricula(models.Model):
    PERIODOS = (
        ("M", "Matutino"),
        ("V", "Vespertino"),
        ("N", "Noturno")
    )
    alunos = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    cursos = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODOS, blank=False, null=False, default='M')

    def __str__(self):
        return '{} - {}'.format(self.alunos, self.cursos) 