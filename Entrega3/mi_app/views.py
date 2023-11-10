from django.shortcuts import render, redirect
from .forms import ClienteForm, ProveedorForm, PedidoForm
from .models import Cliente, Proveedor, Pedido

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear-cliente')
    else:
        form = ClienteForm()
    return render(request, 'mi_app/crear_cliente.html', {'form': form})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear-proveedor')
    else:
        form = ProveedorForm()
    return render(request, 'mi_app/crear_proveedor.html', {'form': form})

def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear-pedido')
    else:
        form = PedidoForm()
    return render(request, 'mi_app/crear_pedido.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        pass
    return render(request, 'mi_app/buscar.html')