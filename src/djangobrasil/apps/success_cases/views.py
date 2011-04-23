from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import NewCaseForm


def all_cases(request):
    return render_to_response(
        'success_cases/all_cases.html',
        context_instance=RequestContext(request),
    )

    
def new_case(request):
    form = NewCaseForm()
    if request.method == 'POST':
        form = NewCaseForm(request.POST)
        if form.is_valid():
            success_case = form.save()
            return render_to_response(
                'success_cases/case_submited.html',
                context_instance = RequestContext(request)
            )
            
    return render_to_response(
        'success_cases/new_case.html',
        {'form': form},
        context_instance=RequestContext(request),
    )
