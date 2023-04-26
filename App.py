class App:
    def __init__(self, covid_data_service, plotter):
        self.covid_data_service = covid_data_service
        self.plotter = plotter
    
    def run(self):
        # Obtener los datos de los países desde el servicio de datos COVID-19
        countries_data = self.covid_data_service.get_countries_data()
        
        # Obtener los datos históricos de los países desde el servicio de datos COVID-19
        countries_historic_data = self.covid_data_service.get_countries_historic_data()
        
        # Procesar los datos obtenidos y generar las gráficas usando el plotter
        processed_data = process_data(countries_data, countries_historic_data)
        self.plotter.plot(processed_data)
