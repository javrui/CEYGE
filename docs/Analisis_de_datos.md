
# Análisis de Datos

## Entidades

- peticionarios
- obras
- muestras
- ensayos
- registros de ensayo
- expedientes
- informes


Para cada entidad, determinar:

- Nombre de campo
- descripción
- tipo de dato
- unidades de medida
- rango o controles de entrada del dato
- procedencia (usuario, fichero de configuracion, )
- ,,,


## Atributos

peticionario:

- peticionario.cif ?
- peticionario.nombre
- peticionario.dirección

obra:

- obra.id
- obra.nombre
- obra.direccion

ensayo:

- ensayo.id
- ensayo.nombre
- ensayo.norma
- ensayo.parametros_de_norma
- ENTIDAD NO GESTIONABLE POR USUARIO, FICH CONFIG

expediente:

- expediente.año
- expediente.id_secuencial
- expediente.peticionario
- expediente.obra
- expediente.ensayos
- expediente.muestras
- expediente.clasificacion_final

muestra:

- muestra.identificador_ceyge
- muestra.fecha_de_toma
- muestra.nombre

registro de ensayo:

- registro.ensayo.id
- registro.muestra.identificador_ceyge
- registro.valores
- registro.es_simulado

informe:

- informe.peticionario.cif?
- informe.obra.id
- informe.ensayos
- informe.MUESTRAS
- informe.

Se definirán una serie de controles para la introducción de cada dato, minimizando la posibilidad de errores tipográficos comunes.



## Relaciones
