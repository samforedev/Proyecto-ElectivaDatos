import matplotlib.pyplot as plt
import seaborn as sns

class data_utils():
    
    @staticmethod
    def get_basic_data(dataset):
        return 'El dataset tiene {} filas y {} columas'.format(dataset.shape[0], dataset.shape[1])

    @staticmethod
    def generate_graphic(dataframe, x=None, y=None, kind='hist', figsize=(8, 6), config=None):
        """
        Parámetros:
        - dataframe: DataFrame de Pandas
        - x: Columna para el eje X
        - y: Columna para el eje Y (opcional, depende del tipo de gráfico)
        - kind: Tipo de gráfico ('hist', 'box', 'scatter', 'bar', 'count', 'line', 'heatmap')
        - figsize: Tamaño de la figura (ancho, alto)
        - config: Diccionario con configuraciones adicionales (ej. {'title': 'Título', 'color': 'red'})

        """
        if config is None:
            config = {}

        plt.figure(figsize=figsize)


        if kind == 'hist':
            sns.histplot(data=dataframe, x=x, bins=config.get('bins', 20), color=config.get('color', 'blue'))


        elif kind == 'box':
            sns.boxplot(data=dataframe, x=x, y=y, palette=config.get('palette', 'pastel'))


        elif kind == 'scatter':
            sns.scatterplot(data=dataframe, x=x, y=y, hue=config.get('hue'), palette=config.get('palette', 'deep'))


        elif kind == 'bar':
            sns.barplot(data=dataframe, x=x, y=y, palette=config.get('palette', 'viridis'))


        elif kind == 'count':
            sns.countplot(data=dataframe, x=x, palette=config.get('palette', 'husl'))


        elif kind == 'line':
            sns.lineplot(data=dataframe, x=x, y=y, marker='o', color=config.get('color', 'green'))

        elif kind == 'heatmap':
            sns.heatmap(dataframe.corr(), annot=True, cmap=config.get('cmap', 'coolwarm'))


        if 'title' in config:
            plt.title(config['title'])

        plt.show()


    def get_complete_info(self, dataframe, config=None):
        if config is None:
            config = {}

        if config.get('show', False):
            print('-------------- DATA INFO --------------')
            self.__print_dataframe_info(dataframe)
            return

        result = {}

        if config.get('all'):
            result['sum_isnull'] = dataframe.isnull().sum()
            result['describe'] = dataframe.describe()
            result['nunique'] = dataframe.nunique()
        else:
            if config.get('sum_isnull'):
                result['sum_isnull'] = dataframe.isnull().sum()
            if config.get('describe'):
                result['describe'] = dataframe.describe()
            if config.get('nunique'):
                result['nunique'] = dataframe.nunique()

        return result

    ''' Private Methods '''
    def __print_dataframe_info(self, dataframe):
        print(dataframe.info())
        print(dataframe.isnull().sum())
        print(dataframe.describe())
        print(dataframe.nunique())


