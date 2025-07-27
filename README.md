# Plugin-Qgis
Plugin for Qgis
# Marcos de plantación

Este complemento permite generar automáticamente puntos dentro de polígonos seleccionados, simulando marcos de plantación. 

## Funcionalidades

- Distribución de puntos en patrón:
  - Rectangular
  - Tresbolillo
  - Real
- Orientación personalizada mediante ángulo definido por el usuario.
- Parámetro de distancia entre plantas (en metros).

## Uso

1. Selecciona una capa de polígonos y las geometrías deseadas.
2. Ejecuta el complemento desde el menú `Complementos > Marcos de plantación`.
3. Define:
   - Distancia entre puntos
   - Tipo de distribución
   - Ángulo de orientación
4. El complemento generará una nueva capa de puntos con los parámetros especificados.

## Requisitos

- QGIS 3.x

## Autor

- mlucia
- www.linkedin.com/in/manuel-lucia-fourcade-4525771b4

## Licencia

Este plugin se publica bajo la licencia GNU GPL v3.

IN ENGLISH:

# Planting Grids

This QGIS plugin generates planting points within selected polygons, allowing for flexible configurations including spacing, distribution pattern, and orientation.

## Features

- Generates evenly spaced points inside selected polygons.
- Supports three distribution patterns:
  - Rectangular
  - Staggered (Tresbolillo)
  - Real
- Custom angle for grid orientation (in degrees).
- User-defined spacing between points (in meters).
- Outputs a new memory layer with the generated points.

## How to Use

1. Select a polygon layer and the polygons where you want to place points.
2. Open the plugin via `Plugins > Planting Grids`.
3. Enter:
   - Distance between planting points
   - Distribution type
   - Rotation angle
4. A new point layer will be added to the map with the specified configuration.

## Requirements

- QGIS 3.x
