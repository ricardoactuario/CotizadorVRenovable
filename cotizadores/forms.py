from django import forms


Opciones = [
    ('Si', 'Si'), 
    ('No', 'No'), 
]
Opciones2 = [
    ('Mensual', 'Mensual'), 
    ('Trimestral', 'Trimestral'),
    ('Semestral', 'Semestral'), 
    ('Anual', 'Anual'),  
]

class C_Intermediario2(forms.Form):
    Nombre = forms.CharField(label="Nombre de Empresa:", max_length=200, required=False)
    Int = forms.CharField(label="Intermediario:", max_length=200, required=False)
    Tel = forms.CharField(label="Teléfono:", max_length=200, required=False)
    Correo = forms.CharField(label="Correo electrónico:", max_length=200, required=False)
    Id = forms.CharField(label="Código de agente:", max_length=200, required=False) 
    
class form_CotizadorTAR(forms.Form):
    Sol = forms.CharField(label="Solicitante:", max_length=200)
    Nac = forms.CharField(label="Fecha de Nacimiento (YYYY/MM/DD):", max_length=200)
    Sum = forms.CharField(label="Suma Asegurada (Entre $5,000 - $10,000,000):", max_length=200)
    Mail = forms.CharField(label="Correo Electrónico", max_length=200, required=False)
    Cellphone = forms.CharField(label="Celular:", max_length=200)
    Titulo = forms.CharField(label="", initial="Coberturas Opcionales:", widget=forms.Textarea(attrs={'readonly':'readonly', 'class': 'Coberturas'})) 
    Ben1 = forms.ChoiceField(label="Invalidez Total y Permanente", choices=Opciones, widget=forms.Select(attrs={'id':'ben1'}))
    Ben2 = forms.ChoiceField(label="Fallecimiento Accidental", choices=Opciones, widget=forms.Select(attrs={'id':'ben2'}))