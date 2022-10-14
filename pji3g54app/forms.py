from django.forms import ModelForm
from pji3g54app.models import Cadastro


class CadastroForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = ['inputEmpresa', 'inputCNPJ', 'inputEmail', 'inputTel', 'inputCel', 'inputAddress', 'inputNumber', 'inputAddress2', 'inputCEP', 'inputCity', 'inputEstado', 'inputTipo']
