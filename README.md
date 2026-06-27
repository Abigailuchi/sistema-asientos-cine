# CineReserva - Sistema de Gestion de Asientos para Salas de Cine

**Trabajo Final - Logica de Programacion**

- **Estudiante:** Lincango Morocho Mayerly Abigail
- **Docente:** Cabezas Erazo Dario Sebastian
- **Fecha de entrega:** 27 de junio de 2026

En la actualidad la tecnologia esta metida en casi todo lo que hacemos,
aunque la mayoria de las veces ni nos damos cuenta. Para el trabajo
final de Logica de Programacion se pidio pensar en un problema real de
la vida diaria y resolverlo aplicando lo trabajado en las 4 unidades
del semestre. Despues de pensar en varias opciones, se eligio resolver
un problema bastante comun: la falta de organizacion al reservar
asientos en una sala de cine.

## Objetivo general
Desarrollar un sistema de reservas de asientos para una sala de cine
mediante un programa en Python, que permita gestionar de manera
sencilla la disponibilidad de asientos desde la consola, aplicando los
conocimientos adquiridos en la materia y relacionandolos con un
problema de la vida cotidiana.

## Objetivos especificos
- Analizar un problema real relacionado con la reserva de asientos en una sala de cine.
- Aplicar los conceptos aprendidos en las diferentes unidades de la materia.
- Reflexionar sobre el impacto de la tecnologia en la vida diaria.

## Descripcion de funcionalidades

| # | Funcionalidad | Descripcion |
|---|----------------|-------------|
| 1 | Ver asientos disponibles | Muestra el mapa completo de la sala (20 asientos, filas A-D) indicando cuales estan libres y cuales ocupados |
| 2 | Reservar un asiento | El usuario ingresa el codigo del asiento (ej. A1) y su nombre; el sistema valida que el asiento exista y este libre |
| 3 | Cancelar una reserva | Libera un asiento que estaba reservado |
| 4 | Consultar ocupacion | Muestra el total de asientos ocupados, libres y el porcentaje de ocupacion de la sala |
| 5 | Buscar una reserva | Busca por codigo de asiento o por nombre del cliente |
| 6 | Salir | Termina la ejecucion del programa |

## Metodologia
Primero se identifico y analizo el problema de la vida cotidiana
elegido. Despues se aplicaron los conocimientos de la materia para
pensar la solucion, se disenaron los diagramas (de funcionalidad y de
arquitectura) y, a partir de esos diagramas, se escribio el codigo,
haciendo pruebas y ajustes hasta confirmar que todo funcionara
correctamente.

## Estructura del repositorio
```
├── cine_reservas.py            # Codigo completo del sistema
├── diagramas/
│   ├── diagrama_funcionalidad.png   # Diagrama de flujo del programa
│   └── diagrama_arquitectura.png    # Diagrama de capas del sistema
├── documento_proyecto.docx     # Documento: introduccion, objetivos,
│                                # metodologia, resultados, reflexion
│                                # y conclusiones
└── README.md
```

## Como ejecutar el programa
1. Tener Python 3 instalado
2. Abrir una terminal en la carpeta del proyecto
3. Ejecutar:
   ```
   python cine_reservas.py
   ```
4. Usar el menu numerico (1-6) para navegar por las opciones

## Tecnologias y conceptos aplicados
Variables, operadores, bucles (`for`, `while`), condicionales
(`if/elif/else`), estructuras de datos (diccionarios), funciones,
manejo de errores (`try/except`) y control de versiones con
Git/GitHub.