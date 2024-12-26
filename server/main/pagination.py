from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class NewsPageSizePagination(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        limit = request.query_params.get("limit", None)

        if limit is not None:
            try:
                limit = int(limit)
                if limit > self.max_page_size:
                    limit = self.max_page_size
                self.page_size = limit
            except ValueError:
                self.page_size = 6
        else:
            self.page_size = 6
        
        paginator = super().paginate_queryset(queryset, request, view)
        
        if paginator is None:
            return paginator
        
        return paginator

    def get_paginated_response(self, data):
        next_page = self.page.next_page_number() if self.page.has_next() else None
        previous_page = self.page.previous_page_number() if self.page.has_previous() else None

        from_index = self.page.start_index()
        to_index = self.page.end_index()

        return Response(
            {
                "total_elements": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "page_size": len(data),
                "current_page": self.page.number,
                "next": next_page,
                "previous": previous_page,
                "from": from_index,
                "to": to_index,
                "status_code": 200,
                "message": "Paginated data list",
                "data": data,
            }
        )

class AnnouncePageSizePagination(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        self.page_size = 6


        paginator = super().paginate_queryset(queryset, request, view)
        
        if paginator is None:
            return paginator
        
        return paginator

    def get_paginated_response(self, data):
        next_page = self.page.next_page_number() if self.page.has_next() else None
        previous_page = self.page.previous_page_number() if self.page.has_previous() else None

        from_index = self.page.start_index()
        to_index = self.page.end_index()

        return Response(
            {
                "total_elements": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "page_size": len(data),
                "current_page": self.page.number,
                "next": next_page,
                "previous": previous_page,
                "from": from_index,
                "to": to_index,
                "status_code": 200,
                "message": "Paginated data list",
                "data": data,
            }
        )

class PhotoGaleryPageSizePagination(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        self.page_size = 6

        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        next_page = self.page.next_page_number() if self.page.has_next() else None
        previous_page = self.page.previous_page_number() if self.page.has_previous() else None

        from_index = self.page.start_index()
        to_index = self.page.end_index()

        return Response(
            {
                "total_elements": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "page_size": len(data),
                "current_page": self.page.number,
                "next": next_page,
                "previous": previous_page,
                "from": from_index,
                "to": to_index,
                "status_code": 200,
                "message": "Paginated data list",
                "data": data,
            }
        )
    
class LaboratoryPageSizePagination(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        self.page_size = 5

        paginator = super().paginate_queryset(queryset, request, view)
        
        if paginator is None:
            return paginator
        
        return paginator

    def get_paginated_response(self, data):
        next_page = self.page.next_page_number() if self.page.has_next() else None
        previous_page = self.page.previous_page_number() if self.page.has_previous() else None

        from_index = self.page.start_index()
        to_index = self.page.end_index()

        return Response(
            {
                "total_elements": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "page_size": len(data),
                "current_page": self.page.number,
                "next": next_page,
                "previous": previous_page,
                "from": from_index,
                "to": to_index,
                "status_code": 200,
                "message": "Paginated data list",
                "data": data,
            }
        )
