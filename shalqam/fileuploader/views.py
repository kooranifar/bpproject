from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Album, Picture
from .forms import MainForm, AuthForm
from PIL import Image
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect


def index(request):	
    request.session.set_expiry(0)
    # request.session['name'] = 'session' + str(session_num_counter)
    
    return render (request, 'index.html')
def sharedphotos(request):
	context = {'albums' : Album.objects.all()}
	return render (request, 'sharedphotos.html', context)


def editphoto(request):	

	# instantiating an empty form
	form = MainForm()
	# print(request.session.session_key)
	return render (request, 'editphoto.html', {'form' : form})


def upload(request):

	# fetching a full form
	if request.method == 'POST':

		form = MainForm(request.POST, request.FILES)
		if form.is_valid():

			# gathering form's data:
			degree =          form.cleaned_data['degree']
			top_left_x =      form.cleaned_data['top_left_x']
			top_left_y =      form.cleaned_data['top_left_y']
			right_bottom_x =  form.cleaned_data['right_bottom_x']
			right_bottom_y =  form.cleaned_data['right_bottom_y']
			new_height =      form.cleaned_data['new_height']
			new_width =       form.cleaned_data['new_width']
			is_bw = 	      form.cleaned_data['is_bw']
			
			image = form.cleaned_data['image']
			
			is_shared = form.cleaned_data['is_shared']

			# adding data to our DB
			if not Album.objects.filter(owner = request.session.session_key).exists():
				a = Album(owner = request.session.session_key)
				a.save()
			else:
				a = Album.objects.get(owner = request.session.session_key)


			b = Picture(album = a, image = image, is_shared = is_shared, is_deleted = False)
			b.save()

			# implementing PIL shits
			img = Image.open(b.image.path)
			crop_args = (top_left_x, top_left_y, right_bottom_x, right_bottom_y)
			resize_args = (new_height, new_width)
			img = img.crop(crop_args)
			img = img.resize(resize_args)
			img = img.rotate(degree, expand = 1)
			if is_bw:
				img = img.convert('LA')

			img.save(b.image.path)

	return redirect('/')
	
def myadmin(request):
	form = AuthForm()
	return render (request, 'myadmin.html', {'form' : form, 'message' : ''})

def auth(request):
	if request.method == 'POST':
		form = AuthForm(request.POST, request.FILES)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(username=username, password=password)
			if user is not None:
			    return redirect('trueadmin/')
			else:
				return HttpResponse("sorry you're not an admin")
		

def trueadmin(request):
	return render(request, 'trueadmin.html', {'albums' : Album.objects.all()})

def adminalbum(request, album_id):
	context = {
		'sharedphotos': Album.objects.get(id = album_id).picture_set.all().filter(is_shared=True)
	}
	return render(request, 'adminalbum.html', context)

def delete(request, album_id):
	album = Album.objects.get(id = album_id)
	selected_picture = album.picture_set.get(id = request.POST['picture'])
	selected_picture.is_deleted = True
	selected_picture.save()
	context = {
		'album' : album
	}
	return redirect('/myadmin/auth/trueadmin')








