import os

from django.conf import settings
from lxml import etree


class RetailysXMLParser:
    def __init__(self, file_path: str):
        parser = etree.XMLParser()
        tree = etree.parse(file_path, parser)
        self.root = tree.getroot()

    def get_number_of_items(self):
        """
        :return: number of items(products)
        """
        return len(self.root.xpath("items/item"))

    def get_next_item(self):
        """
        Generator for next item(product)
        :yield: item
        """
        for item in self.root.xpath("items/item"):
            yield item

    def get_item_spare_parts(self, item):
        """
        Generator for next spare part (which is categoryId="1", name="Náhradní díly")
        :param item:
        :yield: spare part item
        """
        if item.xpath("parts/part[@categoryId=1]"):
            for item in item.xpath("parts/part[@categoryId=1]/item"):
                yield item

    def get_name_of_item(self, item):
        return item.xpath("@name")[0] if item.xpath("@name") else ""


retailys_xml_parser = RetailysXMLParser(os.path.join(settings.BASE_DIR, "app/data/export_full.xml"))
