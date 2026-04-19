from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from gestion.views import dashboard, ocupar_plaza, liberar_plaza, reporte_diario

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rutas de login y logout (predeterminadas de Django)
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # Rutas de Danny Park
    path('', dashboard, name='dashboard'),
    path('ocupar/<int:plaza_id>/', ocupar_plaza, name='ocupar'),
    path('liberar/<int:plaza_id>/', liberar_plaza, name='liberar'),
    path('reporte/', reporte_diario, name='reporte'),
]