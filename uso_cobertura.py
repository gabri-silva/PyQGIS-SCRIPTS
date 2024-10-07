"""
Autor: Gabriel Almeida da Silva
Título: Área de Preservação Ambiental - Uso e Cobertura
Ano: 2023

Descrição:
Este script define um dicionário contendo características de uso e cobertura do solo
em áreas de preservação ambiental, associado a cores em formato hexadecimal.

O script foi utilizado para definição do uso e cobertura da APANA - Araguaína-TO
O script pode ser editado para  diferentes finalidades e análises de uso e cobertura
"""

from qgis.core import (
    QgsApplication,
    QgsRasterLayer,
    QgsVectorLayer,
    QgsProcessingFeatureSourceDefinition,
    QgsProcessingAlgorithm,
    QgsProcessingParameterRasterLayer,
    QgsProcessingParameterVectorLayer,
    QgsProcessingParameterString,
    QgsProcessingParameterNumber,
    QgsProject,
    QgsProcessing,
    QgsRasterCalculator,
    QgsRasterCalculatorEntry,
    QgsFillSymbol,
    QgsCategorizedSymbolRenderer
)

# Inicializa o QGIS (se não estiver rodando em um ambiente QGIS)
QgsApplication.setPrefixPath('/caminho/para/o/qgis', True)  # ajuste o caminho para o QGIS
QgsApplication.initQgis()

# Caminhos dos arquivos
tiff_file_path = '/caminho/para/imagem.tif' #caminho imagem tif
shapefile_path = '/caminho/para/area_de_estudo.shp' #caminho shapefile

# Carregar imagem TIFF
raster_layer = QgsRasterLayer(tiff_file_path, 'Imagem TIFF')
if not raster_layer.isValid():
    print("Falha ao carregar a imagem TIFF.")
else:
    QgsProject.instance().addMapLayer(raster_layer)

# Carregar shapefile
vector_layer = QgsVectorLayer(shapefile_path, 'Área de Estudo', 'ogr')
if not vector_layer.isValid():
    print("Falha ao carregar o shapefile.")
else:
    QgsProject.instance().addMapLayer(vector_layer)

# Recortar imagem TIFF pela área de estudo
processing.run("gdal:cliprasterbymasklayer", {
    'INPUT': tiff_file_path,
    'MASK': shapefile_path,
    'OUTPUT': '/caminho/para/imagem_recortada.tif'
})

# Atribuir valores de cor
# Dicionário para atribuição de cores em hexadecimal
caracteristicas = {
    #Coleção 8 - Classes MapBiomas <https://brasil.mapbiomas.org/wp-content/uploads/sites/4/2023/08/Legenda-Colecao-8-LEGEND-CODE.pdf>
    #Floresta
    "Floresta": "#32a65e",
    "Formação Florestal": "#1f8d49",
    "Formação Savânica": "#7dc975",
    "Mangue": "#04381d",
    "Floresta Alagável (beta)": "#026975",
    "Restinga Arbórea": "#02d659",

    #Formação Natural não florestal
    "Formação Natural não Florestal": "#ad975a",
    "Campo Alagado e Área Pantanosa": "#519799",
    "Formação Campestre": "#d6bc74",
    "Apicum": "#fc8114",
    "Afloramento Rochoso": "#ffaa5f",
    "Restinga Herbácea": "#ad5100",
    "Outras Formações não Florestais": "#d89f5c",

    #Agropecuária
    "Agropecuária": "#FFFFB2",
    "Pastagem": "#edde8e",
    "Agricultura": "#E974ED",
    "Lavoura Temporária": "#C27BA0",
    "Soja": "#f5b3c8",
    "Cana": "#db7093",
    "Arroz": "#c71585",
    "Algodão (beta)": "#ff69b4",
    "Outras Lavouras Temporárias": "#f54ca9",
    "Lavoura Perene": "#d082de",
    "Café": "#d68fe2",
    "Citrus": "#9932cc",
    "Dendê (beta)": "#9065d0",
    "Outras Lavouras Perenes": "#e6ccff",
    "Silvicultura": "#7a5900",
    "Mosaico de Usos": "#ffefc3",

    #Área não vegetada
    "Área não Vegetada": "#d4271e",
    "Praia, Duna e Areal": "#ffa07a",
    "Área Urbanizada": "#d4271e",
    "Mineração": "#9c0027",
    "Outras Áreas não Vegetadas": "#db4d4f",

    #Corpos D'Água
    "Corpo D'água": "#0000FF",
    "Rio, Lago e Oceano": "#2532e4",
    "Aquicultura": "#091077",
    "Não observado": "#ffffff"
}

# Criar uma nova camada categorizada
renderer = QgsCategorizedSymbolRenderer('class', [])
for label, color in caracteristicas.items():
    symbol = QgsFillSymbol.createSimple({'color': color})
    item = QgsRendererRange(label, label, symbol)
    renderer.addCategory(item)

# Aplicar o renderer à camada
vector_layer.setRenderer(renderer)

# Salvar o projeto
QgsProject.instance().write('/caminho/para/projeto.qgs')

# Finaliza o QGIS
QgsApplication.exitQgis()
