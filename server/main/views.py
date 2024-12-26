from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from .pagination import *
from .filters import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from datetime import timedelta
from django.utils import timezone

class SuccessResponse(Response):
    def __init__(self, data=None, message=None, status=None, *args, **kwargs):
        response = {
            "data": data or [],
            "message": message or "",
            "status_code": status or 200
        }

        super().__init__(data=response, status=status, *args, **kwargs)


class ErrorResponse(Response):
    def __init__(self, error=None, message=None, status=None, path=None, method=None, *args, **kwargs):
        response = {
            "error": error or "",
            "message": message or "",
            "status_code": status or 400,
            "path": path,
            "method": method
        }

        super().__init__(data=response, status=status, *args, **kwargs)

class ContactView(APIView):
    @swagger_auto_schema(method="get")
    def get(self, request):
        contacts = Contacts.objects.last()
        
        return SuccessResponse(
            data=ContactSerializer(contacts, context={"request": request}).data,
            message="Contact list successfully retrieved",
            status=200
            )

    @swagger_auto_schema(auto_schema=None)
    def post(self, request):
        try:
            serializer = ContactCreateSerializer(data=request.data)

            if serializer.is_valid():

                contact = serializer.save()

                return SuccessResponse(
                    data=ContactSerializer(contact).data,
                    message="Contact successfully created", 
                    status=201,
                )
            else:
                error = serializer.errors

                return ErrorResponse(
                    error="Bad request",
                    message=error,
                    status=400,
                    path=request.path,
                    method=request.method
                )
        except Exception as e:
            return ErrorResponse(
                error="Bad request", 
                message=str(e),
                status=400,
                path=request.path,
                method=request.method
            )
    @swagger_auto_schema(auto_schema=None)
    def put(self, request):
        try:
            contact = Contacts.objects.get(pk=request.data.get('id'))

            serializer = ContactSerializer(contact, data=request.data)

            if serializer.is_valid():
                updated_contact = serializer.save()

                return SuccessResponse(
                    data=ContactSerializer(updated_contact).data,
                    message="Contact successfully updated",
                    status=200
                )
            else:
                error = serializer.errors

                return ErrorResponse(
                    error="Bad request",
                    message=error,
                    status=400,
                    path=request.path,
                    method=request.method
                )
        except Contacts.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Does not exists",
                status=404,
                path=request.path,
                method=request.method
            )
        except Exception as e:
            return ErrorResponse(
                error="Bad request",
                message=str(e),
                status=400,
                method=request.method,
                path=request.path
            )
    @swagger_auto_schema(auto_schema=None)
    def patch(self, request):
        try:
            contact = Contacts.objects.get(pk=request.data.get('id'))

            serializer = ContactSerializer(contact, data=request.data)

            if serializer.is_valid():
                updated_contact = serializer.save()

                return SuccessResponse(
                    data=ContactSerializer(updated_contact).data,
                    message="Contact successfully updated",
                    status=200
                )
            else:
                error = serializer.errors

                return ErrorResponse(
                    error="Bad request",
                    message=error,
                    status=400,
                    path=request.path,
                    method=request.method
                )
        except Contacts.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Does not exists",
                status=404,
                path=request.path,
                method=request.method
            )
        
        except Exception as e:
            return ErrorResponse(
                error="Bad request",
                message=str(e),
                status=400,
                method=request.method,
                path=request.path
            )
    @swagger_auto_schema(auto_schema=None)
    def delete(self, request):
        contact = Contacts.objects.filter(pk=request.data.get('id'))

        if contact.exists():
            contact.delete()

            return SuccessResponse(
                message="Contact successfully deleted",
                status=200    
            )
        return ErrorResponse(
            error="Not found",
            message="Contact not found with this id",
            status=404,
            path=request.path,
            method=request.method
        )

class BannerView(APIView):
    @swagger_auto_schema(method="get")
    def get(self, request):
        banners = BannerModel.objects.all()[:4]

        return SuccessResponse(
            data=BannerDetailSerializer(banners, many=True, context={"request": request}).data,
            message="Banners successfully retrieved",
            status=200,
        )
    @swagger_auto_schema(auto_schema=None)
    def post(self, request):
        try:
            serializer = BannerCreateSerializer(data=request.data)

            if serializer.is_valid():
                banner = serializer.save()

                return SuccessResponse(
                    data=BannerDetailSerializer(banner, context={"request": request}).data,
                    message="Banner successfully created",
                    status=201
                )
            else:
                error = serializer.errors

                return ErrorResponse(
                    error="Bad request",
                    message=str(error),
                    status=400,
                    path=request.path,
                    method=request.method
                )
            
        except Exception as e:
            return ErrorResponse(
                error="Bad request",
                message=str(e),
                status=400,
                path=request.path,
                method=request.method
            )    
    @swagger_auto_schema(auto_schema=None)
    def put(self, request):
        try:
            banner = BannerModel.objects.get(pk=request.data.get('id'))
            serializer = BannerUpdateSerializer(banner, data=request.data)

            if serializer.is_valid():
                updated_data = serializer.save()

                return SuccessResponse(
                    data=BannerDetailSerializer(updated_data, context={"request": request}).data,
                    status=200,
                    message="Banner successfully updated"
                )
            else:
                error = serializer.errors

                return ErrorResponse(
                    error="Bad request",
                    message=error,
                    status=400,
                    path=request.path,
                    method=request.method
                )
        except BannerModel.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Does not exists",
                status=404,
                path=request.path,
                method=request.method
            )
            
        except Exception as e:
            return ErrorResponse(
                error="Bad request",
                message=str(e),
                status=400,
                method=request.method,
                path=request.path
            )
    
    @swagger_auto_schema(auto_schema=None)
    def patch(self, request):
        try:
            banner = BannerModel.objects.get(pk=request.data.get('id'))
            serializer = BannerUpdateSerializer(banner, data=request.data)

            if serializer.is_valid():
                updated_data = serializer.save()

                return SuccessResponse(
                    data=BannerDetailSerializer(updated_data, context={"request": request}).data,
                    status=200,
                    message="Banner successfully updated"
                )
            else:
                error = serializer.errors

                return ErrorResponse(
                    error="Bad request",
                    message=error,
                    status=400,
                    path=request.path,
                    method=request.method
                )
        except BannerModel.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Does not exists",
                status=404,
                path=request.path,
                method=request.method
            )
        
        except Exception as e:
            return ErrorResponse(
                error="Bad request",
                message=str(e),
                status=400,
                method=request.method,
                path=request.path
            )
    @swagger_auto_schema(auto_schema=None)
    def delete(self, request):
        banner = BannerModel.objects.filter(pk=request.data.get('id'))

        if banner.exists():
            banner.delete()
            return SuccessResponse(
                message="Banner successfully deleted",
                status=200
            )
        
        return ErrorResponse(
            error="Not found",
            message="Banner not found with this id",
            status=404,
            method=request.method,
            path=request.path
        )

        
class AboutView(APIView):
    @swagger_auto_schema(method=None)
    def get(self, request):
        about = AboutModel.objects.last()

        return SuccessResponse(
            data=AboutDetailSerializer(about, context={'request': request}).data,
            message="About info successfully retrieved",
            status=200
        )
    @swagger_auto_schema(auto_schema=None)
    def post(self, request):
        try:
            serializer = AboutCreateSerializer(data=request.data)

            if serializer.is_valid():
                about = AboutModel.objects.all()

                if about.exists():
                    AboutModel.objects.all().delete()

                serializer.save()

                return SuccessResponse(
                    data=serializer.validated_data,
                    status=200,
                    message="About info successfully added"
                )
            else:
                error = serializer.errors
                return ErrorResponse(
                    error="Bad request",
                    message=error,
                    status=400,
                    path=request.path,
                    method=request.method
                )
            
        except Exception as e:
            return ErrorResponse(
                error="Bad request",
                message=str(e),
                status=400,
                method=request.method,
                path=request.path
            )
    @swagger_auto_schema(auto_schema=None)
    def put(self, request):
        try:
            about = AboutModel.objects.get(pk=request.data.get('id'))
            serializer = AboutUpdateSerializer(about, data=request.data)

            if serializer.is_valid():
                updated_about = serializer.save()

                return SuccessResponse(
                    data=AboutDetailSerializer(updated_about, context={'request': request}).data,
                    status=200,
                    message="About info successfully updated"
                )
            else:
                error = serializer.errors
                return ErrorResponse(
                    error="Bad request",
                    message=error,
                    status=400,
                    path=request.path,
                    method=request.method
                )
        except AboutModel.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Does not exists",
                status=404,
                path=request.path,
                method=request.method
            )
        
        except Exception as e:
            return ErrorResponse(
                    error="Bad request",
                    message=str(e),
                    status=400,
                    path=request.path,
                    method=request.method
                )
    @swagger_auto_schema(auto_schema=None)
    def patch(self, request):
        try:
            about = AboutModel.objects.get(pk=request.data.get('id'))
            serializer = AboutUpdateSerializer(about, data=request.data)

            if serializer.is_valid():
                updated_about = serializer.save()

                return SuccessResponse(
                    data=AboutDetailSerializer(updated_about, context={'request': request}).data,
                    status=200,
                    message="About info successfully updated"
                )
            else:
                error = serializer.errors
                return ErrorResponse(
                    error="Bad request",
                    message=error,
                    status=400,
                    path=request.path,
                    method=request.method
                )
        except AboutModel.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Does not exists",
                status=404,
                path=request.path,
                method=request.method
            )
        
        except Exception as e:
            return ErrorResponse(
                    error="Bad request",
                    message=str(e),
                    status=400,
                    path=request.path,
                    method=request.method
                )
        
class ServiceView(APIView):
    @swagger_auto_schema(method=None)
    def get(self, request):
        services = ServiceModel.objects.all()

        return SuccessResponse(
            data=ServiceDetailSerializer(services, many=True, context={"request": request}).data,
            status=200,
            message="Services list successfully retrieved"
        )
    @swagger_auto_schema(auto_schema=None)
    def post(self, request):
        try:
            serializer = ServiceCreateSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

                return SuccessResponse(
                    data=serializer.data,
                    status=201,
                    message="Service successfully created"
                )
            else:
                error = serializer.errors
                return ErrorResponse(
                    error="Bad request",
                    message=error,
                    status=200,
                    path=request.path,
                    method=request.method
                )
        except Exception as e:
            return ErrorResponse(
                error="Bad request",
                message=str(e),
                status=400,
                path=request.path,
                method=request.method
            )    
    @swagger_auto_schema(auto_schema=None)   
    def patch(self, request):
        try:
            service = ServiceModel.objects.get(pk=request.data.get('id'))
            serializer = ServiceUpdateSerializer(service, data=request.data)

            if serializer.is_valid():
                updated_data = serializer.save()

                return SuccessResponse(
                    data=ServiceDetailSerializer(updated_data, context={'request': request}).data,
                    status=200,
                    message="Service successfully updated"
                )
            else:
                error = serializer.errors
                return ErrorResponse(
                    error="Bad request",
                    message=error,
                    status=400,
                    method=request.method,
                    path=request.path
                )
        except ServiceModel.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Does not exists",
                status=404,
                path=request.path,
                method=request.method
            )
        except Exception as e:
            return ErrorResponse(
                error="Bad request",
                message=str(e),
                status=400,
                path=request.path,
                method=request.method
            )
    @swagger_auto_schema(auto_schema=None)
    def put(self, request):
        try:
            service = ServiceModel.objects.get(pk=request.data.get('id'))
            serializer = ServiceUpdateSerializer(service, data=request.data)

            if serializer.is_valid():
                updated_data = serializer.save()

                return SuccessResponse(
                    data=ServiceDetailSerializer(updated_data, context={'request': request}).data,
                    status=200,
                    message="Service successfully updated"
                )
            else:
                error = serializer.errors
                return ErrorResponse(
                    error="Bad request",
                    message=error,
                    status=400,
                    method=request.method,
                    path=request.path
                )
        except ServiceModel.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Does not exists",
                status=404,
                path=request.path,
                method=request.method
            )
        except Exception as e:
            return ErrorResponse(
                error="Bad request",
                message=str(e),
                status=400,
                path=request.path,
                method=request.method
            )
    @swagger_auto_schema(auto_schema=None)
    def delete(self, request):
        service = ServiceModel.objects.filter(pk=request.data.get('id'))

        if service.exists():
            service.delete()

            return SuccessResponse(
                message="Service successfully deleted",
                status=200
            )
        return ErrorResponse(
            error="Not found",
            message="Service doesn't exist",
            status=404,
            path=request.path,
            method=request.method
        )
    

class NewsView(APIView):
    @swagger_auto_schema(
        operation_description="Paginate by page query param.\n\n\nReturning values\n\n\nid,\ntitle - string,\npictures - list,\npicture_count - int,\n",
        manual_parameters=[
            openapi.Parameter(
                "limit",
                openapi.IN_QUERY,
                description="Paginate by page query",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ]
    )
    def get(self, request):
        news = NewsModel.objects.prefetch_related('pictures').order_by("-id")[5:]
        paginator = NewsPageSizePagination()
        paginated_news = paginator.paginate_queryset(news, request=request)
        serializer = NewsDetailSerializer(paginated_news, many=True, context={"request": request})
        
        return paginator.get_paginated_response(
            data=serializer.data
        )
    
    @swagger_auto_schema(auto_schema=None)
    def post(self, request):
        serializer = NewsCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(
                data=serializer.data,
                message="News successfully created",
                status=201
            )
        return ErrorResponse(
            error="Bad request",
            message=serializer.errors,
            status=400,
            path=request.path,
            method=request.method
        )
    @swagger_auto_schema(auto_schema=None)
    def put(self, request):
        try:
            news = NewsModel.objects.get(pk=request.data.get('id'))
            serializer = NewsUpdateSerializer(news, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return SuccessResponse(
                    data=serializer.data,
                    message="News successfully updated",
                    status=200
                )
            return ErrorResponse(
                error="Bad request",
                message=serializer.errors,
                status=400,
                path=request.path,
                method=request.method
            )
        except NewsModel.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="News doesn't exist",
                status=404,
                path=request.path,
                method=request.method
            )
    @swagger_auto_schema(auto_schema=None)
    def patch(self, request):
        try:
            news = NewsModel.objects.get(pk=request.data.get('id'))
            serializer = NewsUpdateSerializer(news, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return SuccessResponse(
                    data=serializer.data,
                    message="News successfully updated",
                    status=200
                )
            return ErrorResponse(
                error="Bad request",
                message=serializer.errors,
                status=400,
                path=request.path,
                method=request.method
            )
        except NewsModel.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="News doesn't exist",
                status=404,
                path=request.path,
                method=request.method
            )
    @swagger_auto_schema(auto_schema=None)
    def delete(self, request):
        try:
            news = NewsModel.objects.get(pk=request.data.get('id'))
            news.delete()
            return SuccessResponse(
                message="News successfully deleted",
                status=200
            )
        except NewsModel.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="News doesn't exist",
                status=404,
                path=request.path,
                method=request.method
            )

class LastFiveNews(APIView):
    def get(self, request):
        news = NewsModel.objects.prefetch_related('pictures').order_by('-id')[:5]
        serializer = NewsDetailSerializer(news, many=True, context={"request": request})
        return SuccessResponse(
            data=serializer.data,
            message="Last news successfully retrieved",
            status=200
        )

class StatisticsView(APIView):
    @swagger_auto_schema(method=None)
    def get(self, request):
        statistics = Statistics.objects.all()
        serializer = StatisticsDetailSerializer(statistics, many=True, context={"request": request})
        return SuccessResponse(
            data=serializer.data,
            message="Statistics successfully retrieved",
            status=200
        )
    @swagger_auto_schema(auto_schema=None)
    def post(self, request):
        serializer = StatisticsCreateSerializer(data=request.data)
        if serializer.is_valid():
            statistics = Statistics.objects.all()

            if len(statistics) >= 4:
                return ErrorResponse(
                    error="Bad request",
                    message="You have already 4 statistics. You can't add statistics anymore",
                    status=400,
                    path=request.path,
                    method=request.method
                )
            
            serializer.save()
            return SuccessResponse(
                data=serializer.data,
                message="Statistics successfully created",
                status=201
            )
        return ErrorResponse(
            error="Bad request",
            message=serializer.errors,
            status=400,
            path=request.path,
            method=request.method
        )
    @swagger_auto_schema(auto_schema=None)
    def put(self, request):
        try:
            statistic = Statistics.objects.get(pk=request.data.get('id'))
            serializer = StatisticsUpdateSerializer(statistic, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return SuccessResponse(
                    data=serializer.data,
                    message="Statistics successfully updated",
                    status=200
                )
            return ErrorResponse(
                error="Bad request",
                message=serializer.errors,
                status=400,
                path=request.path,
                method=request.method
            )
        except Statistics.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Statistic doesn't exist",
                status=404,
                path=request.path,
                method=request.method
            )
    @swagger_auto_schema(auto_schema=None)    
    def patch(self, request):
        try:
            statistic = Statistics.objects.get(pk=request.data.get('id'))
            serializer = StatisticsUpdateSerializer(statistic, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return SuccessResponse(
                    data=serializer.data,
                    message="Statistics successfully updated",
                    status=200
                )
            return ErrorResponse(
                error="Bad request",
                message=serializer.errors,
                status=400,
                path=request.path,
                method=request.method
            )
        except Statistics.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Statistic doesn't exist",
                status=404,
                path=request.path,
                method=request.method
            )

class GetThreeGalery(APIView):
    def get(self, request):
        galeries = PhotoGalery.objects.prefetch_related('pictures').order_by('-id')[:3]

        serializer = PhotoGaleryDetailSerializer(galeries, many=True, context={"request": request})

        return SuccessResponse(
            data=serializer.data,
            status=200,
            message="Last 3 galeries successfully retrieved"
        )

class PhotoGaleryView(APIView):
    @swagger_auto_schema(
        operation_description="Paginate by page query param.\n\n\nReturning values\n\n\nid,\ntitle - string,\npictures - list,\npicture_count - int,\n",
        manual_parameters=[
            openapi.Parameter(
                "page",
                openapi.IN_QUERY,
                description="Paginate by page query",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ]
    )
    def get(self, request):
        galleries = PhotoGalery.objects.prefetch_related('pictures')
        paginator = PhotoGaleryPageSizePagination()
        paginated_galery = paginator.paginate_queryset(galleries, request)
        serializer = PhotoGaleryDetailSerializer(paginated_galery, many=True, context={"request": request})
        
        return paginator.get_paginated_response(serializer.data)
    
    @swagger_auto_schema(auto_schema=None)
    def post(self, request):
        serializer = PhotoGaleryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(
                data=serializer.data,
                message="Photo gallery successfully created",
                status=201
            )
        return ErrorResponse(
            error="Bad request",
            message=serializer.errors,
            status=400,
            path=request.path,
            method=request.method
        )
    @swagger_auto_schema(auto_schema=None)
    def put(self, request):
        try:
            gallery = PhotoGalery.objects.get(pk=request.data.get('id'))
            serializer = PhotoGaleryUpdateSerializer(gallery, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return SuccessResponse(
                    data=serializer.data,
                    message="Photo gallery successfully updated",
                    status=200
                )
            return ErrorResponse(
                error="Bad request",
                message=serializer.errors,
                status=400,
                path=request.path,
                method=request.method
            )
        except PhotoGalery.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Gallery doesn't exist",
                status=404,
                path=request.path,
                method=request.method
            )
    @swagger_auto_schema(auto_schema=None)   
    def patch(self, request):
        try:
            gallery = PhotoGalery.objects.get(pk=request.data.get('id'))
            serializer = PhotoGaleryUpdateSerializer(gallery, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return SuccessResponse(
                    data=serializer.data,
                    message="Photo gallery successfully updated",
                    status=200
                )
            return ErrorResponse(
                error="Bad request",
                message=serializer.errors,
                status=400,
                path=request.path,
                method=request.method
            )
        except PhotoGalery.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Gallery doesn't exist",
                status=404,
                path=request.path,
                method=request.method
            )
    @swagger_auto_schema(auto_schema=None)
    def delete(self, request):
        try:
            gallery = PhotoGalery.objects.get(pk=request.data.get('id'))
            gallery.delete()
            return SuccessResponse(
                message="Photo gallery successfully deleted",
                status=200
            )
        except PhotoGalery.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Gallery doesn't exist",
                status=404,
                path=request.path,
                method=request.method
            )


class UsefulLinksView(APIView):
    @swagger_auto_schema(method=None)
    def get(self, request):
        links = UsefulLinks.objects.all()
        serializer = UsefullLinksDetailSerializer(links, many=True, context={"request": request})
        return SuccessResponse(
            data=serializer.data,
            message="Useful links successfully retrieved",
            status=200
        )
    @swagger_auto_schema(auto_schema=None)
    def post(self, request):
        serializer = UsefulLinksCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return SuccessResponse(
                data=serializer.data,
                message="Useful link successfully created",
                status=201
            )
        return ErrorResponse(
            error="Bad request",
            message=serializer.errors,
            status=400,
            path=request.path,
            method=request.method
        )
    @swagger_auto_schema(auto_schema=None)
    def put(self, request):
        try:
            link = UsefulLinks.objects.get(pk=request.data.get('id'))
            serializer = UsefulLinkUpdateSerializer(link, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return SuccessResponse(
                    data=serializer.data,
                    message="Useful link successfully updated",
                    status=200
                )
            return ErrorResponse(
                error="Bad request",
                message=serializer.errors,
                status=400,
                path=request.path,
                method=request.method
            )
        except UsefulLinks.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Useful link doesn't exist",
                status=404,
                path=request.path,
                method=request.method
            )
    @swagger_auto_schema(auto_schema=None)
    def patch(self, request):
        try:
            link = UsefulLinks.objects.get(pk=request.data.get('id'))
            serializer = UsefulLinkUpdateSerializer(link, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return SuccessResponse(
                    data=serializer.data,
                    message="Useful link successfully updated",
                    status=200
                )
            return ErrorResponse(
                error="Bad request",
                message=serializer.errors,
                status=400,
                path=request.path,
                method=request.method
            )
        except UsefulLinks.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Useful link doesn't exist",
                status=404,
                path=request.path,
                method=request.method
            )
    @swagger_auto_schema(auto_schema=None)   
    def delete(self, request):
        try:
            link = UsefulLinks.objects.get(pk=request.data.get('id'))
            link.delete()
            return SuccessResponse(
                message="Useful link successfully deleted",
                status=200
            )
        except UsefulLinks.DoesNotExist:
            return ErrorResponse(
                error="Not found",
                message="Useful link doesn't exist",
                status=404,
                path=request.path,
                method=request.method
            )

class GetOneNewsView(APIView):
    def get(self, request, pk):
        news = NewsModel.objects.filter(pk=pk)
        if news.exists():
            news = news.last()
            serializer = NewsDetailSerializer(news, context={"request": request})

            return SuccessResponse(
                data=serializer.data,
                message="News successfully retrieved",
                status=200,
            )
        return ErrorResponse(
            error="Not found",
            message="News not found with this id",
            path=request.path,
            method=request.method,
            status=404
        )
    
class GetOneGaleryView(APIView):
    def get(self, request, pk):
        galery = PhotoGalery.objects.filter(pk=pk)
        if galery.exists():
            galery = galery.last()
            serializer = PhotoGaleryDetailSerializer(galery, context={"request": request})

            return SuccessResponse(
                data=serializer.data,
                message="Galery successfully retrieved",
                status=200,
            )
        return ErrorResponse(
            error="Not found",
            message="Galery not found with this id",
            path=request.path,
            method=request.method,
            status=404
        )
    
class GetOneServiceView(APIView):
    def get(self, request, pk):
        service = ServiceModel.objects.filter(pk=pk)
        if service.exists():
            service = service.last()
            serializer = ServiceDetailSerializer(service, context={"request": request})

            return SuccessResponse(
                data=serializer.data,
                message="Service successfully retrieved",
                status=200,
            )
        return ErrorResponse(
            error="Not found",
            message="Service not found with this id",
            path=request.path,
            method=request.method,
            status=404
        )
    
class GetOneUsefullView(APIView):
    def get(self, request, pk):
        usefull = UsefulLinks.objects.filter(pk=pk)
        if usefull.exists():
            usefull = usefull.last()
            serializer = UsefullLinksDetailSerializer(usefull, context={"request": request})

            return SuccessResponse(
                data=serializer.data,
                message="Usefull link successfully retrieved",
                status=200,
            )
        return ErrorResponse(
            error="Not found",
            message="Usefull link not found with this id",
            path=request.path,
            method=request.method,
            status=404
        )

class GetOneBannerView(APIView):
    def get(self, request, pk):
        banner = BannerModel.objects.filter(pk=pk)
        if banner.exists():
            banner = banner.last()
            serializer = BannerDetailSerializer(banner, context={"request": request})

            return SuccessResponse(
                data=serializer.data,
                message="Banner successfully retrieved",
                status=200,
            )
        return ErrorResponse(
            error="Not found",
            message="Banner not found with this id",
            path=request.path,
            method=request.method,
            status=404
        )

class PopularNewsView(APIView):
    def get(self, request):
        popular_news = NewsModel.objects.filter(popular=True).prefetch_related('pictures')

        if popular_news.exists():
            serializer = NewsDetailSerializer(popular_news, many=True, context={"request": request})

            return SuccessResponse(
                data=serializer.data,
                message="Popular news successfully retrieved",
                status=200
            )
        return SuccessResponse(
            data=[],
            message="Popular news list is empty",
            status=200
        )


class MailView(APIView):
    def get(self, request):
        mails = MailsModel.objects.filter(status=True)

        if mails.exists():
            return SuccessResponse(
                data=MailSerializer(mails, many=True).data,
                status=200,
                message="Mails list successfully retrieved"
            )
        return SuccessResponse(
            data=[],
            message="Mail list is empty",
            status=200
        )
    
    @swagger_auto_schema(
        operation_description="Send data via POST request. Fields: name, phone, message.",
        request_body=MailCreateSerializer
    )
    def post(self, request):
        try:
            serializer = MailSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

                return SuccessResponse(
                    data=serializer.data,
                    message="Successfully sended",
                    status=201  
                )
            return ErrorResponse(
                error="Bad request",
                message=str(serializer.errors),
                path=request.path,
                method=request.method,
                status=400
            )
        except Exception as e:
            return ErrorResponse(
                error="Bad request",
                message=str(e),
                status=400,
                path=request.path,
                method=request.method
            )
        

class GetDetailMail(APIView):
    def get(self, request, pk):
        mail = MailsModel.objects.filter(pk=pk)

        if mail.exists():
            mail = mail.first()
            return SuccessResponse(
                data=MailSerializer(mail).data,
                status=200,
                message="Mail detail successfully retrieved"
            )
        return ErrorResponse(
            error="Not found",
            message="Mail not found",
            status=404,
            path=request.path,
            method=request.method
        )
    
class GetDisactiveMailsView(APIView):
    def get(self, request):
        mails = MailsModel.objects.filter(status=False)

        if mails.exists():
            return SuccessResponse(
                data=MailSerializer(mails, many=True).data,
                status=200,
                message="Disactive Mails list successfully retrieved"
            )
        return SuccessResponse(
            data=[],
            message="Mails list is empty",
            status=200
        )
    

class LaboratoryView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve by query params.",
        manual_parameters=[
            openapi.Parameter(
                "page",
                openapi.IN_QUERY,
                description="Paginate by page query",
                type=openapi.TYPE_STRING,
                required=False,
            ),
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                description="Search by search query",
                type=openapi.TYPE_STRING,
                required=False,
            ),
        ]
    )
    def get(self, request):
        laboratories = LaboratoryModel.objects.all()
        filterset = LaboratoryFilter(request.GET, queryset=laboratories, request=request)
        paginator = LaboratoryPageSizePagination()
        filtered_data = filterset.qs
        paginated_data = paginator.paginate_queryset(filtered_data, request)

        serializer = LaboratoryDetailSerializer(paginated_data, many=True, context={"request": request})

        return paginator.get_paginated_response(
            data=serializer.data
        )
    
    @swagger_auto_schema(auto_schema=None)
    def post(self, request):
        try:
            serializer = LaboratorySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

                return SuccessResponse(
                    data=serializer.data,
                    message="Successfully posted",
                    status=201
                )
            return ErrorResponse(
                error="Bad request",
                message=serializer.errors,
                status=400,
                path=request.path,
                method=request.method
            )
        except Exception as e:
            return ErrorResponse(
                error="Bad request",
                message=str(e),
                status=400,
                path=request.path,
                method=request.method
            )
class ApparatView(APIView):
    def get(self, request):
        apparats =  ApparatModel.objects.all()
        if not apparats.exists():
            return SuccessResponse(
                data=[],
                message="Apparat list is empty",
                status=200
            )
        serializer = ApparatDetailSerializer(apparats, many=True, context={"request": request})

        return SuccessResponse(
            data=serializer.data,
            status=200,
            message="Apparat successfully retrieved"
        )
    
    @swagger_auto_schema(auto_schema=None)
    def post(self, request):
        try:
            serializer = ApparatSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

                return SuccessResponse(
                    data=serializer.data,
                    message="Successfully posted",
                    status=201
                )
            return ErrorResponse(
                error="Bad request",
                message=serializer.errors,
                status=400,
                path=request.path,
                method=request.method
            )
        except Exception as e:
            return ErrorResponse(
                error="Bad request",
                message=str(e),
                status=400,
                path=request.path,
                method=request.method
            )

class GetLaboratoryView(APIView):
    def get(self, request, pk):
        laboratory = LaboratoryModel.objects.filter(pk=pk)

        if laboratory.exists():
            laboratory = laboratory.last()

            return SuccessResponse(
                data=LaboratoryDetailSerializer(laboratory, context={'request': request}).data,
                status=200,
                message="Laboratory successfully retrieved"
            )
        return ErrorResponse(
            error="Not found",
            message="Laboratory not found",
            status=404,
            path=request.path,
            method=request.method
        )
    
class GetApparatView(APIView):
    def get(self, request, pk):
        apparat = ApparatModel.objects.filter(pk=pk)

        if apparat.exists():
            apparat = apparat.last()

            return SuccessResponse(
                data=ApparatDetailSerializer(apparat, context={'request': request}).data,
                status=200,
                message="Apparat successfully retrieved"
            )
        return ErrorResponse(
            error="Not found",
            message="Apparat not found",
            status=404,
            path=request.path,
            method=request.method
        )
    


class StructureVIew(APIView):
    def get(self, request):
        structure = Structure.objects.last()

        return SuccessResponse(
            data=StructureSerializer(structure).data,
            message="Structure img retrieved",
            status=200
        )
    

class HomeAboutView(APIView):
    def get(self, request):
        about = HomeAboutModel.objects.last()

        return SuccessResponse(
            data=HomeAboutDetailSerializer(about, context={"request": request}).data,
            status=200,
            message="Home about infos successfully retrieved"
        )


class LegalStatusView(APIView):
    def get(self, request):
        legal_status = LegalStatusModel.objects.last()

        serializer = LegalStatusSerializer(legal_status, context={"request": request})

        return SuccessResponse(
            data=serializer.data,
            message="Legal status info successfully retrieved",
            status=200
        )

class LegalStatusFilesView(APIView):
    def get(self, request):
        files = LegalStatusFiles.objects.all()

        serializer = LegalStatusFilesSerializer(files, many=True, context={"request": request})

        return SuccessResponse(
            data=serializer.data,
            message="Legal status files successfully retrieved",
            status=200
        )
    
class StructureFilesView(APIView):
    def get(self, request):
        structure = StructureFiles.objects.all()

        serializer = StructureFilesSerializer(structure, many=True, context={"request": request})

        return SuccessResponse(
            data=serializer.data,
            message="Structure files successfully retrieved",
            status=200
        )

class OpenDataFilesView(APIView):
    def get(self, request):
        open_data_files = OpenDataFiles.objects.all()

        serializer = OpenDataFilesSerializer(open_data_files, many=True, context={"request": request})

        return SuccessResponse(
            data=serializer.data,
            message="Open Data files successfully retrieved",
            status=200
        )

class FinanceFilesView(APIView):
    def get(self, request):
        finance_files = FinanceFiles.objects.all()

        serializer = FinanceFilesSerializer(finance_files, many=True, context={"request": request})

        return SuccessResponse(
            data=serializer.data,
            message="Finance files successfully retrieved",
            status=200
        )

class ActivityView(APIView):
    def get(self, request):
        activities = ActivityModel.objects.all()

        serializer = ActivitySerializer(activities, many=True, context={"request": request})
        return SuccessResponse(
            data=serializer.data,
            message="Activities successfully retrieved",
            status=200
        )

class GetOneActivity(APIView):
    def get(self, request, pk):
        activity = ActivityModel.objects.filter(pk=pk)
        
        if activity.exists():
            activity = activity.first()
            return SuccessResponse(
                data=ActivityDetail(activity, context={"request": request}).data,
                message="Activity info successfully retrieved",
                status=200
            )
        return ErrorResponse(
            error="Not found",
            message="Activity not found",
            path=request.path,
            method=request.method,
            status=404
        )
        
class WeekendView(APIView):
    def get(self, request):
        weekends = Weekend.objects.all()

        serializer = WeekendSerializer(weekends, many=True, context={"request": request})

        return SuccessResponse(
            data=serializer.data,
            message="Weekend list successfully retrieved",
            status=200
        )

class ManagementView(APIView):
    def get(self, request):
        managements = ManagementModel.objects.prefetch_related('admission_days')

        serializer = ManagementSerializer(managements, many=True, context={"request": request})

        return SuccessResponse(
            data=serializer.data,
            message="Management list successfully retrieved",
            status=200
        )

class GetOneManagmentView(APIView):
    def get(self, request, pk):
        management = ManagementModel.objects.filter(pk=pk)

        if management.exists():
            management = management.first()

            return SuccessResponse(
                data=ManagementSerializer(management, context={"request": request}).data
            )
        return ErrorResponse(
            error="Not found",
            message="Manager not found with this id",
            status=404,
            path=request.path,
            method=request.method
        )


class FilterNews(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a list of news with optional filtering by title.\n\n\nReturning values\n\n\nid,\ntitle - string,\ndescription - string,\npictures - list,\npopular - boolean,\npicture_count - int,\ncreated_at - date-time,\nupdated_at - date-time,\n",
        manual_parameters=[
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                description="Search query to filter news by title.",
                type=openapi.TYPE_STRING,
                required=False,
            )
        ]
    )
    def get(self, request):
        news = NewsModel.objects.all()

        filterset = NewsFilter(request.GET, queryset=news, request=request)

        filtered_news = filterset.qs

        serializer = NewsDetailSerializer(filtered_news, many=True, context={"request": request})

        return SuccessResponse(
            data=serializer.data,
            message="Filtering successfully",
            status=200
        )

class HomeAnnounceView(APIView):
    def get(self, request):
        announce = Announce.objects.prefetch_related('pictures').order_by('-id')[:3]

        serializer = AnnounceSerializer(announce, many=True, context={"request": request})

        return SuccessResponse(
            data=serializer.data,
            message="Announce successfully retrieved",
            status=200
        )
class AnnounceView(APIView):
    def get(self, request):
        announce = Announce.objects.prefetch_related('pictures')
        paginator = AnnouncePageSizePagination()
        paginated_data = paginator.paginate_queryset(announce, request=request)
        serializer = AnnounceSerializer(paginated_data, many=True, context={"request": request})

        return paginator.get_paginated_response(
            data=serializer.data
        )
    
class GetAnnounceView(APIView):
    def get(self, request, pk):
        announce = Announce.objects.filter(pk=pk)

        if announce.exists():
            announce = announce.first()

            serializer = AnnounceSerializer(announce, context={"request": request})
            return SuccessResponse(
                data=serializer.data,
                message="Announce successfully retrieved",
                status=200
            )
        return ErrorResponse(
            error="Not found",
            message="Announce not found",
            status=404,
            path=request.path,
            method=request.method
        )


class PartnerView(APIView):
    def get(self, request):
        partners = PartnersModel.objects.all()

        serializer = PartnerSerializer(partners, many=True)

        return SuccessResponse(
            data=serializer.data,
            message="Partners list successfully retrieved",
            status=200
        )