# InvestProperty AI - Análisis Inteligente de Inversiones Inmobiliarias

## 📋 Descripción General

**InvestProperty AI** es una aplicación web diseñada para analizar inversiones inmobiliarias utilizando simulaciones Monte Carlo. La plataforma permite a los usuarios evaluar el potencial de inversión de propiedades mediante cálculos avanzados de ROI (Retorno de Inversión), VPN (Valor Presente Neto) y análisis de escenarios probabilísticos.

## 🎯 Objetivo del Proyecto

El objetivo principal de este proyecto es proporcionar una herramienta accesible y poderosa para que inversores, tanto principiantes como experimentados, puedan tomar decisiones informadas sobre inversiones inmobiliarias basándose en análisis estadísticos y proyecciones financieras.

## 🚀 Características Principales

- **Análisis con Simulaciones Monte Carlo**: Ejecuta 10,000 escenarios probabilísticos para calcular resultados realistas
- **Métricas Financieras Completas**: Calcula ROI, VPN, valor proyectado de la propiedad y ganancias totales
- **Análisis de Escenarios**: Proporciona análisis de mejor caso, peor caso y escenarios esperados
- **Recomendaciones de Inversión**: Genera recomendaciones automáticas basadas en los resultados del análisis
- **Interfaz Moderna y Responsive**: Diseño limpio y profesional que funciona en dispositivos móviles y de escritorio
- **Completamente en Español**: Toda la interfaz y documentación están en español

## 📁 Estructura del Proyecto

```
RealStateAI/
│
├── index.html          # Página principal con formulario de análisis
├── results.html        # Página de resultados del análisis
├── about.html          # Página informativa sobre el proyecto
└── README.md           # Este archivo
```

### Descripción de Archivos

- **index.html**: Página principal que contiene:
  - Sección hero con presentación del proyecto
  - Formulario de entrada de datos de la propiedad
  - Sección de características y beneficios
  - Navegación entre páginas

- **results.html**: Página de resultados que muestra:
  - Valor Presente Neto (VPN)
  - Retorno de Inversión (ROI)
  - Valor proyectado de la propiedad
  - Ganancia total
  - Mejor y peor escenario
  - Recomendación de inversión

- **about.html**: Página informativa que explica:
  - La misión del proyecto
  - Cómo funciona el análisis
  - Por qué usar simulaciones Monte Carlo
  - Estadísticas y características del sistema

## 🛠️ Tecnologías Utilizadas

- **HTML5**: Estructura semántica de las páginas
- **CSS3**: Estilos modernos con variables CSS, gradientes y diseño responsive
- **Formularios HTML**: Captura de datos del usuario (preparado para integración con Flask)

## 📊 Parámetros de Análisis

El formulario captura los siguientes datos de la propiedad:

- **Precio de la Propiedad**: Valor total de la propiedad
- **Enganche (%)**: Porcentaje de pago inicial
- **Tasa de Interés (%)**: Tasa de interés de la hipoteca
- **Plazo de Hipoteca (años)**: Duración del préstamo hipotecario
- **Renta Mensual ($)**: Ingreso mensual por alquiler
- **Apreciación Anual (%)**: Tasa de apreciación esperada de la propiedad
- **Gastos Anuales (%)**: Porcentaje del valor de la propiedad en gastos anuales
- **Período de Inversión (años)**: Tiempo que se mantendrá la inversión
- **Ubicación de la Propiedad**: Ubicación geográfica de la propiedad

## 🔄 Flujo de Trabajo Actual

1. **Entrada de Datos**: El usuario completa el formulario en `index.html`
2. **Envío del Formulario**: Los datos se envían mediante método GET a `results.html`
3. **Visualización de Resultados**: La página `results.html` muestra los resultados (actualmente con placeholders)

## 🔮 Próximos Pasos - Integración con Flask

El proyecto está preparado para integrarse con **Flask** para el procesamiento del análisis:

### Funcionalidades Planificadas:

1. **Backend con Flask**:
   - Captura de datos del formulario
   - Implementación de simulaciones Monte Carlo en Python
   - Cálculo de métricas financieras
   - Generación de recomendaciones

2. **Procesamiento de Datos**:
   - Validación de entrada
   - Cálculos financieros precisos
   - Análisis estadístico de resultados
   - Generación de reportes

3. **Mejoras Futuras**:
   - Base de datos para historial de análisis
   - Exportación de resultados a PDF
   - Comparación de múltiples propiedades
   - Gráficos y visualizaciones interactivas

## 🎨 Diseño

El proyecto utiliza un diseño moderno con:
- **Paleta de Colores**:
  - Color primario: `#2d3561` (azul oscuro)
  - Color secundario: `#6366f1` (índigo)
  - Color de acento: `#10b981` (verde esmeralda)
  
- **Características de Diseño**:
  - Gradientes modernos
  - Bordes redondeados
  - Sombras suaves
  - Transiciones suaves
  - Diseño responsive (mobile-first)

## 📱 Compatibilidad

- ✅ Navegadores modernos (Chrome, Firefox, Safari, Edge)
- ✅ Dispositivos móviles (responsive design)
- ✅ Tablets y escritorio

## 🚦 Cómo Usar (Versión Actual)

1. Abre `index.html` en tu navegador web
2. Completa el formulario con los datos de la propiedad
3. Haz clic en "Analizar Inversión"
4. Serás redirigido a `results.html` (actualmente muestra placeholders)

## 📝 Notas de Desarrollo

- El proyecto actualmente no tiene JavaScript para el procesamiento
- Los resultados se mostrarán cuando se integre Flask
- El formulario está configurado para enviar datos mediante GET
- Todos los campos del formulario tienen validación HTML5 (`required`)

## 📄 Licencia

Este proyecto es de uso educativo y personal.

## 👥 Contribuciones

Este es un proyecto en desarrollo. Las contribuciones y sugerencias son bienvenidas.

## 📧 Contacto

Para preguntas o sugerencias sobre el proyecto, por favor contacta al equipo de desarrollo.

---

**Desarrollado con ❤️ para ayudar a tomar mejores decisiones de inversión inmobiliaria**

