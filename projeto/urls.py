from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='index'),
    path('aluno/<int:id>',views.aluno, name='aluno'),
    path('del/<int:id>', views.deletar, name='deletar'),
    path('edit/<int:id>', views.editar, name='editar'),
    path('form/',views.create, name='criar'), #de views a gente pega a função (create) e tras para ca para formar uma url
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # url (link) por exemplo /admin
