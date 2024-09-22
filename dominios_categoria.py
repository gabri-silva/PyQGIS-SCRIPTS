# Importar os módulos necessários do PyQGIS
from qgis.core import QgsVectorLayer, QgsProject, QgsPalLayerSettings, QgsTextFormat, QgsVectorLayerSimpleLabeling, QgsCategorizedSymbolRenderer, QgsSymbol, QgsRendererCategory
from qgis.utils import iface
from PyQt5.QtGui import QColor
import random

# Caminho do arquivo .shp no seu computador
caminho_shp = "C:/Users/gab02/OneDrive/Área de Trabalho/QGIS Processos e Projetos/af6d128695a83e83fe5fed9bfc8445ac/Unidades_Conservacao.shp"

# Carregar o arquivo .shp como uma camada vetor
camada_vetor = QgsVectorLayer(caminho_shp, "APAs Tocantins", "ogr")

# Verificar se a camada foi carregada corretamente
if not camada_vetor.isValid():
    print("Erro ao carregar a camada!")
else:
    # Adicionar a camada ao projeto atual no QGIS
    QgsProject.instance().addMapLayer(camada_vetor)
    print("Camada carregada com sucesso!")

    # Obter a lista de valores únicos de um campo (por exemplo, campo "unidade")
    campo_categoria = 'Dominios'  # Campo que contém as unidades
    valores_unicos = camada_vetor.uniqueValues(camada_vetor.fields().lookupField(campo_categoria))

    # Definir uma lista para armazenar as categorias
    categorias = []

    # Gerar cores únicas para cada unidade
    for valor in valores_unicos:
        # Criar um símbolo padrão
        simbolo = QgsSymbol.defaultSymbol(camada_vetor.geometryType())
        
        # Gerar uma cor aleatória
        cor = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        # Aplicar a cor ao símbolo
        simbolo.setColor(cor)
        
        # Criar a categoria (valor, símbolo, rótulo)
        categoria = QgsRendererCategory(valor, simbolo, str(valor))
        categorias.append(categoria)

    # Criar o renderer categorizado
    renderer_categorizado = QgsCategorizedSymbolRenderer(campo_categoria, categorias)

    # Aplicar o renderer à camada
    camada_vetor.setRenderer(renderer_categorizado)
    
    # Atualizar a interface do QGIS para exibir as alterações
    camada_vetor.triggerRepaint()
    iface.mapCanvas().refreshAllLayers()

    # Configurar os rótulos (continuação do script anterior)
    rotulos_config = QgsPalLayerSettings()
    rotulos_config.fieldName = 'Dominios'  # Defina o campo dos rótulos
    
    rotulos_config.enabled = True
    texto_formatado = QgsTextFormat()
    texto_formatado.setFont(QFont("Arial", 10))
    texto_formatado.setSize(10)
    rotulos_config.setFormat(texto_formatado)
    
    camada_vetor.setLabelsEnabled(True)
    camada_vetor.setLabeling(QgsVectorLayerSimpleLabeling(rotulos_config))
    camada_vetor.triggerRepaint()

