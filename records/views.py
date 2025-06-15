from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Record, Like, Comment
from .forms import RecordForm, CommentForm

class RecordListView(LoginRequiredMixin, ListView):
    model = Record
    template_name = 'records/record_list.html'
    context_object_name = 'records'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ログインユーザーがいいねした投稿のIDリストを取得
        if self.request.user.is_authenticated:
            context['liked_records'] = Like.objects.filter(user=self.request.user).values_list('record__id', flat=True)
        return context


class RecordCreateView(LoginRequiredMixin, CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'records/record_form.html'
    success_url = reverse_lazy('records:record_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecordDetailView(LoginRequiredMixin, DetailView):
    model = Record
    template_name = 'records/record_detail.html'
    context_object_name = 'record'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.order_by('created_at').all()
        context['comment_form'] = CommentForm()
        # この投稿をログインユーザーがいいねしているかどうかのフラグ
        context['is_liked'] = self.object.likes.filter(user=self.request.user).exists()
        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    # このビューは直接テンプレートを描画しないので、template_nameは不要

    def form_valid(self, form):
        record = get_object_or_404(Record, pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.record = record
        form.save()
        return redirect('records:record_detail', pk=record.pk)

    def get_success_url(self):
        return reverse_lazy('records:record_detail', kwargs={'pk': self.kwargs['pk']})


class LikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        record = get_object_or_404(Record, pk=self.kwargs['pk'])
        like, created = Like.objects.get_or_create(user=request.user, record=record)

        if not created:
            # すでに「いいね」していた場合は削除
            like.delete()
            liked = False
        else:
            # 新しく「いいね」した場合
            liked = True

        # JSONレスポンスを返す
        return JsonResponse({'liked': liked, 'count': record.likes.count()})
