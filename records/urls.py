# (既存のimportの下に追加)
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Record, Like, Comment # LikeとCommentを追加

# (RecordListView, RecordCreateViewの下に追記)
class LikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        record = get_object_or_404(Record, pk=self.kwargs['pk'])
        like, created = Like.objects.get_or_create(user=request.user, record=record)

        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        return JsonResponse({'liked': liked, 'count': record.likes.count()})

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
    template_name = 'records/record_detail.html' # コメントは詳細ページで行う

    def form_valid(self, form):
        record = get_object_or_404(Record, pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.record = record
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('records:record_detail', kwargs={'pk': self.kwargs['pk']})

class RecordDetailView(LoginRequiredMixin, DetailView):
    model = Record
    template_name = 'records/record_detail.html'
    context_object_name = 'record'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm() # CommentFormを定義する必要がある
        return context
