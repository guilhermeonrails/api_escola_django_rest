from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id','nome', 'rg', 'cpf', 'data_nascimento', 'ativo']

class CursoSerializer(serializers.ModelSerializer):
    nivel = serializers.SerializerMethodField()
    class Meta:
        model = Curso
        fields = '__all__'
    def get_nivel(self,obj):
        return obj.get_nivel_display()

class MatriculaSerializer(serializers.ModelSerializer):
    # aluno_nome = serializers.ReadOnlyField(source='alunos.nome')
    # curso_nome = serializers.ReadOnlyField(source='cursos.descricao')
    # periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        exclude = []
    def get_periodo(self,obj):
        return obj.get_periodo_display()

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso_nome = serializers.ReadOnlyField(source='cursos.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso_nome', 'periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='alunos.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']