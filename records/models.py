from django.db import models
from django.conf import settings

class Record(models.Model):
    """
    D-1, D-3, D-5, D-6: 学習記録モデル
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='records')
    content = models.TextField('学習内容')
    study_time = models.PositiveIntegerField('学習時間(分)', help_text='分単位で入力')
    concentration = models.IntegerField('集中度', default=5, help_text='1-10のスライダーで評価')
    memo = models.TextField('メモ', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username}の学習記録: {self.content[:20]}'

class Like(models.Model):
    """ F-2: いいねモデル """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 1ユーザーが1投稿に1つしか「いいね」できないようにする
        unique_together = ('user', 'record')

class Comment(models.Model):
    """ F-3: コメントモデル """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('コメント内容', max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.text[:20]
