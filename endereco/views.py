from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy

from .models import Adrress
from .forms import AdrressForm, CepForm
import requests

def cep_search_view(request):
    if request.method == 'get':
        form = CepForm()

    message = ''

    if request.method == 'POST':
        form = CepForm(request.POST)
        
        cep_digitado = request.POST.get('cep')
        url = f"https://viacep.com.br/ws/{cep_digitado}/json/"
        response = request.get(url)


        if response.status_code == 200:
            dados_cep = response.json()
            if 'erro' not in dados_cep:
                message = 'CEP encontrado'
            else:
                resposta_em_json_filtrada = (
                'cep' : dados_cep['cep'],
                'logradouro' : dados_cep['logradouro'],
                'bairro' : dados_cep['bairro'],
                'localidade' : dados_cep['localidade'],
                'uf' : dados_cep['uf']
                )
                form = CepForm(resposta_em_json_filtrada)

                if form.is_valid():
                    address = form.save(commit=False)
                    address.save
                    form.save()
        else:
            message = "Erro durante a api"
    return render (request, 'endereco/cep.html', {'form': form, 'message': message})

        

class AdrressCreate(CreateView):
    model = Adrress
    form_class = AdrressForm
    context_object_name = 'CreateAdrressform'
    template_name = 'endereco/addressForm.html'
    success_url = reverse_lazy('endereco:list')

class AddressList(ListView):
    model = Adrress
    template_name = 'endereco/address_list.html'
    context_object_name = 'addresses'

    class AddressUpdate(UpdateView):
        model = Adrress
        form_class = AdrressForm
        context_object_name = 'address'
        template_name = 'endereco/addressForm.html'
        sueccess_url = reverse_lazy('endereco:listar')

    class AddressDetail(DetailView):
        model = Adrress
        template_name = 'endereco/address_confirm_delete.html'
        context_object_name = 'address'
        
    class AddressDelete(DeleteView):
        model = Adrress
        template_name = 'endereco/address_confirm_delete.html'
        success_url = reverse_lazy('endereco:listar')
        
        

   
