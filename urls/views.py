from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.shortcuts import get_object_or_404, redirect
from django.db.models import F

from .models import Token
from .forms import TokenForm
from .utils import create_short_url, menu


class TokenCreateView(CreateView):
    model = Token
    form_class = TokenForm
    template_name = 'urls/tokenCreate.html'
    success_url = reverse_lazy('token_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['absolute_url'] = self.request.build_absolute_uri()
        context['menu'] = menu
        return context

    def form_valid(self, form):
        existing_token = Token.objects.filter(original_url=form.cleaned_data['original_url'])
        if existing_token.exists():
            return JsonResponse({'short_url': Token.objects.get(original_url=
                                                                form.cleaned_data['original_url']).short_url})
        else:
            short_url = create_short_url()
            form.instance.short_url = short_url
            super().form_valid(form)
            return JsonResponse({'short_url': short_url})

    def form_invalid(self, form):
        return JsonResponse({'errors': [i for i in form.errors.values()]})


class TokenListView(ListView):
    model = Token
    template_name = 'urls/tokenList.html'
    context_object_name = 'tokens'
    queryset = Token.objects.all().order_by('-created_at')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['absolute_url'] = ''.join(self.request.build_absolute_uri().split('/')[:-2])
        context['menu'] = menu
        return context


def short_url_redirect(request, short_url):
    token = get_object_or_404(Token, short_url=short_url)
    Token.objects.filter(short_url=short_url).update(requests_count=F('requests_count') + 1)
    return redirect(token.original_url)




