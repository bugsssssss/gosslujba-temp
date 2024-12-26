from django.db import models
from ckeditor.fields import RichTextField
from uuid import uuid4
from colorfield.fields import ColorField


class Contacts(models.Model):
    phone_number = models.CharField(("Телефонный номер"), max_length=15)
    email = models.EmailField(("Электронная почта"))
    addrees_uz = models.CharField(("Узбекский Адрес"), max_length=200, blank=True)
    addrees_en = models.CharField(("Адрес на английском"), max_length=200, blank=True)
    addrees_ru = models.CharField(("Русский Адрес"), max_length=200, blank=True)
    facebook = models.CharField(("Ссылка на Facebook"), max_length=200)
    telegram = models.CharField(("Ссылка на Telegram"), max_length=200)
    instagram = models.CharField(("Ссылка на Instagram"), max_length=200)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"


class BannerModel(models.Model):
    img = models.ImageField(("Изображение баннера"), upload_to="images/")
    title_uz = models.CharField(("Узбекский заголовок баннера"), max_length=500)
    title_ru = models.CharField(("Русский заголовок баннера"), max_length=500)
    title_en = models.CharField(("Заголовок баннера на английском"), max_length=500)
    text_uz = models.TextField(("Узбекский текст баннера"))
    text_ru = models.TextField(("Русский текст баннера"))
    text_en = models.TextField(("Текст баннера на английском"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Баннеры"
        verbose_name_plural = "Баннеры"
        ordering = ["-created_at"]


class AboutModel(models.Model):
    text_uz = RichTextField(("Узбекский о тексте"))
    text_en = RichTextField(("Текст на английском"))
    text_ru = RichTextField(("Текст на русском"))

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = "О деталях"
        verbose_name_plural = "О деталях"


class ServiceModel(models.Model):
    img = models.FileField(("Изображение услуги"), upload_to="images/")
    title_uz = models.CharField(("Узбекский заголовок услуги"), max_length=100)
    title_ru = models.CharField(("Русский заголовок услуги"), max_length=100)
    title_en = models.CharField(("Заголовок услуги на английском"), max_length=100)
    text_uz = RichTextField(("Узбекский текст услуги"))
    text_en = RichTextField(("Текст услуги на английском"))
    text_ru = RichTextField(("Русский текст услуги"))
    color = ColorField(("Цвет фона услуги"))
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Сервисы"
        verbose_name_plural = "Сервисы"


class PicturesModel(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False)
    picture = models.ImageField(upload_to="images/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.uuid)

    class Meta:
        verbose_name = "Изображения"
        verbose_name_plural = "Изображения"


class NewsModel(models.Model):
    title_uz = models.CharField(("Узбекский заголовок новости"), max_length=200)
    title_en = models.CharField(("Заголовок новости на английском"), max_length=200)
    title_ru = models.CharField(("Русский заголовок новости"), max_length=200)
    description_uz = RichTextField(("Узбекский текст новости"))
    description_en = RichTextField(("Текст новости на английском"))
    description_ru = RichTextField(("Русский текст новости"))
    pictures = models.ManyToManyField(
        PicturesModel, verbose_name="Изображения новости", blank=True
    )
    popular = models.BooleanField(("Популярно?"), default=False)
    picture_count = models.IntegerField(("Количество изображений"), default=0)
    short_description_uz = models.TextField(
        blank=True, verbose_name="Краткое описание (узбекский)"
    )
    short_description_en = models.TextField(
        blank=True, verbose_name="Краткое описание (английский)"
    )
    short_description_ru = models.TextField(
        blank=True, verbose_name="Краткое описание (русский)"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]


class Statistics(models.Model):
    title_uz = models.CharField(("Узбекский заголовок статистики"), max_length=100)
    title_en = models.CharField(("Заголовок статистики на английском"), max_length=100)
    title_ru = models.CharField(("Русский заголовок статистики"), max_length=100)
    count = models.IntegerField(("Количество статистики"))

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Статистика"
        verbose_name_plural = "Статистика"


class PhotoGalery(models.Model):
    title_uz = models.CharField(("Узбекский заголовок галереи"), max_length=200)
    title_en = models.CharField(("Заголовок галереи на английском"), max_length=200)
    title_ru = models.CharField(("Русский заголовок галереи"), max_length=200)
    pictures = models.ManyToManyField(
        PicturesModel, verbose_name="Изображения галереи", blank=True
    )
    picture_count = models.IntegerField(("Количество изображений в галерее"), default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Галереи"
        verbose_name_plural = "Галереи"
        ordering = ["-created_at"]


class UsefulLinks(models.Model):
    img = models.FileField(("Изображение для полезной ссылки"), upload_to="images/")
    title_uz = models.CharField(
        ("Узбекский заголовок полезной ссылки"), max_length=100, blank=True
    )
    title_en = models.CharField(
        ("Заголовок полезной ссылки на английском"), max_length=100, blank=True
    )
    title_ru = models.CharField(
        ("Русский заголовок полезной ссылки"), max_length=100, blank=True
    )
    url = models.URLField(("Полезная ссылка"))

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Полезные ссылки"
        verbose_name_plural = "Полезные ссылки"


class MailsModel(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(("Имя"), max_length=100)
    phone = models.CharField(("Номер телефона"), max_length=15)
    message = models.TextField(("Текст сообщения"))

    sended_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = ("Сообщения",)
        verbose_name_plural = "Сообщения"
        ordering = ["-sended_time"]


class LaboratoryModel(models.Model):
    img = models.ImageField(("Изображение лаборатории"), upload_to="images/")
    title_uz = models.CharField(("Узбекский заголовок лаборатории"), max_length=300)
    title_en = models.CharField(("Заголовок лаборатории на английском"), max_length=300)
    title_ru = models.CharField(("Русский заголовок лаборатории"), max_length=300)
    avatar = models.ImageField(("Изображение кандидата"), upload_to="images/")
    fio_ru = models.CharField(
        ("Полное имя кандидата на русском (Фамилия, Имя, Отчество)"), max_length=200
    )
    fio_en = models.CharField(
        ("Полное имя кандидата на английском (Фамилия, Имя, Отчество)"), max_length=200
    )
    fio_uz = models.CharField(
        ("Полное имя кандидата на узбекском (Фамилия, Имя, Отчество)"), max_length=200
    )
    organized_date = models.DateField(("Год основания"))
    in_position = models.DateField("Дата начала работы кандидата")
    position_ru = models.CharField(
        ("Род деятельности кандидата на русском"), max_length=100
    )
    position_en = models.CharField(
        ("Род деятельности кандидата на английском"), max_length=100
    )
    position_uz = models.CharField(
        ("Род деятельности кандидата на узбекском"), max_length=100
    )
    description_uz = RichTextField(("Узбекское дополнительное описание"))
    description_en = RichTextField(("Дополнительное описание на английском"))
    description_ru = RichTextField(("Русское дополнительное описание"))
    degree_uz = models.CharField(("Узбекское Академическая степень"), max_length=100)
    degree_ru = models.CharField(("Русское Академическая степень"), max_length=100)
    degree_en = models.CharField(
        ("Академическая степень на английском"), max_length=100
    )
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Лаборатория"
        verbose_name_plural = "Лаборатория"
        ordering = ["-created_at"]


class ApparatModel(models.Model):
    img = models.ImageField(("Изображение аппарата"), upload_to="images/")
    title_uz = models.CharField(("Узбекский заголовок аппарата"), max_length=300)
    title_en = models.CharField(("Заголовок аппарата на английском"), max_length=300)
    title_ru = models.CharField(("Русский заголовок аппарата"), max_length=300)
    avatar = models.ImageField(("Изображение кандидата"), upload_to="images/")
    fio_ru = models.CharField(
        ("Полное имя кандидата на русском (Фамилия, Имя, Отчество)"), max_length=200
    )
    fio_en = models.CharField(
        ("Полное имя кандидата на английском (Фамилия, Имя, Отчество)"), max_length=200
    )
    fio_uz = models.CharField(
        ("Полное имя кандидата на узбекском (Фамилия, Имя, Отчество)"), max_length=200
    )
    organized_date = models.DateField(("Год основания"))
    in_position = models.DateField("Дата начала работы кандидата")
    position_ru = models.CharField(
        ("Род деятельности кандидата на русском"), max_length=100
    )
    position_en = models.CharField(
        ("Род деятельности кандидата на английском"), max_length=100
    )
    position_uz = models.CharField(
        ("Род деятельности кандидата на узбекском"), max_length=100
    )
    description_uz = RichTextField(("Узбекское дополнительное описание"))
    description_en = RichTextField(("Дополнительное описание на английском"))
    description_ru = RichTextField(("Русское дополнительное описание"))
    degree_uz = models.CharField(("Узбекское Академическая степень"), max_length=100)
    degree_ru = models.CharField(("Русское Академическая степень"), max_length=100)
    degree_en = models.CharField(
        ("Академическая степень на английском"), max_length=100
    )
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Аппарат"
        verbose_name_plural = "Аппарат"
        ordering = ["-created_at"]


class Structure(models.Model):
    img = models.ImageField(("Изображение структуры"), upload_to="images/")

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Схема структуры"
        verbose_name_plural = "Схема структуры"


class HomeAboutModel(models.Model):
    title_uz = models.CharField(
        ("Узбекский заголовок раздела 'О нас' на главной странице"),
        max_length=300,
        blank=True,
        null=True,
    )
    title_en = models.CharField(
        ("Заголовок раздела 'О нас' на главной странице на английском"),
        max_length=300,
        blank=True,
        null=True,
    )
    title_ru = models.CharField(
        ("Русский заголовок раздела 'О нас' на главной странице"),
        max_length=300,
        blank=True,
        null=True,
    )
    text1_uz = models.TextField(
        ("Узбекский текст первого абзаца раздела 'О нас' на главной странице"),
        blank=True,
        null=True,
    )
    text1_en = models.TextField(
        ("Текст первого абзаца раздела 'О нас' на главной странице на английском"),
        blank=True,
        null=True,
    )
    text1_ru = models.TextField(
        ("Текст первого абзаца раздела 'О нас' на главной странице на русском"),
        blank=True,
        null=True,
    )
    text2_uz = models.TextField(
        ("Узбекский текст второго абзаца раздела 'О нас' на главной странице"),
        blank=True,
        null=True,
    )
    text2_en = models.TextField(
        ("Текст второго абзаца раздела 'О нас' на главной странице на английском"),
        blank=True,
        null=True,
    )
    text2_ru = models.TextField(
        ("Текст второго абзаца раздела 'О нас' на главной странице на русском"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Главная О на"
        verbose_name_plural = "Главная О на"


class LegalStatusModel(models.Model):
    text_uz = RichTextField(("Узбекский текст Правовой статуса"))
    text_ru = RichTextField(("Русский текст Правовой статуса"))
    text_en = RichTextField(("Текст Правовой статуса на английском"))

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Правовой статус"
        verbose_name_plural = "Правовой статус"


class LegalStatusFiles(models.Model):
    file = models.FileField(("Файл"), upload_to="files/")
    size = models.CharField(("Размер файла"), max_length=100)
    file_name_uz = models.CharField(("Узбекское имя файла"), max_length=1000)
    file_name_ru = models.CharField(("Русское имя файла"), max_length=1000)
    file_name_en = models.CharField(("Английское имя файла"), max_length=1000)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Файлы Правовой статуса"
        verbose_name_plural = "Файлы Правовой статуса"


class StructureFiles(models.Model):
    file = models.FileField(("Файл"), upload_to="files/")
    size = models.CharField(("Размер файла"), max_length=100)
    file_name_uz = models.CharField(("Узбекское имя файла"), max_length=1000)
    file_name_ru = models.CharField(("Русское имя файла"), max_length=1000)
    file_name_en = models.CharField(("Английское имя файла"), max_length=1000)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Структура документа"
        verbose_name_plural = "Структура документа"


class FinanceFiles(models.Model):
    file = models.FileField(("Файл"), upload_to="files/")
    size = models.CharField(("Размер файла"), max_length=100)
    file_name_uz = models.CharField(("Узбекское имя файла"), max_length=1000)
    file_name_ru = models.CharField(("Русское имя файла"), max_length=1000)
    file_name_en = models.CharField(("Английское имя файла"), max_length=1000)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Финансовые документы"
        verbose_name_plural = "Финансовые документы"


class OpenDataFiles(models.Model):
    file = models.FileField(("Файл"), upload_to="files/")
    size = models.CharField(("Размер файла"), max_length=100)
    file_name_uz = models.CharField(("Узбекское имя файла"), max_length=1000)
    file_name_ru = models.CharField(("Русское имя файла"), max_length=1000)
    file_name_en = models.CharField(("Английское имя файла"), max_length=1000)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Файлы открытых данных"
        verbose_name_plural = "Файлы открытых данных"


class ActivityModel(models.Model):
    title_uz = models.CharField(("Узбекский заголовок деятельности"), max_length=200)
    title_ru = models.CharField(("Русский заголовок деятельности"), max_length=200)
    title_en = models.CharField(("Английский заголовок деятельности"), max_length=200)
    description_uz = RichTextField(("Узбекский текст о деятельности"))
    description_ru = RichTextField(("Русский текст о деятельности"))
    description_en = RichTextField(("Текст о деятельности на английском"))

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Деятельность"
        verbose_name_plural = "Деятельность"
        ordering = ["-created_at"]


class Weekend(models.Model):
    week_uz = models.CharField(("Узбекское название дня недели"), max_length=200)
    week_ru = models.CharField(("Русское название дня недели"), max_length=200)
    week_en = models.CharField(("Название дня недели на английском"), max_length=200)

    def __str__(self):
        return self.week_uz

    class Meta:
        verbose_name = "Дни недели"
        verbose_name_plural = "Дни недели"


class ManagementModel(models.Model):
    avatar = models.ImageField(("Фото"), upload_to="images/")
    name_uz = models.CharField(
        ("Узбекское полное имя (Имя, Фамилия и Отчество)"), max_length=200
    )
    name_ru = models.CharField(
        ("Русское полное имя (Имя, Фамилия и Отчество)"), max_length=200
    )
    name_en = models.CharField(
        ("Английское полное имя (Имя, Фамилия и Отчество)"), max_length=200
    )
    position_uz = models.CharField(("Узбекская должность"), max_length=200)
    position_ru = models.CharField(("Русская должность"), max_length=200)
    position_en = models.CharField(("Английская должность"), max_length=200)
    email = models.EmailField(("Электронная почта"))
    phone = models.CharField(("Телефонный номер"), max_length=15)
    admission_days = models.ManyToManyField(
        Weekend, verbose_name="Выберите дни приема", blank=True
    )
    admission_start_time = models.TimeField(("Время начала приема"))
    admission_end_time = models.TimeField(("Время окончания приема"))
    bio_uz = models.TextField(("Узбекская биография"))
    bio_ru = models.TextField(("Русская биография"))
    bio_en = models.TextField(("Английская биография"))

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = "Руководители"
        verbose_name_plural = "Руководители"


class Announce(models.Model):
    pictures = models.ManyToManyField(
        PicturesModel, verbose_name="Изображение", blank=True
    )
    title_uz = models.CharField(max_length=300, verbose_name="Заголовок на узбекском")
    title_ru = models.CharField(max_length=300, verbose_name="Заголовок на русском")
    title_en = models.CharField(max_length=300, verbose_name="Заголовок на английском")
    text_uz = models.TextField(verbose_name="Текст на узбекском")
    text_ru = models.TextField(verbose_name="Текст на русском")
    text_en = models.TextField(verbose_name="Текст на английском")
    body_uz = RichTextField(verbose_name="Основной текст на узбекском")
    body_ru = RichTextField(verbose_name="Основной текст на русском")
    body_en = RichTextField(verbose_name="Основной текст на английском")
    published_date = models.DateTimeField(auto_now_add=True)
    picture_count = models.IntegerField(("Количество изображений"), default=0)

    def __str__(self):
        return self.title_uz

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class PartnersModel(models.Model):
    icon = models.FileField(("Изображение Компании"), upload_to="images/")
    url = models.URLField()

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "Партнеры"
        verbose_name_plural = "Партнеры"


class CorruptionModel(models.Model):
    description_uz = RichTextField(("Узбекский текст"))
    description_ru = RichTextField(("Русский текст"))
    description_en = RichTextField(("английском Текст"))

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = "Коррупции"
        verbose_name_plural = "Коррупции"


class CorruptionFiles(models.Model):
    file = models.FileField(("Файл"), upload_to="files/")
    size = models.CharField(("Размер файла"), max_length=100)
    file_name_uz = models.CharField(("Узбекское имя файла"), max_length=1000)
    file_name_ru = models.CharField(("Русское имя файла"), max_length=1000)
    file_name_en = models.CharField(("Английское имя файла"), max_length=1000)

    def __str__(self):
        return self.file_name_ru

    class Meta:
        verbose_name = "Файлы Коррупции"
        verbose_name_plural = "Файлы Коррупции"
