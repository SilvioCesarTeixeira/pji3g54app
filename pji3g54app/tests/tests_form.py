from django.test import TestCase
from ..forms import CadastroForm

class CadastroFormTestCase(TestCase):

    def test_cadastro_form_is_valid(self):
        form = CadastroForm(data={
            'inputEmpresa' : "Empresa",
            'inputCNPJ' : "123456789100023",
            'inputEmail' : "teste@teste.com",
            'inputTel' : "1234567890",
            'inputCel' : "12987456321",
            'inputAddress' : "Endereço 1",
            'inputNumber' : 1,
            'inputAddress2' : "Endereço 2",
            'inputCEP' : "12345678",
            'inputCity' : "Cidade",
            'inputEstado' : "EE",
            'inputTipo' : 'True'
        })
        self.assertTrue(form.is_valid())

