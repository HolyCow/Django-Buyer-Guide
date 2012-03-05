from django.shortcuts import render_to_response
from django.template import RequestContext

from buyerguideapp.models import Group, Publication

def index(request):
    return render_to_response('buyerguideapp/index.html', 
                              { 'publications': Publication.objects.all, },
                              context_instance=RequestContext(request))

