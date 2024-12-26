from rest_framework import serializers
from .models import *


class ContactCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    addrees = serializers.SerializerMethodField()

    class Meta:
        model = Contacts
        fields = [
            "phone_number",
            "email",
            "addrees",
            "facebook",
            "telegram",
            "instagram",
        ]

    def get_addrees(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")

        if lang == "en":
            return obj.addrees_en
        elif lang == "ru":
            return obj.addrees_ru
        return obj.addrees_uz


class BannerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        exclude = ["created_at", "updated_at"]


class BannerDetailSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    img = serializers.SerializerMethodField()

    class Meta:
        model = BannerModel
        fields = ["id", "title", "text", "img"]

    def get_title(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")

        if lang == "en":
            return obj.title_en
        elif lang == "ru":
            return obj.title_ru
        return obj.title_uz

    def get_text(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")

        if lang == "en":
            return obj.text_en
        elif lang == "ru":
            return obj.text_ru
        return obj.text_uz

    def get_img(self, obj):
        return f"/media/{obj.img}/"


class BannerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = [
            "title_uz",
            "title_en",
            "title_ru",
            "text_uz",
            "text_en",
            "text_ru",
            "img",
        ]


class AboutCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutModel
        fields = [
            "text_1_uz",
            "text_1_en",
            "text_1_ru",
            "text_2_uz",
            "text_2_en",
            "text_2_ru",
        ]


class AboutDetailSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()

    class Meta:
        model = AboutModel
        fields = ["id", "text"]

    def get_text(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")
        print(lang)
        if lang == "en":
            return obj.text_en
        elif lang == "ru":
            return obj.text_ru
        return obj.text_uz


class AboutUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutModel
        fields = [
            "id",
            "text_1_uz",
            "text_1_en",
            "text_1_ru",
            "text_2_uz",
            "text_2_en",
            "text_2_ru",
        ]


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = "__all__"


class ServiceDetailSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    img = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = ServiceModel
        fields = ["id", "img", "title", "text", "description", "color"]

    def get_title(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")

        if lang == "en":
            return obj.title_en
        elif lang == "ru":
            return obj.title_ru
        return obj.title_uz

    def get_description(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")

        if lang == "en":
            return obj.description_en
        elif lang == "ru":
            return obj.description_ru
        return obj.description_uz

    def get_text(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")

        if lang == "en":
            return obj.text_en
        elif lang == "ru":
            return obj.text_ru
        return obj.text_uz

    def get_img(self, obj):
        return f"/media/{obj.img}/"


class ServiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = "__all__"


class PicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PicturesModel
        fields = ["uuid", "picture", "created_at", "updated_at"]


class PictureDetailSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = PicturesModel
        fields = ["uuid", "picture"]

    def get_picture(self, obj):
        return f"/media/{obj.picture}"


class NewsCreateSerializer(serializers.ModelSerializer):
    pictures = PicturesSerializer(many=True, read_only=True)

    class Meta:
        model = NewsModel
        fields = [
            "title_uz",
            "title_en",
            "title_ru",
            "description_uz",
            "description_en",
            "description_ru",
            "short_description_uz",
            "short_description_en",
            "short_description_ru",
            "pictures",
            "popular",
            "created_at",
            "updated_at",
        ]


class NewsUpdateSerializer(serializers.ModelSerializer):
    pictures = PicturesSerializer(many=True, read_only=True)

    class Meta:
        model = NewsModel
        fields = [
            "title_uz",
            "title_en",
            "title_ru",
            "description_uz",
            "description_en",
            "description_ru",
            "pictures",
            "popular",
        ]


class NewsDetailSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    pictures = PictureDetailSerializer(many=True)
    picture_count = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()

    class Meta:
        model = NewsModel
        fields = [
            "id",
            "title",
            "description",
            "short_description",
            "pictures",
            "popular",
            "picture_count",
            "created_at",
            "updated_at",
        ]

    def get_title(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")

        if lang == "en":
            return obj.title_en
        elif lang == "ru":
            return obj.title_ru
        return obj.title_uz

    def get_description(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")

        if lang == "en":
            return obj.description_en
        elif lang == "ru":
            return obj.description_ru
        return obj.description_uz

    def get_short_description(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")

        if lang == "en":
            return obj.short_description_en
        elif lang == "ru":
            return obj.short_description_ru
        return obj.short_description_uz

    def get_picture_count(self, obj):
        total_images = obj.pictures.count()
        return total_images


class StatisticsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ["title_uz", "title_en", "title_ru", "count"]


class StatisticsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ["title_uz", "title_en", "title_ru", "count"]


class StatisticsDetailSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Statistics
        fields = ["id", "title", "count"]

    def get_title(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")

        if lang == "en":
            return obj.title_en
        elif lang == "ru":
            return obj.title_ru
        return obj.title_uz


class PhotoGaleryCreateSerializer(serializers.ModelSerializer):
    pictures = PicturesSerializer(many=True, read_only=True)

    class Meta:
        model = PhotoGalery
        fields = [
            "title_uz",
            "title_en",
            "title_ru",
            "pictures",
            "created_at",
            "updated_at",
        ]


class PhotoGaleryUpdateSerializer(serializers.ModelSerializer):
    pictures = PicturesSerializer(many=True, read_only=True)

    class Meta:
        model = PhotoGalery
        fields = ["title_uz", "title_en", "title_ru", "pictures"]


class PhotoGaleryDetailSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    pictures = PictureDetailSerializer(many=True)
    picture_count = serializers.SerializerMethodField()

    class Meta:
        model = PhotoGalery
        fields = ["id", "title", "pictures", "picture_count"]
        depth = 1

    def get_title(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")

        if lang == "en":
            return obj.title_en
        elif lang == "ru":
            return obj.title_ru
        return obj.title_uz

    def get_picture_count(self, obj):
        total_picture = obj.pictures.count()
        return total_picture


class UsefulLinksCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulLinks
        fields = ["img", "title_uz", "title_en", "title_ru", "url"]


class UsefulLinkUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulLinks
        fields = ["img", "title_uz", "title_en", "title_ru", "url"]


class UsefullLinksDetailSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    img = serializers.SerializerMethodField()

    class Meta:
        model = UsefulLinks
        fields = ["id", "title", "url", "img"]

    def get_title(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")

        if lang == "en":
            return obj.title_en
        elif lang == "ru":
            return obj.title_ru
        return obj.title_uz

    def get_img(self, obj):
        return f"/media/{obj.img}"


class MailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailsModel
        fields = "__all__"


class MailCreateSerializer(serializers.Serializer):
    name = serializers.CharField(
        max_length=100,
        required=True,
        help_text="Name of the person submitting the request",
    )
    phone = serializers.CharField(
        max_length=15,
        required=True,
        help_text="Phone number of the person submitting the request",
    )
    message = serializers.CharField(
        required=True, help_text="Message content of the request"
    )


class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LaboratoryModel
        fields = "__all__"


class LaboratoryDetailSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    fio = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    img = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()
    degree = serializers.SerializerMethodField()

    class Meta:
        model = LaboratoryModel
        fields = [
            "id",
            "title",
            "description",
            "organized_date",
            "img",
            "avatar",
            "fio",
            "position",
            "in_position",
            "degree",
            "email",
            "phone",
        ]

    def get_title(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.title_en
        if lang == "ru":
            return obj.title_ru
        return obj.title_uz

    def get_degree(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.degree_en
        if lang == "ru":
            return obj.degree_ru
        return obj.degree_uz

    def get_description(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.description_en
        if lang == "ru":
            return obj.description_ru
        return obj.description_uz

    def get_position(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.position_en
        if lang == "ru":
            return obj.position_ru
        return obj.position_uz

    def get_fio(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.fio_en
        if lang == "ru":
            return obj.fio_ru
        return obj.fio_uz

    def get_img(self, obj):
        return f"/media/{obj.img}/"

    def get_avatar(self, obj):
        return f"/media/{obj.avatar}/"


class ApparatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApparatModel
        fields = "__all__"


class ApparatDetailSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    fio = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    img = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()
    degree = serializers.SerializerMethodField()

    class Meta:
        model = ApparatModel
        fields = [
            "id",
            "title",
            "description",
            "organized_date",
            "img",
            "avatar",
            "fio",
            "position",
            "in_position",
            "degree",
            "email",
            "phone",
        ]

    def get_title(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.title_en
        if lang == "ru":
            return obj.title_ru
        return obj.title_uz

    def get_degree(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.degree_en
        if lang == "ru":
            return obj.degree_ru
        return obj.degree_uz

    def get_description(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.description_en
        if lang == "ru":
            return obj.description_ru
        return obj.description_uz

    def get_position(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.position_en
        if lang == "ru":
            return obj.position_ru
        return obj.position_uz

    def get_fio(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.fio_en
        if lang == "ru":
            return obj.fio_ru
        return obj.fio_uz

    def get_img(self, obj):
        return f"/media/{obj.img}/"

    def get_avatar(self, obj):
        return f"/media/{obj.avatar}/"


class StructureSerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    class Meta:
        model = Structure
        fields = "__all__"

    def get_img(self, obj):
        return f"/media/{obj.img}/"


class HomeAboutDetailSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text1 = serializers.SerializerMethodField()
    text2 = serializers.SerializerMethodField()

    class Meta:
        model = HomeAboutModel
        fields = ["id", "title", "text1", "text2"]

    def get_title(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.title_en
        if lang == "ru":
            return obj.title_ru
        return obj.title_uz

    def get_text1(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.text1_en
        if lang == "ru":
            return obj.text1_ru
        return obj.text1_uz

    def get_text2(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.text2_en
        if lang == "ru":
            return obj.text2_ru
        return obj.text2_uz


class LegalStatusSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField()

    class Meta:
        model = LegalStatusModel
        fields = ["id", "text"]

    def get_text(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.text_en
        if lang == "ru":
            return obj.text_ru
        return obj.text_uz


class LegalStatusFilesSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = LegalStatusFiles
        fields = ["id", "file", "size", "file_name"]

    def get_file(self, obj):
        return f"/media/{obj.file}/"

    def get_size(self, obj):
        fsize = obj.file.size
        if fsize < 1024:
            return f"{fsize} bytes"
        elif fsize < 1024 * 1024:
            return f"{fsize / 1024:.2f} KB"
        else:
            return f"{fsize / (1024 * 1024):.2f} MB"

    def get_file_name(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.file_name_en
        if lang == "ru":
            return obj.file_name_ru
        return obj.file_name_uz


class StructureFilesSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = StructureFiles
        fields = ["id", "file", "size", "file_name"]

    def get_file(self, obj):
        return f"/media/{obj.file}/"

    def get_size(self, obj):
        fsize = obj.file.size
        if fsize < 1024:
            return f"{fsize} bytes"
        elif fsize < 1024 * 1024:
            return f"{fsize / 1024:.2f} KB"
        else:
            return f"{fsize / (1024 * 1024):.2f} MB"

    def get_file_name(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.file_name_en
        if lang == "ru":
            return obj.file_name_ru
        return obj.file_name_uz


class FinanceFilesSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = FinanceFiles
        fields = ["id", "file", "size", "file_name"]

    def get_file(self, obj):
        return f"/media/{obj.file}/"

    def get_size(self, obj):
        fsize = obj.file.size
        if fsize < 1024:
            return f"{fsize} bytes"
        elif fsize < 1024 * 1024:
            return f"{fsize / 1024:.2f} KB"
        else:
            return f"{fsize / (1024 * 1024):.2f} MB"

    def get_file_name(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.file_name_en
        if lang == "ru":
            return obj.file_name_ru
        return obj.file_name_uz


class OpenDataFilesSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = OpenDataFiles
        fields = ["id", "file", "size", "file_name"]

    def get_file(self, obj):
        return f"/media/{obj.file}/"

    def get_size(self, obj):
        fsize = obj.file.size
        if fsize < 1024:
            return f"{fsize} bytes"
        elif fsize < 1024 * 1024:
            return f"{fsize / 1024:.2f} KB"
        else:
            return f"{fsize / (1024 * 1024):.2f} MB"

    def get_file_name(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.file_name_en
        if lang == "ru":
            return obj.file_name_ru
        return obj.file_name_uz


class CorruptionFilesSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = OpenDataFiles
        fields = ["id", "file", "size", "file_name"]

    def get_file(self, obj):
        return f"/media/{obj.file}/"

    def get_size(self, obj):
        fsize = obj.file.size
        if fsize < 1024:
            return f"{fsize} bytes"
        elif fsize < 1024 * 1024:
            return f"{fsize / 1024:.2f} KB"
        else:
            return f"{fsize / (1024 * 1024):.2f} MB"

    def get_file_name(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.file_name_en
        if lang == "ru":
            return obj.file_name_ru
        return obj.file_name_uz


class CorruptionSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = LegalStatusModel
        fields = ["id", "description"]

    def get_description(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.description_en
        if lang == "ru":
            return obj.description_ru
        return obj.description_uz


class ActivitySerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = ActivityModel
        fields = ["id", "title"]

    def get_title(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.title_en
        if lang == "ru":
            return obj.title_ru
        return obj.title_uz


class ActivityDetail(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()

    class Meta:
        model = ActivityModel
        fields = ["description"]

    def get_description(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.description_en
        if lang == "ru":
            return obj.description_ru
        return obj.description_uz


class WeekendSerializer(serializers.ModelSerializer):
    week = serializers.SerializerMethodField()

    class Meta:
        model = Weekend
        fields = ["id", "week"]

    def get_week(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language", "uz")

        if lang == "en":
            return obj.week_en
        if lang == "ru":
            return obj.week_ru
        return obj.week_uz


class ManagementSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    bio = serializers.SerializerMethodField()
    position = serializers.SerializerMethodField()
    admission_days = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = ManagementModel
        fields = [
            "id",
            "name",
            "bio",
            "position",
            "avatar",
            "email",
            "phone",
            "admission_days",
            "admission_start_time",
            "admission_end_time",
        ]

    def get_name(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.name_en
        if lang == "ru":
            return obj.name_ru
        return obj.name_uz

    def get_bio(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.bio_en
        if lang == "ru":
            return obj.bio_ru
        return obj.bio_uz

    def get_position(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.position_en
        if lang == "ru":
            return obj.position_ru
        return obj.position_uz

    def get_admission_days(self, obj):
        request = self.context.get("request")

        lang = request.headers.get("Accept-Language", "uz")

        admission_days = obj.admission_days.all()

        field_mapping = {
            "en": "week_en",
            "ru": "week_ru",
            "uz": "week_uz",
        }

        field_name = field_mapping.get(lang, "week_uz")

        admission_days_list = [
            getattr(weekend, field_name) for weekend in admission_days
        ]

        return admission_days_list

    def get_avatar(self, obj):
        return f"/media/{obj.avatar}/"


class AnnounceSerializer(serializers.ModelSerializer):
    pictures = PictureDetailSerializer(many=True)
    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    body = serializers.SerializerMethodField()
    picture_count = serializers.SerializerMethodField()

    class Meta:
        model = Announce
        fields = [
            "id",
            "title",
            "text",
            "body",
            "pictures",
            "picture_count",
            "published_date",
        ]

    def get_title(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.title_en
        if lang == "ru":
            return obj.title_ru
        return obj.title_uz

    def get_text(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.text_en
        if lang == "ru":
            return obj.text_ru
        return obj.text_uz

    def get_body(self, obj):
        request = self.context.get("request")
        lang = request.headers.get("Accept-Language")

        if lang == "en":
            return obj.body_en
        if lang == "ru":
            return obj.body_ru
        return obj.body_uz

    def get_img(self, obj):
        return f"/media/{obj.img}/"

    def get_picture_count(self, obj):
        total_images = obj.pictures.count()
        return total_images


class PartnerSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = PartnersModel
        fields = ["id", "icon", "url"]

    def get_icon(self, obj):
        return f"/media/{obj.icon}/"
