class CovidDataService:
    def __init__(self, data_sources):
        self.data_sources = data_sources
    
    def get_countries_data(self):
        countries_data = {}
        for source in self.data_sources:
            data = source.get_countries_data()
            countries_data.update(data)
        return countries_data
    
    def get_countries_historic_data(self):
        countries_historic_data = {}
        for source in self.data_sources:
            data = source.get_countries_historic_data()
            countries_historic_data.update(data)
        return countries_historic_data
