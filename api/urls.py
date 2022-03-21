from django.urls import path, include

from api import views as v

urlpatterns = [
    path("dados_api/", v.dados_api, name='dados-api'),
    # PLANETA
    path("planetas/", v.planetas, name='planetas'),
    path("planeta/adicionar_planeta/", v.adicionar_planeta, name='adicionar_planeta'),
    path("planeta/atualizar_planeta/<int:id>/", v.atualizar_planeta, name='atualizar_planeta'),
    path("planeta/deletar_planeta/<int:id>/", v.deletar_planeta, name='deletar_planeta'),
    # FILME
    path("filmes/", v.filmes),
    path("planeta/adicionar_filme/", v.adicionar_filme, name='adicionar_filme'),
    path("planeta/atualizar_filme/<int:id>/", v.atualizar_filme, name='atualizar_filme'),
    path("planeta/deletar_filme/<int:id>/", v.deletar_filme, name='deletar_filme'),
    # Filmes do planeta
    path("filmes_do_planeta/<int:planeta_id>/", v.films_do_planet, name='filmes_do_planeta'),

    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]