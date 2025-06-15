from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    カスタムユーザーモデル
    B-4, B-5: プロフィール項目
    G-1: ゲーミフィケーション項目
    """
    # emailを必須・ユニークにする
    email = models.EmailField('メールアドレス', unique=True)
    
    profile_image = models.ImageField('プロフィール画像', upload_to='profile_pics/', default='profile_pics/default.png')
    introduction = models.TextField('自己紹介', max_length=500, blank=True)
    target_school = models.CharField('志望校', max_length=100, blank=True)

    # G-1: ゲーミフィケーション要素
    level = models.PositiveIntegerField('レベル', default=1)
    experience = models.PositiveIntegerField('経験値', default=0)
    points = models.PositiveIntegerField('ポイント', default=0)

    # emailでログインするように設定
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
