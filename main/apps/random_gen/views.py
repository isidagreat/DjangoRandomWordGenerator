from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
	if 'attempt' not in request.session:
		request.session['attempt'] = 1
	else:
		request.session['attempt'] += 1

	response = {
		"rword" : get_random_string(length=14)
	}
	return render(request, "index.html", response)

def reset(request):
	request.session.clear()
	return redirect(index)