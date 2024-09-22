# Importar os módulos necessários do PyQGIS
from qgis.core import QgsVectorLayer, QgsProject, QgsPalLayerSettings, QgsTextFormat
from qgis.utils import iface
from qgis.core import QgsVectorLayerSimpleLabeling

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

    # Configurar os rótulos
    rotulos_config = QgsPalLayerSettings()
    
    # Definir o campo que será usado como rótulo (exemplo: campo "nome")
    rotulos_config.fieldName = 'Unidades'
    
    # Ativar rótulos
    rotulos_config.enabled = True
    
    # Definir o formato do texto do rótulo
    texto_formatado = QgsTextFormat()
    texto_formatado.setFont(QFont("Arial", 10))  # Fonte e tamanho do texto
    texto_formatado.setSize(10)  # Tamanho da fonte
    
    # Aplicar o formato de texto aos rótulos
    rotulos_config.setFormat(texto_formatado)
    
    # Aplicar a configuração de rótulos à camada
    camada_vetor.setLabelsEnabled(True)
    camada_vetor.setLabeling(QgsVectorLayerSimpleLabeling(rotulos_config))
    
    # Atualizar a interface para exibir os rótulos
    camada_vetor.triggerRepaint()
    iface.mapCanvas().refreshAllLayers()
