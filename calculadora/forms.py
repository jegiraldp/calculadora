from django import forms

class formularioCal(forms.Form):
	numeroUno = forms.IntegerField(label="Número uno")
	numeroDos = forms.IntegerField(label="Número Dos")