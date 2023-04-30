from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from app.helpers.XMLParser import retailys_xml_parser


class ProductCount(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        data = {"product_count": retailys_xml_parser.get_number_of_items()}
        return Response(data=data)


class ProductList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        data = {
            "product_names": [
                retailys_xml_parser.get_name_of_item(item) for item in retailys_xml_parser.get_next_item()
            ]
        }
        return Response(data=data)


class SparePartsList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        data = []
        for item in retailys_xml_parser.get_next_item():
            list_of_spare_parts = [
                retailys_xml_parser.get_name_of_item(spare_part)
                for spare_part in retailys_xml_parser.get_item_spare_parts(item)
            ]
            data.append({retailys_xml_parser.get_name_of_item(item): list_of_spare_parts})
        return Response(data={"products_with_spare_parts": data})
