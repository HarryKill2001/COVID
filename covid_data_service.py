# covid_data_service.py
from third_party_plotter_adapter import ThirdPartyPlotterAdapter
import json

class CovidDataService:
    def __init__(self):
        self.third_party_plotter_adapter = ThirdPartyPlotterAdapter(ThirdPartyPlotter())

    def get_countries_data(self):
        # Lógica para descargar los datos de contagios, muertes y pruebas de COVID-19 en formato JSON
        # ...
        # Conversión de los datos a un diccionario
        data = json.loads('{"Spain": {"deaths": 13000, "cases": 140000}, "France": {"deaths": 10000, "cases": 120000}}')
        self.third_party_plotter_adapter.plot(data)
    
    def get_countries_historic_data(self):
        # Lógica para descargar los datos históricos de contagios, muertes y pruebas de COVID-19 en formato JSON
        # ...
        # Conversión de los datos a un diccionario
        data = json.loads('{"Spain": [{"date": "2022-01-01", "deaths": 1300, "cases": 14000}, {"date": "2022-01-02", "deaths": 1310, "cases": 14100}], "France": [{"date": "2022-01-01", "deaths": 1000, "cases": 12000}, {"date": "2022-01-02", "deaths": 1010, "cases": 12100}]}')
        self.third_party_plotter_adapter.plot(data)
