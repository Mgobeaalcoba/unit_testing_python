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

### Uso de subTest() en unittest:

- **subTest():** Permite ejecutar subtests dentro de un test principal, lo que facilita la identificación de múltiples fallos en un solo test.
  - **Ejemplo**:
    ```python
    with self.subTest(i=i):
        self.assertEqual(i % 2, 0)
    ```
    
### Mocking en Python:

- **Mocking:** Es una técnica que permite simular el comportamiento de objetos reales en un entorno controlado.
- **Objetivo:** Simplificar la escritura de tests y reducir la dependencia de componentes externos.
- 
- **Librerías populares:** `unittest.mock`, `pytest-mock`, `mockito`, entre otras.
  - **Ejemplo Mock**:
    ```python
    from unittest.mock import Mock
    mock = Mock()
    mock.some_method.return_value = 42
    assert mock.some_method() == 42
    ``` 
  - **Ejemplo Patch como Context Manager:**
    ```python
    from unittest.mock import patch
    with patch('module.function') as mock_function:
        mock_function.return_value = 42
        assert module.function() == 42
    ```
  - **Ejemplo Patch como Decorador:**
    ```python
    from unittest.mock import patch
    @patch('module.function')
    def test_function(mock_function):
        mock_function.return_value = 42
        assert module.function() == 42
    ```
- **Nota:** `unittest.mock` es parte de la librería estándar de Python a partir de la versión 3.3.
- **Referencia:** [Documentación oficial de unittest.mock](https://docs.python.org/3/library/unittest.mock.html)

### Testing con Doctest en comentarios usando sesiones interactivas de Python:

- **Doctest:** Permite incluir ejemplos de uso y resultados esperados en los comentarios del código.
- **Ventajas:** Facilita la documentación y verificación de ejemplos en el código.
- **Ejemplo**:
  ```python
  def add(a, b):
      """
      Suma dos números.

      >>> add(2, 3)
      5
      >>> add(-1, 1)
      0
      """
      return a + b
  ```
- **Ejemplo con ZeroDivisionError**:
  ```python
  def divide(a, b):
      """
      Divide dos números.

      >>> divide(10, 2)
      5.0
      >>> divide(5, 0)
      Traceback (most recent call last):
      ZeroDivisionError: division by zero
      """
      return a / b
  ```
- **Ejecución:** Los tests de doctest se pueden ejecutar con el módulo `doctest` de Python o con el comando `python -m doctest -v file.py`.
  - **Ejemplo de Ejecución:**
    ```
    Trying:
        add(2, 3)
    Expecting:
        5
    ok
    Trying:
        add(-1, 1)
    Expecting:
        0
    ok
    ```
    - **Ejemplo de comandos de ejecución:**
      ```bash
      python -m doctest -v file.py
      python -m doctest -v file.py -o ELLIPSIS
      ```
- **Nota:** Los tests de doctest se ejecutan por defecto en modo "ELLIPSIS", lo que permite ignorar diferencias en la salida que no afectan el resultado.
- **Referencia:** [Documentación oficial de doctest](https://docs.python.org/3/library/doctest.html)

### Workflow de Testing en Python:

- **Pasos:**
  1. **Planificación:** Definir qué se va a testear y cómo.
  2. **Implementación:** Escribir los tests y el código a testear.
  3. **Ejecución:** Correr los tests y verificar los resultados.
  4. **Reporte:** Analizar los resultados y corregir los errores.
  5. **Automatización:** Integrar los tests en un flujo de CI/CD.

### Testing con Pytest

- **Pytest:** Es una librería de testing popular en Python que permite escribir tests de forma sencilla y eficiente.
- **Ventajas:** Mayor legibilidad, menos código boilerplate y soporte para tests parametrizados.
  - **Ejemplo de Test con Pytest:**
    ```python
    def test_add():
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
    ```
- **Ejecución:** Los tests de pytest se pueden ejecutar con el comando `pytest` en la terminal.
- **Referencia:** [Documentación oficial de Pytest](https://docs.pytest.org/en/stable/)
- **Instalación:** Pytest se puede instalar con `pip install pytest`. o `pip install pytest-cov` para obtener información de cobertura de código.
- **Instalación Poetry:** Pytest se puede instalar con `poetry add pytest`. o `poetry add pytest-cov` para obtener información de cobertura de código.
- **Ejemplo de ejecución con Pytest:** `pytest -v test_file.py`

### Cobertura de Código con Pytest

- **Cobertura de Código:** Mide la cantidad de código que es ejecutada por los tests.
- **Pytest-cov:** Es una extensión de Pytest que permite obtener información detallada sobre la cobertura de código.
- **Ejecución:** Los tests con cobertura se pueden ejecutar con el comando `pytest --cov=module` en la terminal.
- **Reporte HTML:** Se puede generar un reporte HTML detallado con el comando `pytest --cov=module --cov-report=html`.
- **Referencia:** [Documentación oficial de pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
- **Ejemplo de ejecución con Cobertura:** `pytest --cov=module -v test_file.py`