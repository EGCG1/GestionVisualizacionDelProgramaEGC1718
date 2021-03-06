# Gestión Visualizacion Del Programa EGC 17/18
Repositorio para llevar a cabo el trabajo sobre Gestión de visualización del programa, de la asignatura de EGC 17/18

https://programa-egc.herokuapp.com/

# Grupo 2

# ID de opera: grupo 23 (en la url el 96)

Integrantes del grupo:
- Juan Pablo Argote Ortiz
- Jesús Enrique Bozada Márquez
- Alejandro Gallego Segura
- Anastasio Rafael Leon Gonzalez
- Jesus Sosa Sánchez

Para instalar dependecias necesarias: 
```
pip install -r requirements.txt
```

### Introducción y contexto
El grupo de gestión y visualización del programa, será el encargado de mostrar de manera clara y sencilla el programa de las jornadas. Mostrando información sobre la fecha ,el horario ,el ponente ,el lugar ,el tipo de la acividad si es taller o una charla y una pequeña descripción sobre dicha actividad . Además se podrán gestionar dichos eventos pudiendolos añadir a sistemas como Twitter, Telegram, Google Calendar, exportarlos a PDFs o verlos en una aplicación Android.

### Descripción del sistema


### Planificación del proyecto

La planificación realizada en este proyecto ha estado orientada al seguimiento por parte de los profesores en los diferentes Milestones, por tanto, se presentará dividida en secciones siguiendo el orden de éstos.

#### Milestone 1 - Ecosistema preparado.

El objetivo principal que se propone cumplir antes de este milestone es la realización de una o más reuniones con objetivo de conocernos como equipo, llegar a un acuerdo de la idea a desarrollar y de las trazas generales que se deben seguir para este cometido.

En el trascurso de estas reuniones se ha decido utilizar un grupo de Telegram como canal principal de comunicación debido a la situación laboral de tres componentes del grupo. Adicionalmente se decidió que la gestión de tareas se realice a través de GitHub, como se detallará más adelante.

Dentro de las tareas a realizar durante este periodo de tiempo, se debe destacar la de conocimiento de dependencias con otros subsistemas del proyecto general. Esperando recabar dicha información a través del equipo de integración.

#### Milestone 2 - Sistema funcionando con incremento.

Se aprovecha la revisión del Milestone 1 para aclarar cuales son las líneas que debe seguir el proyecto para adaptarse a las dependencias encontradas.

Se prevee la utilización de una API aportada por otro equipo de trabajo, por tanto, se decide realizar durante este periodo de tiempo labores de estudio sobre las tecnologías, mientras el otro equipo aporta mayor información en cuanto a dicha API.

Se realizará una instanciación base de un proyecto de Python sobre Django por Alejandro, debido a sus conocimientos, para que los demás compañeros puedan avanzar en un futuro en las siguientes funcionalidades:
- Mostrar programa por Twitter. (Jesús)
- Mostrar programa por Telegram. (Anastasio)
- Mostrar programa en formato pdf. (Alejandro)
- Mostrar programa como Calendar de Google. (Enrique)
- Mostrar programa en una aplicación Android. (Juan Pablo)

En cuanto a la gestión de tareas se decide utilizar las issues de GitHub que serán gestionadas como cards desde la vista de Proyecto del repositorio, una tarea podrá encontrarse en tres fases diferentes:

- **ToDo:** aquellas tareas que están pendientes de su comienzo.

- **In progress:** aquellas tareas que ya han comenzado.

- **Done:** aquellas tareas que han sido terminadas. 

#### Milestone 3 - Taller de automatización.

De cara a este Milestone, debido a un gran retraso en las funcionalidades, causado por la ausencia de la API que debe ser proporcionada por el equipo de programa, se decide implementar las funcionalidades en torno a ficheros de hoja de cálculo de excel.

Las principales tareas planificadas para este periodo de tiempo serán la implementación de una base de datos SQLite, en la que introducir la información del programa que se obtendrá de dichos ficheros de hoja de cálculo. El estudio de que herramientas utilizar para la automatización de la construcción, la ejecución de pruebas y la integración.

#### Milestone 4 - Entrega y defensa de trabajos.

Para este Milestone, tras la revisión del anterior con el profesor, se llega a la conclusión de que se debe comenzar a realizar las labores de pruebas, integración y automatización sin dejar atras la funcionalidad, debido al retraso existente. Por tanto, se decide que los componentes del grupo continuen el desarrollo de sus funcionalidades hasta la realización de una reunión una semana del Milestone para comenzar en común las tareas mencionadas anteriormente.

Debido a una interacción con el grupo de programa en el que se aporta, por parte de ellos, una posible solución a la ausencia de API que consumir, se estudia la posibilidad de cambiar el desarrollo para adaptarlo a la propuesta, debido a la falta de tiempo y el retraso acumulado se decide ignorar la propuesta y continuar con la planificación actual.

Por último, de cara a la entrega se decide avanzar lo máximo posible en las tareas comunes para el beneficio de todos los componentes del grupo por encima del avance en las tareas individuales

### Entorno de desarrollo
A continuación se describen los entornos de desarrollo utilizados por el equipos. Se presentan dos diferentes debido a las necesidades del proyecto.

En primer lugar, se describe el entorno utilizado para desarrollar las funcionalidades la aplicación en python:
- **JetBrains PyCharm:** versión 2017.2.4 x64.
- **Python:** versión 2.7.
- **SQLite:** versión 3.10.1.
- **Django:** versión 1.11.8.
- **TravisCI**.
	
Por último, se describe el entorno utilizado para desarrollar la aplicación en android:
- **Android Studio:** versión 3.0.1 build #AI-171.4443003.
- **JRE:** 1.8.0_152-release-915-b01 amd64.
- **JVM:** OpenJDK 64-Bit.
- **SQLite:** versión 3.10.1.
- **TravisCI**.

### Gestión del cambio, incidencias y depuración
Para la gestión de incidencias se realiza mediante **issues** de **Github**. Se crearán en caso de que se vaya a realizar un avance o cambio en el proyecto, incluido los errores que aparezcan o tareas que se vayan a desempeñar.
Para la creación de éstas hemos utilizado la siguiente plantilla:
- Título breve y descriptivo mediante el cual se identifique bien el contenido que va a tener esa incidencia.
- Descripción en la que se explique el problema que ha tenido o la tarea realizada.
- Error: adjuntar error en el caso de que exista
- Prioridad: baja, media, alta y urgente 
- Etiqueta
- Proyecto asociado
- Hito correspondiente
- Miembro o miembros que la han creado, en el caso de que se tenga alguna duda o encuentre un problema se asignará a todos los miembros del grupo ya sea para que se resuelva con la mayor rapidez posible o bien por si alguien en concreto no supiera resolverlo.  En caso de que se encuentre un “bug” se adjuntará el error encontrado en la descripción de la incidencia.
La incidencia solo se cerrará en el caso de que se esté seguro que se ha terminado o se haya solucionado, todos los miembros podrán añadir comentarios si lo ven oportuno.

Etiquetas utilizadas:
- Desarrollo
- Documentación
- Planificación
- Despliegue
- Bug
- Otros
- Formación
- Reunión

Tareas:
La gestión de las tareas se controlará mediante el tablero proporcionado por **Github**, por lo que estas pasarán por tres estados que se irán modificando manualmente según sea oportuno: **To Do**, **In Progress** y **Done**.

 

### Gestión del código fuente
Para la gestión del código se usa la herramienta Git, utilizándola para realizar commits en el repositorio situado en la plataforma **Github**.

Commit
Se realizará un **commit** cuando se obtenga un avance importante en el proyecto o se solucione algún error. Para esto se utilizará los siguientes comandos (se tendrá en cuenta la rama en la que se está situado):
- ```git status``` 				 # detectar modificación de archivos
- ```git add <nombre del fichero modificado>``` o ```git add .```
- ```git commit -m “comentario de la nueva modificación #(número de la incidencia)”```
- ```git push origin <rama>```  		# publicar el commit en el repositorio Github
- ```git checkout <nombreArchivo>``` 	# para revertir un cambio antes de haber hecho un push
- ```git log -p```				# listar todos los commits realizados

Ramas
Para tener un mejor control de las funcionalidades, se ha creado una rama por cada una, existiendo en total 4 ramas secundarias y 1 rama principal:
- master (principal)
- twitter
- pdf
- telegram
- aplicación Android (puesto que se desarrolla en otro lenguaje y no tiene nada que ver con las demás funcionalidades se encuentra en un repositorio aparte.

Comandos utilizados en las ramas:
- ```git branch```			# ver la rama en la que estás situado
- ```git branch <nombreRama>```	# crear una nueva rama
- ```git checkout <nombreRama>``` 	# para cambiar de rama
- ```git merge <nombreRama>```	# unir la rama que se le pasa a la que estas situado
No se realizará ningún **merge** a la rama principal (master) hasta que no esté totalmente completa la funcionalidad y haya pasado todas las pruebas necesarias.

Conexión entre incidencias y commits
Cada vez que se lleva a cabo un commit importante sobre alguna de las ramas, este será añadido en la incidencia, ya que **Github** permite localizar los commits mediante su ‘ID’ y si este se copia en la **issue** correspondiente, se enlazan ambos.
Para los últimos commit se utilizó una forma mejor de enlazar ambas y es añadidiendo el #(número de la incidencia) en el comentario a la hora de llevar a cabo el commit.


### Gestión de la construcción e integración continua
Para la gestión de la construcción no hemos basado en el gestor de paquetes y librerias de python ***pip*** en su versión **9.0.1**. Con lo que si necesitabamos alguna librería ejecutabamos el siguiente código ```pip install <nombre de la librería>```, con esto ya la tendríamos disponible para usarla.

En cuanto a la gestión de la integración continua hemos utilizado ***Travis Cl*** iteraccionando con nuestro repositorio de ***GitHub*** de tal manera que el proceso utilizado es el siguiente:
- Creación del fichero **.travis.yml**.
- Trabajar en dicha rama y hacer commit.
- Travis se encarga de bajarse es último commit.
- Le ejecuta los correspondientes tests.
- Por último, vuelve a arrancar servidor de nuestra aplicación.

Pasando unos tests, que se configura en el **.travis.yml** para que este funcione correctamente.

### Gestión de liberaciones, despliegue y entregas

**Gestión de liberaciones**

La liberación continua la gestionamos mediante el servicio ***Travis CI***, utilizado para probar nuestro proyecto alojado en el repositorio de ***GitHub***. Para ello hacemos un fork al repositorio de ***GitHub*** y en ***Travis CI*** sincronizamos el mismo. Una vez hecho esto, automatizadas las pruebas del código, procedemos a ejecutarlas. ***Travis CI*** nos notifica por correo electrónico el resultado de la prueba, tanto si haya tenido éxito como con la aparición de un fallo. Si ha tenido éxito lo consideraremos como una nueva versión del código.

**Gestión de Despliegue**

 Una vez se haya pasado las pruebas de ***Travis CI***, el archivo ***.travis.yml*** establecerá la nueva versión y se actualizará en nuestro servidor que será ***Heroku***.

**Política de nombrado e identificación de los entregables**

El entregable completo se realizará en nuestro repositorio de ***GitHub***, donde el documento podrá encontrarse en el archivo ***README.md***

### Mapa de herramientas

![Mapa de herramientas](https://github.com/enruiq/GestionVisualizacionDelProgramaEGC1718/blob/master/Documentacion/Imagenes/Herramientas.png)

***Imagen 1 - Mapa de Herramientas***
