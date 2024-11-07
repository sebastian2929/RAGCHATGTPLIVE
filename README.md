# Introduction to Creating RAGs (Retrieval-Augmented Generators) with OpenAI

## Resumen
Este proyecto es una aplicación de muestra construida con LangChain para traducir texto de inglés a otro idioma. La aplicación usa un modelo de lenguaje (LLM) para realizar la traducción mediante una sola llamada y algunas plantillas de mensajes. Es un excelente punto de partida para aprender a trabajar con LangChain y sus funcionalidades.

## Descripción General

- Uso de modelos de lenguaje (LLM)
- Encadenar componentes usando el Lenguaje de Expresiones de LangChain (LCEL)
- Realizar seguimiento y depuración de la aplicación
- Despliegue de la con LangServe


## Arquitectura de la Aplicación

![image](https://github.com/user-attachments/assets/b6bc00e9-c5d0-49c2-aac2-f059a76bd9b8)


Esta aplicación utiliza LangChain para traducir texto de manera eficiente. La arquitectura se divide en los siguientes componentes:
- **PromptTemplate:** Define la estructura del mensaje que el modelo recibirá, indicando qué texto traducir y a qué idioma.
- **LLM Model:** El modelo de lenguaje encargado de procesar el texto y realizar la traducción.
- **OutputParser:** Extrae la respuesta generada por el modelo y la convierte en un formato legible.
- **Encadenamiento (LCEL):** LangChain permite conectar estos componentes en un flujo, usando el operador | para encadenar el PromptTemplate, el modelo LLM y el OutputParser.
- **LangSmith:** Ofrece seguimiento y trazabilidad de las ejecuciones, permitiendo depurar y observar los pasos del proceso de traducción.
- **LangServe:** Una capa de despliegue que expone la cadena como una API REST mediante FastAPI.


## Uso      

1. Para iniciar el servidor, ejecuta:
``` 
python langchainserver.py
```
2. Para iniciar el cliente, ejecuta:
``` 
python langchainclient.py
```
3.  La API estará disponible en http://localhost:8000/chain. También puedes acceder al "Playground" en http://localhost:8000/chain/playground para probar el servicio con streaming de salida.

## Pruebas

### Cliente
![image](https://github.com/user-attachments/assets/22b836c8-6ffd-42ce-8a31-7296dd0d6253)

### Servidor
![image](https://github.com/user-attachments/assets/5ef7aa48-0165-40de-a879-0b846fe39464)

![image](https://github.com/user-attachments/assets/74897ef5-2da3-4e00-bcc3-5c6db61be443)

## Autor

- [Sebastián David Blanco Rodríguez](https://github.com/Sebastian2929)


## Licencia


Este proyecto está bajo la Licencia (MIT) - ver el archivo [LICENSE](LICENSE.md) para ver más detalles.
