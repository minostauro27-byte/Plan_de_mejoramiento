# 🛠️ HelpDesk en Tiempo Real - Backend

## 📌 Descripción

Este proyecto corresponde al desarrollo del backend para un sistema de gestión de tickets de soporte técnico en laboratorios de cómputo.

Permite a los usuarios reportar fallas en equipos y a los técnicos gestionar dichos tickets en tiempo real mediante WebSockets.

---

## 🚀 Tecnologías utilizadas

* Python 3
* Django
* Django REST Framework
* JWT (SimpleJWT)
* Django Channels (WebSockets)
* drf-spectacular (Swagger)
* SQLite
* Visual Studio Code(VSC)
---

## 🔐 Autenticación

El sistema utiliza autenticación basada en **JWT (JSON Web Tokens)**.

### Endpoints:

* `POST /api/register/` → Crear usuario
* `POST /api/login/` → Obtener token

---

## 👥 Roles de Usuario

### 👤 usuario_base

* Crear tickets
* Ver solo sus tickets

### 🛠️ tecnico

* Ver todos los tickets
* Cambiar estado de tickets

---

## 📡 Endpoints principales

### 🎫 Tickets

| Método | Endpoint                     | Descripción       |
| ------ | ---------------------------- | ----------------- |
| POST   | `/api/tickets/`              | Crear ticket      |
| GET    | `/api/tickets/list/`         | Listar tickets    |
| PUT    | `/api/tickets/{id}/`         | Actualizar estado |
| GET    | `/api/tickets/estadisticas/` | Ver estadísticas  |

---

## ⚡ WebSockets (Tiempo Real)

### Endpoint:

```bash
ws://127.0.0.1:8000/ws/alertas/
```

### Funcionamiento:

Cuando un técnico cambia el estado de un ticket, el sistema envía un mensaje en tiempo real:

```json
{
  "mensaje": "El ticket #1 ahora está en estado resuelto"
}
```

---

## 📊 Estadísticas

El sistema proporciona métricas como:

* Total de tickets
* Tickets pendientes
* Tickets resueltos
* Tiempo promedio de resolución

---

## 📚 Documentación API (Swagger)

Disponible en:

```bash
http://127.0.0.1:8000/api/docs/
```

Permite probar los endpoints directamente desde el navegador.

---

## ⚙️ Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/minostauro27-byte/Plan_de_mejoramiento.git
cd Proyecto_maikoll_torres
```

---

### 2. Crear entorno virtual

```bash
py -m venv venv
.\venv\Scripts\activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Ejecutar servidor (ASGI)
1.En una terminal levantamos el servidor asi:
```bash
daphne plan_de_mejoramiento.asgi:application
```
2.En una terminal bash ejecutamos el siguiente comando para ver la notificacion y cambio de estado de los tickets.

```bash
wscat -c ws://127.0.0.1:8000/ws/alertas/
```

---

## 🧪 Pruebas

    Realizamos todas las pruebas correspondientes en el archivo test.http, como por ejemplo:

    1.Crear Usuario con rol base 
    2.Crear Usuario con rol tecnico 
    3.Inicio de sesion rol=base
    4.Inicio de sesion(rol=tecnico)
    5.Entre otras

---

## 🧠 Arquitectura

El sistema está construido siguiendo una arquitectura REST con separación de responsabilidades:

* Autenticación y autorización
* Lógica de negocio por roles
* Persistencia de datos
* Comunicación en tiempo real con WebSockets

---

## 🎯 Características principales

* API RESTful completa
* Autenticación JWT
* Control de acceso por roles
* WebSockets en tiempo real
* Endpoint analítico de estadísticas
* Documentación automática con Swagger

---

## 👨‍💻 Autor

 Maikoll Daniel Torres Fandiño

---

## 📌 Notas finales

* El sistema es 100% backend
* No incluye frontend
* Todas las pruebas se realizan mediante herramientas API
