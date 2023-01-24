from django import forms   # se agrego este script para agregar forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200,widget=forms.TextInput(attrs={"class":"input"}))
    description = forms.CharField(label="Descripcion de la tarea",widget=forms.Textarea )

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del Proyecto", max_length=200,widget=forms.TextInput(attrs={"class":"input"}))
    