# Implementación de la interfaz CSVAdapter
class CSVAdapter(ThirdPartyPlotter):
    def __init__(self, jsonProcessor):
        self.jsonProcessor = jsonProcessor

    def plotData(self, csvData):
        jsonData = self.jsonProcessor.convertToJson(csvData)
        # Lógica adicional para adaptar el jsonData antes de utilizar ThirdPartyPlotter
        super().plotData(jsonData)

# Implementación de la clase CovidDataService
