SIMULADOR DE CREDITO

Este programa es un simulador de préstamos que permite a los usuarios ingresar sus datos personales y los detalles del préstamo que desean solicitar. A partir de la información proporcionada, el sistema evalúa la elegibilidad para diferentes tipos de créditos (consumo, estudiantil, hipotecario, compra de cartera) y calcula los intereses, la cantidad adeudada y las cuotas mensuales. Además, los datos ingresados se almacenan en un archivo CSV y se pueden exportar a un archivo Excel.
Instalación

Para ejecutar este programa, asegúrate de tener instalados los siguientes componentes:

    Python: Asegúrate de tener Python 3.x instalado en tu sistema. Puedes descargarlo desde python.org.

    Bibliotecas necesarias: Este programa utiliza las bibliotecas tkinter y pandas. Para instalar pandas, abre tu terminal o símbolo del sistema y ejecuta el siguiente comando:

En el terminal o bash

    pip install pandas

    Dependencias: La biblioteca tkinter viene incluida en la mayoría de las instalaciones de Python. Sin embargo, si no está instalada, puedes buscar información específica para tu sistema operativo.

Ejecución

Una vez que hayas instalado los componentes necesarios, puedes ejecutar el programa. Simplemente abre una terminal, navega a la carpeta donde se encuentra el archivo .pyw y ejecuta:

En el terminal o bash

python nombre_del_archivo.pyw

Reemplaza nombre_del_archivo con el nombre del archivo que contiene el código.

Uso

    Ingresa los datos personales requeridos (nombre, edad, trabajo, ingresos, meses trabajando, capital solicitado y tiempo del préstamo).
    Selecciona el motivo del préstamo.
    Haz clic en "Continuar" para ver la evaluación y los resultados.
    Si deseas exportar los datos a un archivo Excel, presiona el botón correspondiente.

Notas

    Asegúrate de completar todos los campos requeridos antes de continuar.
    Los datos de los usuarios se guardan en un archivo CSV llamado datos_usuarios.csv, y los resultados se exportan a datos_prestamos.xlsx cuando se selecciona la opción de exportar.
