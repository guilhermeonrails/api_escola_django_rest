from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaAlunosMatriculadosSerializer, ListaMatriculasAlunoSerializer, DetalhesAlunoCursoSerializer
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    # @action(detail=True, methods=['GET'])
    # def matriculas(self, request, pk):
    #     matricula_set = Matricula.objects.filter(alunos_id=pk)
    #     serializer = MatriculaSerializer(matricula_set, many=True)
    #     return Response(serializer.data)

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os Cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo as Matrículas"""
    queryset = Matricula.objects.all().select_related('alunos', 'cursos')
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    """Exibindo todas as matrículas de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(alunos_id=self.kwargs["pk"])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    """Exibindo todos alunos e alunas de um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(cursos_id=self.kwargs["pk"])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class DetalhesAlunoCurso(generics.ListAPIView, generics.UpdateAPIView):
    """Exibindo detalhes de um aluno e um curso matriculado"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(alunos_id=self.kwargs["aluno_id"], cursos_id=self.kwargs["curso_id"] )
        return queryset
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]