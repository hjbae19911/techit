from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from articleapp.models import Article
from profileapp.models import Profile


def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_article = Article.objects.get(pk=kwargs['pk'])
        if target_article.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated

