# Create your views here.
from django.http import HttpResponse
from polls.models import Poll
from django.template import RequestContext,loader
from django.http import Http404
from django.shortcuts import render

#def index(request):
#    latest_pool_list = Poll.objects.order_by('-pub_date')[:5]
#    output = ','.join([p.question for p in latest_pool_list])
#    return HttpResponse(output)

def index(request):
    latest_pool_list = Poll.objects.order_by('-pub_date')[:5]
#    print latest_pool_list
#    return HttpResponse(latest_pool_list)
    output = ','.join([p.question for p in latest_pool_list])
    ids = ','.join([str(p.id) for p in latest_pool_list])
    template = loader.get_template('polls/index.html')
    context = RequestContext(request,{
                                      'latest_pool_list':latest_pool_list,
                                      'data':{"name":333333333333},
                                      'output':output,
                                      'ids':ids,
                                      }
                             )
    return HttpResponse(template.render(context))

def detail(request,poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
        
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll':poll})
#    return HttpResponse("you are looking at %s " % poll_id)

def results(request,poll_id):
    return HttpResponse("you are looking at results of poll  %s " % poll_id)

def vote(request,poll_id):
    return HttpResponse("you are voting on poll %s " % poll_id)

    