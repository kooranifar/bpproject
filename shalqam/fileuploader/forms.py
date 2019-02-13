from django import forms
from PIL import Image
from django.core.files import File
from .models import Picture

class MainForm(forms.Form):

	degree = forms.IntegerField(label = 'degree')
	top_left_x = forms.IntegerField(label = 'top_left_x')
	top_left_y = forms.IntegerField(label = 'top_left_y')
	right_bottom_x = forms.IntegerField(label = 'right_bottom_x')
	right_bottom_y = forms.IntegerField(label = 'right_bottom_y')
	new_width = forms.IntegerField(label = 'new_width')
	new_height = forms.IntegerField(label = 'new_height')
	is_bw = forms.BooleanField(label = 'turn to gray scale?', initial = False, required = False) 	
	image = forms.ImageField()
	is_shared = forms.BooleanField(label = 'share it?', initial = False, required = False)

class AuthForm(forms.Form):
    username = forms.CharField(label = 'username', max_length = 200)
    password = forms.CharField(label = 'password', max_length = 200, widget = forms.PasswordInput)





