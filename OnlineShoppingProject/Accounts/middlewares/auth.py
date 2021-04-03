from django.shortcuts import redirect

def isLoggedIn(get_response):

	def middleware(request):

		returnUrl=request.get_full_path()
	
		if not request.user.is_authenticated:
			return redirect(f'/accounts/login?returnUrl={returnUrl}')
	
		response = get_response(request)
		return response
	
	return middleware