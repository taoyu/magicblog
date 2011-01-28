from django.shortcuts import render_to_response

def static_page(response, template):
	template =  "%s.html" % (template)
	return render_to_response(template)
