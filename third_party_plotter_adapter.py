# third_party_plotter_adapter.py
from third_party_plotter import ThirdPartyPlotter

class ThirdPartyPlotterAdapter:
    def __init__(self, third_party_plotter):
        self.third_party_plotter = third_party_plotter
    
    def plot(self, data):
        # Adaptar los datos al formato esperado por ThirdPartyPlotter
        file_path = "countries_data.csv"
        # Llamada a la función plot_csv de ThirdPartyPlotter
        self.third_party_plotter.plot_csv(file_path)
