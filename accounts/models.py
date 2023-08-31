from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.
class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='profile',
    )
    # post_set =
    # post_set 였으나 중복으로 인해 related_name 거쳐서 like_posts=가 됨.

    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # followers = 칼럼 생김 나를 팔로잉 하는 사람 following은 내가 팔로우 하는 사람들