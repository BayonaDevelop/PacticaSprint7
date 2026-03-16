"""
Aplicación Web de Análisis de Vehículos
========================================
Esta aplicación Streamlit permite visualizar datos de anuncios de venta de vehículos
mediante gráficos interactivos construidos con Plotly.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ============================================
# FUNCIONES DE VISUALIZACIÓN
# ============================================

def create_odometer_histogram(data):
    """Crea y muestra un histograma del odómetro."""
    st.write('### Distribución del Odómetro')
    st.write('Este histograma muestra la distribución del kilometraje de los vehículos en el dataset.')
    fig = go.Figure(data=[go.Histogram(
        x=data['odometer'],
        nbinsx=50,
        marker_color='steelblue',
        opacity=0.75
    )])
    fig.update_layout(
        title_text='Distribución del Odómetro',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Frecuencia',
        bargap=0.1
    )
    st.plotly_chart(fig, use_container_width=True)

def create_scatter_plot(data):
    """Crea y muestra un gráfico de dispersión de odómetro vs. precio."""
    st.write('### Relación entre Odómetro y Precio')
    st.write('Este gráfico de dispersión muestra la relación entre el kilometraje y el precio de los vehículos.')
    filtered_data = data[
        (data['price'] > 0) &
        (data['price'] < 150000) &
        (data['odometer'].notna())
    ]
    fig = go.Figure(data=[go.Scatter(
        x=filtered_data['odometer'],
        y=filtered_data['price'],
        mode='markers',
        marker=dict(
            size=6,
            color=filtered_data['price'],
            colorscale='Viridis',
            showscale=True,
            colorbar=dict(title='Precio (USD)')
        ),
        opacity=0.6
    )])
    fig.update_layout(
        title_text='Relación entre Odómetro y Precio',
        xaxis_title='Odómetro (millas)',
        yaxis_title='Precio (USD)'
    )
    st.plotly_chart(fig, use_container_width=True)

def create_price_histogram(data):
    """Crea y muestra un histograma de precios."""
    st.write('### Distribución de Precios')
    st.write('Este histograma muestra la distribución de precios de los vehículos.')
    filtered_prices = data[(data['price'] > 0) & (data['price'] < 100000)]
    fig = go.Figure(data=[go.Histogram(
        x=filtered_prices['price'],
        nbinsx=50,
        marker_color='coral',
        opacity=0.75
    )])
    fig.update_layout(
        title_text='Distribución de Precios de Vehículos',
        xaxis_title='Precio (USD)',
        yaxis_title='Frecuencia',
        bargap=0.1
    )
    st.plotly_chart(fig, use_container_width=True)

def create_condition_bar_chart(data):
    """Crea y muestra un gráfico de barras de la condición del vehículo."""
    st.write('### Distribución por Condición del Vehículo')
    condition_counts = data['condition'].value_counts().reset_index()
    condition_counts.columns = ['condition', 'count']
    fig = go.Figure(data=[go.Bar(
        x=condition_counts['condition'],
        y=condition_counts['count'],
        marker_color=['#2ecc71', '#3498db', '#9b59b6', '#e74c3c', '#f39c12', '#1abc9c']
    )])
    fig.update_layout(
        title_text='Distribución de Vehículos por Condición',
        xaxis_title='Condición',
        yaxis_title='Cantidad de Vehículos'
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================
# CONFIGURACIÓN Y CARGA DE DATOS
# ============================================
st.set_page_config(
    page_title="Análisis de Vehículos",
    page_icon="🚗",
    layout="wide"
)

@st.cache_data
def load_data(path):
    """Carga los datos desde un archivo CSV y los cachea."""
    return pd.read_csv(path)

car_data = load_data('vehicles_us.csv')

# ============================================
# ENCABEZADO PRINCIPAL
# ============================================
st.header('🚗 Análisis de Datos de Vehículos en Venta')

st.write("""
Esta aplicación permite explorar visualmente el conjunto de datos de anuncios de venta de vehículos.
Utiliza los controles a continuación para generar diferentes visualizaciones interactivas.
""")

# ============================================
# INFORMACIÓN GENERAL DEL DATASET
# ============================================
st.subheader('📊 Información General del Dataset')

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Vehículos", f"{len(car_data):,}")
with col2:
    st.metric("Precios Promedio", f"${car_data['price'].mean():,.0f}")
with col3:
    st.metric("Odómetro Promedio", f"{car_data['odometer'].mean():,.0f} mi")

# ============================================
# VISUALIZACIONES CON CASILLAS DE VERIFICACIÓN
# ============================================
st.subheader('📈 Visualizaciones Interactivas')

st.write("Selecciona las casillas de verificación para generar los gráficos:")

# Crear casillas de verificación
build_histogram = st.checkbox('Construir un histograma del odómetro')
build_scatter = st.checkbox('Construir un gráfico de dispersión (odómetro vs precio)')
build_price_histogram = st.checkbox('Construir un histograma de precios')
build_condition_bar = st.checkbox('Mostrar distribución por condición')

# ============================================
# HISTOGRAMA DEL ODÓMETRO
# ============================================
if build_histogram:
    create_odometer_histogram(car_data)

# ============================================
# GRÁFICO DE DISPERSIÓN
# ============================================
if build_scatter:
    create_scatter_plot(car_data)

# ============================================
# HISTOGRAMA DE PRECIOS
# ============================================
if build_price_histogram:
    create_price_histogram(car_data)

# ============================================
# GRÁFICO DE BARRAS POR CONDICIÓN
# ============================================
if build_condition_bar:
    create_condition_bar_chart(car_data)

# ============================================
# SECCIÓN DE BOTONES (ALTERNATIVA)
# ============================================
st.divider()
st.subheader('🎛️ Controles Alternativos con Botones')

st.write("Alternativamente, puedes usar los botones para generar gráficos individuales:")

col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    hist_button = st.button('Construir histograma del odómetro', type='primary')

    if hist_button:
        st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        create_odometer_histogram(car_data)

with col_btn2:
    scatter_button = st.button('Construir gráfico de dispersión', type='primary')

    if scatter_button:
        st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
        create_scatter_plot(car_data)

# ============================================
# PIE DE PÁGINA
# ============================================
st.divider()
st.caption('Aplicación desarrollada con Streamlit y Plotly | Datos: vehicles_us.csv')
