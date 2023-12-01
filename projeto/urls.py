from django.urls import path, include #caminho de importação django.urls, inclua
from . import views # é uma instrução de importação comum em uma aplicação Django, particularmente dentro do arquivo `urls.py'
from django.conf import settings #é usada para importar o módulo de configurações do framework Django. O módulo `settings` contém várias definições de configuração para um projeto Django e permite acessar e modificar essas configurações programaticamente. 
from django.conf.urls.static import static #está importando a função `static` do `django.conf.urls`


urlpatterns = [
    path('',views.index, name='index'),
    path('aluno/<int:id>',views.aluno, name='aluno'),  #int:id - identidade
    path('del/<int:id>', views.deletar, name='deletar'), #caminho em uma configuração de URL do Django
    path('edit/<int:id>', views.editar, name='editar'), #caminho em uma configuração de URL do Django
    path('form/',views.create, name='criar'), #de views a gente pega a função (create) e tras para ca para formar uma url. 
    path('accounts/',include('django.contrib.auth.urls')), #caminho para o login 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # url (link) por exemplo /admin


