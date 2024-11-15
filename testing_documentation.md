# Tipos de Testing:

### Definiciones

- **Testing Unitario:** Verifica el correcto funcionamiento de unidades individuales de código, como funciones o métodos.
- **Testing de Integración:** Asegura que los diferentes módulos o componentes funcionen bien en conjunto.
- **Testing de Sistema:** Evalúa el sistema completo para asegurarse de que cumple con los requisitos especificados.
- **Testing de Aceptación:** Verifica que el software satisface las necesidades del usuario final.
- **Testing de Regresión:** Asegura que los cambios o actualizaciones no hayan introducido nuevos errores en funcionalidades ya existentes.

### Datos adicionales

- **Testing Unitario:** Se suele automatizar y es la base del TDD (Test Driven Development)
- **Testing de Integración:** Agregué el detalle sobre probar la interacción de módulos ya probados individualmente y las formas en que se puede realizar (incremental vs. "big bang").
- **Testing de Sistema:** Incorporé una referencia a requisitos no funcionales (rendimiento, seguridad, etc.) que son parte clave de esta fase de pruebas.
- **Testing de Aceptación:** Normalmente lo realiza el cliente o el equipo de QA en su nombre. Suele dividirse en dos subtipos: pruebas de aceptación del usuario (UAT) y pruebas de aceptación operativas.
- **Testing de Regresión:** Añadí un comentario sobre la automatización, que es muy relevante para este tipo de testing, especialmente en proyectos grandes.

### Assert Nativo en Python vs Unittest Assertions:

- **Assert Nativo en Python:** Es una forma sencilla de verificar condiciones, pero no proporciona mensajes de error detallados.
- **Unittest Assertions:** Proporciona mensajes de error más descriptivos y permite verificar múltiples condiciones en un solo test.
- **Ejemplos**:
  - **Assert Nativo en Python:** `assert a == b`
  - **Unittest Assertions:** `self.assertEqual(a, b)`
  - **Nota:** `unittest` es una librería estándar de Python para escribir tests.

### Uso de unittest.skip() y unittest.skipIf():

- **unittest.skip():** Se utiliza para indicar que un test debe ser omitido.
- **unittest.skipIf():** Permite omitir un test si se cumple una condición específica.