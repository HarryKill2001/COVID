# Implementación de la clase App
class App:
    def __init__(self):
        self.covidDataService = CovidDataService()
        self.csvAdapter = CSVAdapter(JSONProcessor())

    def getCountries(self):
        countriesData = self.covidDataService.getCountriesData()
        countriesHistoricData = self.covidDataService.getCountriesHistoricData()
        # Lógica para procesar los datos y obtener el csvData
        self.csvAdapter.plotData(csvData)


# Crear una instancia de la clase App y ejecutar la aplicación
app = App()
app.getCountries()
