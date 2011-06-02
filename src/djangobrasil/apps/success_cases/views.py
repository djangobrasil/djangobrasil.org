from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from forms import NewCaseForm
from models import SuccessCase
from recaptcha_works.decorators import fix_recaptcha_remote_ip


def all_cases(request):
    all_success_cases = SuccessCase.objects.all()
    return render_to_response(
        'success_cases/all_cases.html',
        {'all_success_cases': all_success_cases},
        context_instance=RequestContext(request),
    )

@fix_recaptcha_remote_ip
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

def specific_case(request, slug):
    success_case = get_object_or_404(SuccessCase, slug=slug)
    return render_to_response(
        'success_cases/specific_case.html',
        {'success_case': success_case},
        context_instance = RequestContext(request),
    )
