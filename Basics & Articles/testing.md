# TESTS
- **En las pruebas unitarias** comprobamos unidades individuales como módulos, funciones o métodos de software. Estas sirven para comprobar que los componentes más pequeños funcionen correctamente
- **Las pruebas de integración** sirven para probar o testear esos módulos pero en forma de grupo, ver cómo interaccionan entre sí. Por ejemplo, la interacción de una API con un servicio backend o un servicio con una base de datos
- **En pruebas de funcionalidad** testeamos el código en general en su conjunto. Usualmente forma parte de una técnica de testing que se llama black box donde no vemos el código. Acá el tester simplemente prueba la app con los inputs requeridos y los compara con los outputs o resultados esperados
- Los tests suelen ser ejecutados por un equipo de QA , como desarrollador lo ideal es centrarse en las pruebas unitarias

## Unit Testings / Pruebas Unitarias
#### Pruebas Unitarias
- Las pruebas unitarias o unit testing son una forma de comprobar que un fragmento de codigo funciona correctamente
- Consisten en aislar una parte del codigo y comprobar que funciona a la perfección. Son pequeños tests que validan el comportamiento de un objeto y la lógica
- *When to use Unit tests?*: Easy to write and easy to run. Run unit tests when you want to test functions or small pieces.


#### Ventajas
- **Fomentan el cambio**: Facilitan que el programador cambie el codigo para mejorar su estructura (refactorizacion), puesto que permite hacer pruebas sobre los cambios y asegurarse entonces que los nuevos cambios no han introducido defectos
- **Simplifica la integracion**: Permiten llegar a la fase de integracion con un grado alto de seguridad de que el codigo esta funcionando correctamente -> asi se facilitan las pruebas de integracion
- **Documenta el codigo**: Las propias pruebas son documentacion del codigo
- **Separacion de la interfaz y la implementacion**: La unica interaccion entre los casos de prueba y las unidades bajo prueba son las interfaces de estas ultimas
- **Los errores estan mas acotados y son mas faciles de localizar**: Dado que tenemos pruebas unitarias que pueden desenmascararlos


#### Las 3 A del Unit Testing (Arrange, Act, Assert)
- **Arrange**: 1er paso. Se definen los requisitos que debe cumplir el codigo
- **Act**: 2o paso. El momento de ejecutar el test que dara lugar a los resultados a analizar
- **Arrange**: 3er paso. Momento de comprobar si los resultados obtenidos son los esperados (OK -> validacion y seguir adelante)


## Integration tests / Tests de integracion
- Similar to Unit Tests and they have the smallness of the unit test while having the actual application of an end to end test (it emulates an user emulating with our site)
- *When to use Unit tests?*: When there are lots of calls (Lots of database or API calls). 

<hr>

## [Mocha](https://blog.logrocket.com/testing-node-js-mocha-chai/)
- Mocha is a test framework running in Node.js & the browser
- It's designed for testing both synchronous & asynchronous code with a very simple interface
- Mocha provides functions that execute in a specific order, loggin the results in the terminal window
- Mocha is commonly used with Chai, a popular assertion library for Node.js and the browser
- The default interface is **BDD**, Behavior-Driven Development, which aims to help developers build software that is predictable, resilient, and not error-probe
- BDD evolved from TDD which requires: 1. Write tests, 2. Run tests, 3. Implement software, 4. Fix bugs and refactor until all tests pass, 5. Repeat the cycle for any new functionality
- The main difference between TDD and BDD is that BDD calls for writing test cases in a shared language, simplyfying communication between developers, QA teams & business leaders

### Mocha BDD interface
```js
// begin a test suite of one or more tests
describe('#sum()', function() {
	
	// add a test hook (a hook its a place in code that allows you to tap into a module that either provide different )
	beforeEach(function() {
		// Some logic before each test is run
	});

	// test functionality
	it('should add numbers', function() {
		// add assertion
		expect(sum(1,2,3,4,5).to.equal(15));
	});

	// some more tests

});
```

## [Mock testing](https://blog.logrocket.com/api-mock-testing-with-nock-node-js/)
## [Nock](https://github.com/nock/nock)
When testing individual units of our application, our tests must be isolated. This helps to increase the speed of our tests and reduce the number of dependencies required to run the tests.

However, there will be some parts of the app that rely on data from external systems to run, such as databases, file systems or external APIs. To test these parts, we use a mock object

A mock is a method or objects that mimics the behavior of an external system. Mocks are created in a manner that stimulates the behavior of an external system

**Nock is an HTTP server mocking and expectations library for Node.js**. Nock works by overriding the http.request and http.ClientRequest functions, intercepting all requests made to a specified URL and returning specified responses that mimic the data the real URL would return.

**Using Nock as a mock server allows us to easily perform tests on modules that make HTTP to an external object like a URL without actually making any requests to the URL**. This makes our testing process faster and more efficient.



### TDD Test Driven Development
El Desarrollo guiado por pruebas de software hace referencia un estilo de programación que combina **codificación**, **testeo** y **diseño**
El testeo se realiza mediante *tests unitarios* y el diseño mediante *refactorización*

- Escribir un test unitario simple que describa un aspecto del programa
- Ejecutar el test, que debería fallar porque el programa carece de ese elemento
- Escribir el código más simple posible para hacer pasar el test
- Refactorizar el código hasta que cumple el criterio de simplicidad
- Repetir, acumulando tests unitarios

Entre las ventajas de este desarrollo se destacan el poder hacer aplicaciones de más calidad en menos tiempo
La primera meta es superar la prueba, alcanzar la funcionalidad principal y ocuparse más adelante de los casos excepcionales y el manejo de errores

El ciclo del TDD se llama *red-green-refactor*
1. **Fase roja**: Se redacta un test que contenga componentes no implementados, para luego decidir qué elementos son realmente necesarios para que el código funcione

2. **Fase verde**: Suponiendo que el test falle, se busca una solución simple, este código se integra en el código productivo para que el test quede marcado en verde

3. **Refactorización**: El código productivo se pasa a limpio y se perfecciona, para que quede elegante y comprensible, se eliminan los duplicados en el código y se vuelve más profesional

A partir del **TDD** se desarrolló el **BDD** *Behavior-Driven Development*, es decir el desarrollo guiado por comportamiento
Esta metodología no se guía inicialmente por la adecuación del código sino por el comportamiento que se desea ver en el software
Por lo general, el BDD es el mejor método a la hora de diseñar pruebas, mientras que el TDD da como resultado una arquitectura más limpia


### Unit Testing
Los test unitarios o pruebas unitarias nos permiten comprobar los componentes individuales de los programas informáticos

Estos tests se realizan en las primeras fases del desarrollo, ya que en la fase de prueba se pueden corregir los errores de manera rápida y poco costosa

Las pruebas unitarias son pequeñas piezas de código diseñadas para comprobar que el código principal está funcionando como esperábamos
El proceso que se lleva a cabo consta de tres partes:

- **Arrange**, donde se devinen los requisitos que debe cumplir el código principal
- **Act**, el proceso de ceración donde vamos acumulando los resultados que analizaremos
- **Assert**, se considera el momento en que comprobamos si los resultados agrupados son correctos o incorrectos. Y depende del resultado, se valida o se continúa