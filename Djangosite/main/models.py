from django.db import models
from django.urls import reverse

class Person(models.Model):
    fullName = models.CharField(max_length=255, verbose_name="ФИО")
    about = models.TextField(verbose_name="Обо мне")
    post = models.CharField(max_length=255, verbose_name="Должность")
    photo = models.ImageField(upload_to="photos/", verbose_name="Фото")

    class Meta:
        verbose_name = 'Вы'
        verbose_name_plural = 'Вы'

class Projects(models.Model):
    preson = models.ForeignKey(Person,on_delete=models.CASCADE)
    projName = models.CharField(max_length=255, verbose_name="Имя проекта")
    description = models.TextField(verbose_name="Описание проекта")
    link = models.TextField(verbose_name="Ссылка")
    photo = models.ImageField(upload_to="photos/projects", verbose_name="Фото")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def get_absolute_url(self):
        return reverse('project', kwargs={'project_slug': self.slug})
    
    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'


class Skills(models.Model):
    preson = models.ForeignKey(Person,on_delete=models.CASCADE)
    skiName = models.TextField(verbose_name="Наименование навыка")

    class Meta:
        verbose_name = 'Навыки'
        verbose_name_plural = 'Навыки'

class Experience(models.Model):
    preson = models.ForeignKey(Person,on_delete=models.CASCADE)
    comName = models.TextField(verbose_name="Компания")
    post = models.CharField(max_length=255, verbose_name="Должность")
    dateStart = models.DateField(verbose_name="Начало")
    dateEnd = models.DateField(verbose_name="Конец")

    class Meta:
        verbose_name = 'Опыт работы'
        verbose_name_plural = 'Опыт работы'


class Education(models.Model):
    preson = models.ForeignKey(Person,on_delete=models.CASCADE)
    eduName = models.TextField(verbose_name="Учебн. учреждение")
    eduDepartment = models.TextField(default='IT', verbose_name="Факультет")
    eduQualification = models.TextField(default='IT', verbose_name="Квалификация")
    dateStart = models.DateField(verbose_name="Начало")
    dateEnd = models.DateField(verbose_name="Конец")

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'
