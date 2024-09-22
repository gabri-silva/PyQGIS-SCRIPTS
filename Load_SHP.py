# Importar o módulo necessário do PyQGIS
from qgis.core import QgsVectorLayer, QgsProject

# Caminho do arquivo .shp no seu computador
caminho_shp = "C:/Users/gab02/OneDrive/Área de Trabalho/QGIS Processos e Projetos/af6d128695a83e83fe5fed9bfc8445ac/Unidades_Conservacao.shp"

# Carregar o arquivo .shp como uma camada vetor
camada_vetor = QgsVectorLayer(caminho_shp, "Unidades de Conservacao", "ogr")

# Verificar se a camada foi carregada corretamente
if not camada_vetor.isValid():
    print("Erro ao carregar a camada!")
else:
    # Adicionar a camada ao projeto atual no QGIS
    QgsProject.instance().addMapLayer(camada_vetor)
    print("Camada carregada com sucesso!")
