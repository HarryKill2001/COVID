class CSVPlotter(Plotter):
    def plot(self, data):
        # Convertir los datos a un formato adecuado para la librería de graficación
        csv_data = to_csv(data)
        
        # Generar las gráficas usando la librería de graficación
        generate_plots(csv_data)
