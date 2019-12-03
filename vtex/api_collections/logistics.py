from .base_api import BaseApi


class LogisticsApi(BaseApi):
    def _build_url(self, endpoint):
        url = f"https://logistics.{self.environment}.com.br/api/logistics/pvt"
        return url + endpoint + f"?an={self.account_name}"

    def get_all_carriers(self):
        url = self._build_url("/configuration/carriers")
        return self.get_result(url)

    def get_freight_values(self, carrier_id: int, cep: str):
        url = self._build_url(f"/configuration/freights/{carrier_id}/{cep}/values")
        return self.get_result(url)

    def get_all_docks(self):
        url = self._build_url(f"/configuration/docks")
        return self.get_result(url)

    def get_all_warehouses(self):
        url = self._build_url(f"/configuration/warehouses")
        return self.get_result(url)

    def get_inventory_by_sku(self, sku_id: int):
        url = self._build_url(f"/inventory/skus/{sku_id}")
        return self.get_result(url)
