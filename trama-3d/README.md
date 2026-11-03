# TRAMA 3D

Proyecto paralelo a 2Ruedas: tienda de herramientas para pintura, albañilería y texturado, fabricadas con impresión 3D (y más adelante, accesorios importados).

Por ahora es solo la parte visual: un catálogo de presentación.

## Archivos

- `index.html`: la web catálogo, en un solo archivo. Se abre con doble clic en cualquier navegador (necesita internet para las fuentes y Three.js).
- `CATALOGO.md`: la lista de productos con funciones, medidas, materiales y estado.

## Qué tiene la web

- Hero con una llana 3D que peina enduido en cámara lenta (Three.js).
- Catálogo de 28 productos en 5 líneas, con imágenes 3D generadas desde modelos paramétricos y ficha con visor 3D que se gira con el dedo o el mouse.
- Biblioteca de 6 texturas con simulación de la pasada y el perfil del diente en milímetros.
- Proceso de fabricación, filamentos, hoja de ruta (3D → a medida → importación) y contacto.

## Cómo editar

- Productos: array `PRODUCTS` dentro de `index.html` (nombre, función, usos, medidas, estado y modelo 3D).
- Marca: "TRAMA" es un nombre provisorio; se cambia buscando y reemplazando el texto.
- Contacto: los datos de WhatsApp e Instagram están marcados "(a definir)".
