# Análisis de Vehículos en Venta - Aplicación Web

Este proyecto contiene una aplicación web interactiva construida con Streamlit para visualizar datos de anuncios de venta de vehículos.

## Estructura del Proyecto

```
├── app.py                 # Aplicación Streamlit principal
├── vehicles_us.csv        # Conjunto de datos de vehículos
├── requirements.txt       # Dependencias del proyecto
├── notebooks/
│   └── EDA.ipynb         # Jupyter notebook con análisis exploratorio
└── README.md             # Este archivo
```

## Requisitos

- Python 3.9 o superior
- Las dependencias listadas en `requirements.txt`

## Instalación

1. Crear un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar la aplicación Streamlit

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

### Jupyter Notebook

Para explorar el análisis exploratorio de datos:

```bash
jupyter notebook notebooks/EDA.ipynb
```

## Funcionalidades

- **Histograma del Odómetro**: Visualiza la distribución del kilometraje de los vehículos
- **Gráfico de Dispersión**: Muestra la relación entre el odómetro y el precio
- **Histograma de Precios**: Distribución de precios de los vehículos
- **Distribución por Condición**: Gráfico de barras mostrando la cantidad de vehículos por condición

## Controles

La aplicación ofrece dos formas de generar gráficos:
1. **Casillas de verificación**: Selecciona múltiples gráficos para mostrar simultáneamente
2. **Botones**: Genera gráficos individuales al hacer clic

## Tecnologías

- [Streamlit](https://streamlit.io/) - Framework para aplicaciones web de datos
- [Plotly](https://plotly.com/python/) - Biblioteca de visualización interactiva
- [Pandas](https://pandas.pydata.org/) - Manipulación y análisis de datos
