from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Course(models.Model):
    title = models.CharField('Название курса', max_length=200)
    description = models.TextField('Описание курса', blank=True)
    banner = models.ImageField('Изображение для блока', upload_to='courses_banners/')
    youtube_link_id = models.SlugField('id от видео', max_length=20, blank=True)
    members = models.ManyToManyField(User, related_name='courses', blank=True)
    visible = models.BooleanField('Отображаеться', default=True)
    language = models.CharField('Язык', max_length=20, default='kk')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курстар'

    def get_absolute_url(self):
        return reverse('kurstar:course_landing', args=(self.id,))


class Food(models.Model):
    time = models.DateTimeField('Date-time', default=timezone.now)
    state = models.BooleanField('State', default=True)


class Clock(models.Model):
    visible = models.BooleanField('Отображаеться', default=True)


class Notification(models.Model):
    date = models.DateTimeField('Date-time', default=timezone.now)
    sender = models.ManyToManyField(User, related_name='send_notifications')
    subject = models.ManyToManyField(User, related_name='received_notifications')
    content = models.TextField('Content')


class Meal(models.Model):
    health_points = models.IntegerField('Health points', default=0)
    name = models.CharField('Meal name', max_length=200)
    description = models.TextField('Meal description', blank=True)
    allergic = models.TextField('Allergic specific')


class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, _('Dialog')),
        (CHAT, _('Chat'))
    )

    type = models.CharField(
        _('Тип'),
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=DIALOG
    )
    members = models.ManyToManyField(User, verbose_name=_("Участник"))

    def get_absolute_url(self):
        return 'users:messages', (), {'chat_id': self.pk}


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="Чат", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="Пользователь",  on_delete=models.CASCADE)
    message = models.TextField("Сообщение")
    pub_date = models.DateTimeField(_('Дата сообщения'), default=timezone.now)
    is_readed = models.BooleanField(_('Прочитано'), default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message
