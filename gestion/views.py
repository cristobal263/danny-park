from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from .models import Plaza, RegistroCobro

@login_required
def dashboard(request):
    # Obtenemos plazas ordenadas
    plazas = Plaza.objects.all().order_by('identificador')
    
    # Calculamos el total recaudado hoy
    hoy = timezone.now().date()
    total_dia = RegistroCobro.objects.filter(hora_salida__date=hoy).aggregate(Sum('total_pagado'))['total_pagado__sum'] or 0
    
    return render(request, 'index.html', {
        'plazas': plazas, 
        'total_dia': total_dia
    })

@login_required
def ocupar_plaza(request, plaza_id):
    if request.method == "POST":
        plaza = get_object_or_404(Plaza, id=plaza_id)
        patente = request.POST.get('patente')
        
        plaza.ocupada = True
        plaza.patente = patente.upper()
        plaza.hora_ingreso = timezone.now()
        plaza.save()
        
    return redirect('dashboard')

@login_required
def liberar_plaza(request, plaza_id):
    plaza = get_object_or_404(Plaza, id=plaza_id)
    
    if plaza.ocupada:
        ahora = timezone.now()
        diferencia = ahora - plaza.hora_ingreso
        
        minutos = max(int(diferencia.total_seconds() / 60), 1)
        total = minutos * 35
        
        RegistroCobro.objects.create(
            identificador_plaza=plaza.identificador,
            patente=plaza.patente,
            hora_ingreso=plaza.hora_ingreso,
            minutos=minutos,
            total_pagado=total
        )
        
        plaza.ocupada = False
        plaza.patente = None
        plaza.hora_ingreso = None
        plaza.save()
        
    return redirect('dashboard')

@login_required
def reporte_diario(request):
    hoy = timezone.now().date()
    cobros = RegistroCobro.objects.filter(hora_salida__date=hoy).order_by('-hora_salida')
    total_recaudado = sum(c.total_pagado for c in cobros)
    
    return render(request, 'reporte.html', {
        'cobros': cobros,
        'total': total_recaudado,
        'fecha': hoy
    })