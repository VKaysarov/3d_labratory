from django import forms
from .models import clients

class mainForm(forms.Form):
	username = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={
		'placeholder': 'Ваше имя',

		}))
	phone = forms.CharField(max_length=10, label='', widget=forms.TextInput(attrs={
		'placeholder': 'Телефон',

		}))
	email = forms.EmailField(label='', widget=forms.TextInput(attrs={
		'placeholder': 'Email',

		}))
	extra_contacts = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={
		'placeholder': 'Ваш Skype или VK',

		}))
	coment = forms.CharField(label='', widget=forms.Textarea(attrs={
		'placeholder': 'Сообщение...',

		}))

	def save(self):
		new_user = clients.objects.create(
			username=self.cleaned_data['username'],
			phone=self.cleaned_data['phone'],
			email=self.cleaned_data['email'],
			extra_contacts=self.cleaned_data['extra_contacts'],
			coment=self.cleaned_data['coment']
			)










# class comentForm(forms.Form):
# 	coment = forms.CharField(label='', widget=forms.Textarea(attrs={
# 		'placeholder': 'Сообщение...',

# 		}))

# 	def save(self):
# 		new_user = clients.objects.create(
# 			coment=self.cleaned_data['coment']
# 			)
