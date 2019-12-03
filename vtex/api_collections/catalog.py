from .base_api import BaseApi


class CatalogApi(BaseApi):
    def _build_url(self, endpoint):
        catalog_endpoint = "/api/catalog_system"
        return self.base_url + catalog_endpoint + endpoint

    def get_category(self, category_id=1):
        endpoint = f"/pvt/category/{category_id}"
        return self._call_api(endpoint)

    def get_category_tree(self, level=3):
        endpoint = f"/pub/category/tree/{level}/"
        return self._call_api(endpoint)

    def get_brand(self, brand_id: int):
        endpoint = f"/pvt/brand/{brand_id}"
        return self._call_api(endpoint)

    def get_product_specification(self, product_id: int):
        endpoint = f"/pvt/products/{product_id}/specification"
        return self._call_api(endpoint)

    def get_product(self, product_id: int):
        endpoint = f"/pvt/products/ProductGet/{product_id}"
        return self._call_api(endpoint)

    def get_product_variations(self, product_id: int):
        endpoint = f"/pub/products/variations/{product_id}"
        return self._call_api(endpoint)

    def get_product_review_rate(self, product_id: int):
        # This one has an odd endpoint
        endpoint = f"/api/addon/pvt/review/GetProductRate/{product_id}"
        url = self.base_url + endpoint
        return self.get_result(url)

    def get_list_all_skus(self, page=1, page_size=1000):
        endpoint = f"/pvt/sku/stockkeepingunitids?page={page}&pagesize={page_size}"
        return self._call_api(endpoint)

    def get_sku(self, sku_id):
        endpoint = f"/pvt/sku/stockkeepingunitbyid/{sku_id}"
        return self._call_api(endpoint)

    def get_sales_channel(self):
        endpoint = f"/pvt/saleschannel/list"
        return self._call_api(endpoint)

    def get_sales_channel_by_id(self, sales_channel_id=1):
        endpoint = f"/pub/saleschannel/{sales_channel_id}"
        return self._call_api(endpoint)

    def get_seller_by_id(self, seller_id=1):
        endpoint = f"/pvt/seller/{seller_id}"
        return self._call_api(endpoint)
