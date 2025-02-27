# Aplicación de gestión de informes geotécnicos para CEYGE

## Introducción

CEYGE es una empresa acreditada para la realización de estudios  geotécnicos, ensayos de laboratorio y control de calidad de materiales de construcción. Ubicada en Madrid (Móstoles) con plantilla de aproximadamente 40 empleados.

Entre su actividad, se encuentra la elaboración de informes técnicos de calificación de suelos, en base a ensayos de su propio laboratorio y los criterios establecidos por normativas técnicas como el Pliego General de Condiciones para las Obras de Carreteras y Puentes (PG3) o Pliegos equivalentes.


## Motivación

Los mencionados informes geotécnicos se están realizando en la actualidad a partir de hojas excel. Su tratamiento es laborioso y propenso a errores, pues la gestión de expedientes se realiza copiando y pegando datos en hojas excel. Estas hojas  generan 3 archivos .pdf que posteriormente hay que fundir en un .pdf único entregable a cliente.

Por otro lado, para realizar una simulación de la gráfica de ciertos ensayos, que permita valorar cuánto se aleja el terreno de condiciones ideales, el sistema actual  requiere ir probando sucesivamente valores numéricos en las correpondientes celdas del excel hasta encontrar el que mejor se ajusta a la forma deseada para la curva. No es posible la interacción directa del usuario con la gráfica del ensayo.


## Conceptos
En estas especificaciones se usarán reiradamente estos conceptos, con el significado que se indica:

- **Peticionario**

    Persona o entidad que solicita el informe geotécnico.

- **Obra**

    Proyecto o emplazamiento donde se toman las muestras de suelo para su análisis.

- **Muestra**

    Porción de terreno extraída en la obra para su estudio geotécnico.

- **Método de ensayo**

      Conjunto de procedimientos normalizados que regulan la ejecución de una prueba experimental, incluyendo las condiciones de ensayo, los parámetros a medir, el equipamiento requerido y la metodología para la obtención e interpretación de los resultados.
      Está definido por una norma técnica, Ejemplo: UNE 103-502-94 (ensayo CBR en laboratorio), ASTM D3080 (ensayo de corte directo).

- **Registro de ensayo**

      Se refiere a la ejecución de un *método de ensayo* sobre una *muestra* específica, bajo unas *variables de control*, que permite obtener unas *magnitudes medidas* y unos  *resultados*. (Son lso 3 conmceptos que a continuación se detallan).
      Ejemplo: "Ensayo CBR realizado según UNE 103-502-94 sobre una muestra de suelo extraída a 1.5 m de profundidad, compactada al 95% de la densidad máxima Proctor con un contenido de humedad del 12%, inmersa en agua durante 96 horas antes del ensayo y ensayada a una velocidad de penetración de 1 mm/min, registrando la carga aplicada (kN) para cada nivel de penetración estándar (0.625 mm, 1.25 mm, 2.5 mm, 5 mm, 7.5 mm, 10 mm), obteniendo como resultado un índice CBR del X% a 2.5 mm de penetración y del Y% a 5 mm, junto con la curva carga-deformación correspondiente.".


- **Variables de control**

    Son los factores que pueden ser ajustados o controlados durante la ejecución del ensayo.
    Ejemplo: contenido de humedad, carga normal aplicada, gradiente hidráulico, tiempo de inmersión, tasa de deformación.

- **Magnitudes medidas**

    Son los valores obtenidos directamente de los instrumentos de medición durante la ejecución del ensayo y que permiten el cálculo de los parámetros geotécnicos resultantes.
    Ejemplo: carga aplicada (kN), desplazamiento (mm), caudal de agua (cm³/s), deformación unitaria (%).

- **Resultados del ensayo**

    Son las magnitudes derivadas del análisis del ensayo y que caracterizan el comportamiento del suelo. Ejemplo: índice CBR (%), coeficiente de permeabilidad (cm/s), cohesión (kPa), ángulo de fricción interna (°).

- **Norma**

    Estándar técnico aplicado en la ejecución del ensayo (ejemplo: UNE 103 101:1995).

- **Expediente**

    Conjunto estructurado de documentos, datos y registros relacionados con un estudio geotécnico. Contempla uno o mas *registros de ensayo* sobre una o mas muestras.

- **Informe final**

    Documento en formato PDF entregado al cliente, que contiene los resultados y conclusiones del estudio geotécnico.

## Objetivos de la aplicación

- Automatizar la elaboración del informe final pdf entregable a cliente, proporcionando los mismos datos, cálculos y representaciones gráficas que los informes generados actualmente (u otros mejorados que se determinen)

- Utilizar un entorno gráfico de escritorio, con formularios propios de la aplicación, que sustituya a las hojas excel actuales.

- Realizar simulaciones de la representación gráfica de los registros de ciertos ensayos, que requieran valorar el grado de inadecuación de alguna característica del terreno. Se podrá interactar directamente con la representación gráfica, generándose de forma inmediata el recálculo automático de los datos de registro de ensayo simulado.

## Alcance

### Estudios geotécnicos contemplados

En esta primera fase:

- Estudios geotécnicos de **Suelos**
- Los expedientes pueden contener un número variable de ensayos de entre 14  posibles.
- La simulación gráfica será posible en 3 ensayos de estos 14.

## Requisitos funcionales

### Gestión de entidades

La aplicación tendrá su propia gestión de:

- peticionarios
- obras
- muestras
- ensayos
- registros de ensayo
- expedientes
- informes

Es decir, la aplicación permitirá el alta, baja, modificación y consulta de estos conceptos.

Los datos quedarán almacenados en disco como ficheros estructurados, pero no se utilizará una base de datos en esta primera versión.

### Simulación

La aplicación permitirá realizar la simulación y ajuste interactivo de respresentaciones gráficas de ciertos ensayos, almacenando los datos resultantes como registro simulado.

## Menús de la aplicación

(Por definir)

### Informe generado por la aplicación

La aplicación generará un único documento .pdf de informe entregable a cliente por expediente, con las mismas secciones actuales:

- Datos del expediente (Peticionario, obra, ensayos solicitados)
- Antecedentes (Datos relativos a la toma de muestra)
- Especificaciones PG-3 para la clasificación de suelos.
- Conclusiones (Clasificación PG-3)
- Actas de los ensayos (registro de ensayo, valores calculados, gráficas si procede)

## Ensayos: especificaciones de cálculo

Pendiente de definir

[Especificaciones_de_cada_ensayo](Especificaciones_de_cada_ensayo.md)

## Análisis de datos

[Análisis de datos](Analisis_de_datos.md)


## Entorno operativo de la aplicación

- Tipo de aplicación: escritorio, con interfaz gráfica propia.
- Tecnología softare: Python 3.x, QTSide, librerías avanzadas (matplotlib, numpy, scipy)
- Sistema operativo y versión en que correrá la aplicación: ¿Windows?
- Número de equipos en los que debe correr la aplicación: 1
- Número de equipos trabajando simultáneamente con la aplicación: 1

## Propiedad del software

El propietario del código será exclusivamenmte su desarrolador.
CEYGE no puede revender ni ceder el software a terceros.

## Nombre propuesto para la aplicación:

Se proponen como nombres para la aplicación:
- "GIGA" (Gestión de Informes Técnicos Automatizada")
- "GES" (Gestión de Expedientes de Suelos) - quizás demasiado limitado

## Ampliaciones posibles a la aplicación

[ampliaciones funcionales propuestas](ampliaciones_funcionales_propuestas.md)
