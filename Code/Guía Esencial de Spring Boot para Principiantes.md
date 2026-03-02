---
type: "project"
tags:
  - spring-boot
  - java
  - microservicios
  - backend
  - api-rest
project: "none"
status: "en-progreso"
date_created: "2026-03-01"
date_modified: "2026-03-01"
related: [] # Array vacío o con [[links]]
---

## **1. ¿Qué es Spring Boot?**

- **Spring Boot** es un framework de Java que simplifica el desarrollo de aplicaciones al proporcionar configuraciones predeterminadas.
- Está basado en el ecosistema **Spring Framework** pero facilita su uso mediante auto-configuración y menos configuraciones manuales.
- Diseñado para crear aplicaciones listas para ejecutar (standalone), con un servidor embebido como Tomcat o Jetty.

**Ventajas**:

- Configuración sencilla.
- Incorporación de dependencias automática.
- Ideal para microservicios.
- Compatible con herramientas modernas como Docker y Kubernetes.
---

## **2. Requisitos Previos**

- **Java**: Instala JDK 8 o superior.
- **Maven o Gradle**: Herramientas para gestionar dependencias.
- **IDE**: IntelliJ IDEA, Eclipse o Visual Studio Code son ideales para desarrollar.
- Familiaridad básica con Java.

---

## **3. Crear un Proyecto de Spring Boot**

- **Spring Initializr**:
    1. Ve a [start.spring.io](https://start.spring.io/).

    2. Selecciona las opciones:
        - **Project**: Maven o Gradle.
        - **Language**: Java.
        - **Spring Boot version**: La más reciente (ejemplo: 3.x).
        - **Dependencies**: Elige lo necesario (ejemplo: Spring Web para crear APIs REST).
    3. Descarga el proyecto generado y ábrelo en tu IDE.

**Consola**:
```
curl https://start.spring.io/starter.zip \
  -d dependencies=web \
  -d name=demo \
  -o demo.zip
```

---

## **4. Estructura del Proyecto**
Un proyecto típico de Spring Boot tiene la siguiente estructura:

```
src/main/java
    com.example.demo
        DemoApplication.java  // Punto de entrada principal
        controllers           // Controladores REST
        services              // Lógica de negocio
        repositories          // Interacciones con la base de datos
src/main/resources
    application.properties    // Configuraciones de la aplicación
```

---

## **5. Crear una Aplicación Básica**
- **Clase Principal**:

    ```
    @SpringBootApplication
    public class DemoApplication {
        public static void main(String[] args) {
            SpringApplication.run(DemoApplication.class, args);
        }
    }
    ```
    - `@SpringBootApplication`: Combina `@Configuration`, `@EnableAutoConfiguration` y `@ComponentScan`.

---

## **6. Crear un Controlador REST**
Un controlador maneja las peticiones HTTP. Ejemplo:

```
@RestController
@RequestMapping("/api")
public class HelloController {

    @GetMapping("/hello")
    public String sayHello() {
        return "Hola, Spring Boot!";
    }
}
```

- `@RestController`: Define una clase que devuelve respuestas JSON o texto.
- `@RequestMapping`: Define el prefijo de las rutas.
- `@GetMapping`: Define una ruta HTTP GET.

---

## **7. Configuración con application.properties**
Este archivo permite personalizar la aplicación:
```
# Configuración del servidor
server.port=8081
# Configuración de la base de datos (H2)
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=password
```

---

## **8. Conectar con una Base de Datos**
1. **Agrega las dependencias en** `**pom.xml**`:
    ```
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jpa</artifactId>
    </dependency>
    <dependency>
        <groupId>com.h2database</groupId>
        <artifactId>h2</artifactId>
        <scope>runtime</scope>
    </dependency>
    ```
    
2. **Crea una Entidad**:
    ```
    @Entity
    public class Usuario {
        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        private Long id;
    
        private String nombre;
        private String email;
    
        // Getters y setters
    }
    ```
    
3. **Crea un Repositorio**:
    ```
    public interface UsuarioRepository extends JpaRepository<Usuario, Long> {}
    ```

---

## **9. Ejecutar la Aplicación**

- Desde tu IDE: Ejecuta la clase principal (`DemoApplication.java`).
- Desde la terminal:
    ```
    mvn spring-boot:run
    ```
---
## **10. Recursos Adicionales**
- **Documentación oficial**: [spring.io/docs](https://spring.io/docs)