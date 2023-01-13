from django.db import models


class review(models.Model):
    image = models.ImageField(default='default.jpg', blank=True, null=True)
    title = models.CharField(max_length=64)
    director = models.CharField(max_length=16)
    lead_actor = models.CharField(max_length=24)
    release_year = models.IntegerField()

    GENRE = [
        ('액션', '액션'),
        ('코미디', '코미디'),
        ('로맨스', '로맨스'),
        ('애니메이션', '애니메이션'),
        ('범죄', '범죄'),
        ('드라마', '드라마'),
        ('미스테리', '미스테리'),
        ('스릴러', '스릴러'),
        ('SF', 'SF'),
        ('모험', '모험'),
        ('판타지', '판타지'),
        ('공포', '공포'),
        ('기타', '기타'),
    ]
    genre = models.CharField(max_length=10, choices=GENRE, default='기타')
    stats = models.FloatField(max_length=1)
    running_time = models.CharField(max_length=16)
    content = models.TextField()
