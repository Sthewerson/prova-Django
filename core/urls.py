"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from curso import views as cursoViews

cursosRoutes = routers.DefaultRouter()

cursosRoutes.register(r'alunos', cursoViews.AlunoViewSet)
cursosRoutes.register(r'professor', cursoViews.ProfessorViewSet)
cursosRoutes.register(r'disciplina', cursoViews.DisciplinaAlunoViewSet)
cursosRoutes.register(r'planoAula', cursoViews.PlanoAulaViewSet)
cursosRoutes.register(r'atividade', cursoViews.AtividadeViewSet)
cursosRoutes.register(r'disciplinaAluno', cursoViews.DisciplinaAlunoViewSet)
cursosRoutes.register(r'atividadeAluno', cursoViews.AtividadeAlunoViewSet)
cursosRoutes.register(r'frequencia', cursoViews.FrequenciaViewSet)
cursosRoutes.register(r'frequenciaAluno', cursoViews.FrequenciaAlunoViewSet)


urlpatterns = [
    path('cursos/', include(cursosRoutes.urls),name='views'),
    path('admin/', admin.site.urls),
]
