from django.db import models
from django.urls import reverse

class Person(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    about = models.TextField(verbose_name="Обо мне")
    photo = models.ImageField(upload_to="photos/", verbose_name="Фото")
    active = models.BooleanField(verbose_name="Активно")

    class Meta:
        verbose_name = 'Вы'
        verbose_name_plural = 'Вы'

class Projects(models.Model):
    person = models.ForeignKey(Person,on_delete=models.PROTECT)
    projName = models.CharField(max_length=255, verbose_name="Имя проекта")
    desc = models.TextField(verbose_name="Описание проекта")
    tech = models.TextField(verbose_name="Используемые технологии")
    comment = models.TextField(verbose_name="Комментарий")
    link = models.TextField(verbose_name="Ссылка")
    photo = models.ImageField(upload_to="photos/projects", verbose_name="Фото", null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('project', kwargs={'project_slug': self.slug})
    
    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'
        ordering = ['-id']


class Skills(models.Model):
    person = models.ForeignKey(Person,on_delete=models.PROTECT)
    backend = models.TextField(verbose_name="Бэкенд", null=True, blank=True)
    frontend = models.TextField(verbose_name="Фронтенд", blank=True)
    linux = models.TextField(verbose_name="ПО Линукс", blank=True)
    windows = models.TextField(verbose_name="ПО Виндовс", blank=True)
    databases = models.TextField(verbose_name="Базы данных", blank=True)
    virtualization = models.TextField(verbose_name="Виртуализация", blank=True)
    softskills = models.TextField(verbose_name="СофтСкиллс", blank=True)

    class Meta:
        verbose_name = 'Навыки'
        verbose_name_plural = 'Навыки'

class Experience(models.Model):
    person = models.ForeignKey(Person,on_delete=models.PROTECT)
    company = models.TextField(verbose_name="Компания")
    post = models.CharField(max_length=255, verbose_name="Должность")
    info = models.TextField(verbose_name="Обязанности")
    dateStart = models.DateField(verbose_name="Начало")
    dateEnd = models.DateField(verbose_name="Конец")

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'


class Education(models.Model):
    person = models.ForeignKey(Person,on_delete=models.PROTECT)
    name = models.TextField(verbose_name="Учебн. учреждение")
    department = models.TextField(verbose_name="Факультет")
    info = models.TextField(verbose_name="Что освоили")
    dateStart = models.DateField(verbose_name="Начало")
    dateEnd = models.DateField(verbose_name="Конец")

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'
        
class MailNotification(models.Model):
    person = models.ForeignKey(Person,on_delete=models.PROTECT)
    mailLogin = models.CharField(max_length=255, verbose_name="Логин")
    mailPassword = models.CharField(max_length=255,verbose_name="Пароль")
    isActive = models.BooleanField(default=False, verbose_name="Активно")
    mailSmtpServer = models.CharField(max_length=255, verbose_name="SMTP сервер")
    mailSmtpPort = models.IntegerField(default=465, verbose_name="SMTP порт")

    class Meta:
        verbose_name = 'Почтовое оповещение'
        verbose_name_plural = 'Почтовое оповещение'

class Contacts(models.Model):
    person = models.ForeignKey(Person,on_delete=models.PROTECT)
    mail = models.CharField(max_length=255, verbose_name="Почта")
    github = models.TextField(verbose_name="Github")
    telegram = models.TextField(verbose_name="Telegram")
    location = models.CharField(max_length=255, verbose_name="Город")
    policy = models.TextField(verbose_name="Политика конфиденциальности")

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Site_settings(models.Model):
    siteName = models.TextField(verbose_name="Имя сайта")
    previewS = models.TextField(verbose_name="Превью статический текст")
    previewD = models.TextField(verbose_name="Превью динамический текст")
    footerText = models.TextField(verbose_name="Текст футера")

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'