import datetime

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import F

from .models import Token
from .forms import TokenForm
from .utils import create_short_url, menu
from URLShortener.settings import TOKEN_LIFETIME


def main_page(request):
    return render(request, 'urls/mainPage.html', {'menu': menu, 'form': TokenForm})


class TokenCreateView(CreateView):
    """Create a new token"""

    model = Token
    form_class = TokenForm
    template_name = 'urls/mainPage.html'
    success_url = reverse_lazy('token_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['absolute_url'] = self.request.build_absolute_uri()
        return context

    def form_valid(self, form):
        original_url = form.cleaned_data['original_url']

        token, created = Token.objects.get_or_create(original_url=original_url)
        if created:
            token.short_url = create_short_url()
            token.save()
        expires_at = token.created_at + datetime.timedelta(days=TOKEN_LIFETIME)
        return render(self.request, 'urls/token_created.html',
                      {'short_url': token.short_url,
                       'expires_at': expires_at.strftime('%d.%m.%Y, %H:%M'),
                       'original_url': original_url,
                       'absolute_url': self.request.build_absolute_uri()[:-13]})

    def form_invalid(self, form):
        return render(self.request, 'urls/token_creation_errors.html',
                      {'errors': [str(i) for i in form.errors.values()]})


class TokenListView(ListView):
    """List of all tokens with detailed info"""

    model = Token
    template_name = 'urls/tokenList.html'
    context_object_name = 'tokens'
    queryset = Token.objects.all().order_by('-created_at') \
        .annotate(expiration_time=F('created_at') + datetime.timedelta(days=TOKEN_LIFETIME))
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['absolute_url'] = ''.join(self.request.build_absolute_uri()[:-6])
        context['menu'] = menu
        return context


def short_url_redirect(request, short_url):
    """Redirect from the short link"""

    token = get_object_or_404(Token, short_url=short_url)
    Token.objects.filter(short_url=short_url).update(requests_count=F('requests_count') + 1)
    return redirect(token.original_url)


def page_not_found_view(request, exception=None):
    """404 handler"""

    context = {'menu': menu}
    return render(request, 'urls/404.html', context=context)
