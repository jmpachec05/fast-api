from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importa los routers
from routes.atributo_routes import router as atributo_router
from routes.atributo_usuario_routes import router as atributo_usuario_router
from routes.conversaciones_routes import router as conversaciones_router
from routes.incidencias_routes import router as incidencias_router
from routes.knowledge_base_routes import router as knowledge_base_router
from routes.mensajes_routes import router as mensajes_router
from routes.metricas_routes import router as metricas_router
from routes.notificaciones_routes import router as notificaciones_router
from routes.permisos_routes import router as permisos_router
from routes.respuestas_routes import router as respuestas_router
from routes.roles_routes import router as roles_router
from routes.satisfaccion_routes import router as satisfaccion_router
from routes.usuarios_routes import router as usuarios_router
from routes.objeto_routes import router as objeto_router  # Importa el enrutador de objetos

app = FastAPI()

# Rutas
app.include_router(atributo_router, prefix="/api/v1", tags=["Atributos"])
app.include_router(atributo_usuario_router, prefix="/api/v1", tags=["Atributo Usuario"])
app.include_router(conversaciones_router, prefix="/api/v1", tags=["Conversaciones"])
app.include_router(incidencias_router, prefix="/api/v1", tags=["Incidencias"])
app.include_router(knowledge_base_router, prefix="/api/v1", tags=["Knowledge Base"])
app.include_router(mensajes_router, prefix="/api/v1", tags=["Mensajes"])
app.include_router(metricas_router, prefix="/api/v1", tags=["Métricas"])
app.include_router(notificaciones_router, prefix="/api/v1", tags=["Notificaciones"])
app.include_router(permisos_router, prefix="/api/v1", tags=["Permisos"])
app.include_router(respuestas_router, prefix="/api/v1", tags=["Respuestas"])
app.include_router(roles_router, prefix="/api/v1", tags=["Roles"])
app.include_router(satisfaccion_router, prefix="/api/v1", tags=["Satisfacción"])
app.include_router(usuarios_router, prefix="/api/v1", tags=["Usuarios"])
app.include_router(objeto_router, prefix="/api/v1", tags=["Objetos"])  # Incluye el enrutador de objetos

# Configuración de CORS
origins = [
    "http://localhost",
    # "http://localhost:8080",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ejecutar el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
