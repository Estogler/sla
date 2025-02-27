from django.urls import path
from .views import AdrressCreate, AddressList, AddressUpdate, AddressDelete

app_name = 'endereco'

urlpatterns = [
    path('create/', AdrressCreate.as_view() , name='criar')
    path('listar/', AddressList.as_view() , name='listar')
    path('delete/<int:pk>/', AddressDelete.as_view() , name='deletar')
    path('update/<int:pk>/', AddressUpdate.as_view() , name='atualizar')
    path('detail/<int:pk>/', AddressDetail.as_view() , name='detalhar')
]