from django.shortcuts import redirect

def isLoggedIn(get_response):

	def middleware(request):

		returnUrl=request.META['PATH_INFO']
	
		if not request.user.is_authenticated:
			return redirect(f'/accounts/login?returnUrl={returnUrl}')
	
		response = get_response(request)
		return response
	
	return middleware