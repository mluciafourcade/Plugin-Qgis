# Importar módulos necesarios de PyQGIS
from qgis.core import QgsPointXY, QgsVectorLayer, QgsFeature, QgsGeometry, QgsField, QgsFields, QgsWkbTypes, QgsProject
from PyQt5.QtCore import QVariant
from math import cos, sin, radians

# Parámetros de usuario
distancia_entre_puntos = 3  # metros
tipo_distribucion = "tresbolillo"  # "real", "tresbolillo" o "rectangular"
angulo = 30  # en grados, orientación del marco de plantación

# Obtener la capa de polígonos seleccionada
capa_poligonos = iface.activeLayer()
if not capa_poligonos or capa_poligonos.geometryType() != QgsWkbTypes.PolygonGeometry:
    raise Exception("Selecciona una capa de polígonos válida")

# Obtener las características seleccionadas
poligonos_seleccionados = capa_poligonos.selectedFeatures()
if not poligonos_seleccionados:
    raise Exception("No hay polígonos seleccionados")

# Crear nueva capa de puntos
nombre_capa_puntos = f"Capa_Puntos_{tipo_distribucion.capitalize()}"
capa_puntos = QgsVectorLayer(f"Point?crs={capa_poligonos.crs().authid()}", nombre_capa_puntos, "memory")
capa_puntos_provider = capa_puntos.dataProvider()

# Definir campos
campos = QgsFields()
campos.append(QgsField("ID", QVariant.Int))
capa_puntos_provider.addAttributes(campos)
capa_puntos.updateFields()

id_punto = 1

# Función para rotar punto respecto al centro
def rotar_punto(x, y, cx, cy, angulo):
    ang_rad = radians(angulo)
    x_rot = cos(ang_rad) * (x - cx) - sin(ang_rad) * (y - cy) + cx
    y_rot = sin(ang_rad) * (x - cx) + cos(ang_rad) * (y - cy) + cy
    return x_rot, y_rot

# Función para generar puntos
def agregar_puntos(x_min, y_min, x_max, y_max, geometria_poligono, tipo_distribucion, angulo):
    global id_punto
    centro = geometria_poligono.centroid().asPoint()
    y = y_min
    fila_par = True

    while y < y_max:
        x = x_min
        if tipo_distribucion == "tresbolillo" and not fila_par:
            x += distancia_entre_puntos / 2

        while x < x_max:
            # Rotar el punto alrededor del centro
            x_rot, y_rot = rotar_punto(x, y, centro.x(), centro.y(), angulo)
            punto = QgsPointXY(x_rot, y_rot)
            if geometria_poligono.contains(QgsGeometry.fromPointXY(punto)):
                nueva_feature = QgsFeature()
                nueva_feature.setGeometry(QgsGeometry.fromPointXY(punto))
                nueva_feature.setAttributes([id_punto])
                capa_puntos_provider.addFeature(nueva_feature)
                id_punto += 1
            x += distancia_entre_puntos

        y += distancia_entre_puntos * (3**0.5) / 2 if tipo_distribucion == "tresbolillo" else distancia_entre_puntos
        fila_par = not fila_par

# Iterar sobre los polígonos seleccionados
for poligono in poligonos_seleccionados:
    geometria_poligono = poligono.geometry()
    x_min, y_min, x_max, y_max = geometria_poligono.boundingBox().toRectF().getCoords()
    agregar_puntos(x_min, y_min, x_max, y_max, geometria_poligono, tipo_distribucion, angulo)

# Agregar la capa al proyecto
QgsProject.instance().addMapLayer(capa_puntos)

print(f"Capa de puntos creada con orientación de {angulo}°, distribución '{tipo_distribucion}' y distancia de {distancia_entre_puntos} m.")
