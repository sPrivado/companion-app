# WORK.md: Bitácora y plan de trabajo

> Cómo se usa: al empezar cada sesión, lee "Dónde voy". Al terminar, marca `[x]` y anota en "Notas" qué aprendiste o en qué te trabaste.
> Cada tarea dura máximo de 30 a 45 minutos. Si una toma más, se parte en dos.

## Perfil (2026-10-03)
- Python y JavaScript: sabe variables, condicionales, bucles y funciones.
- Terminal: no la domina todavía; tiene Warp instalado (Windows).
- Herramientas: cree tener Python, Node.js, Git y VS Code/Cursor (verificado: Python 3.12.10, Node v24.18.0, npm 11.16.0, Git 2.55.0).
- Web: hizo HTML y CSS con ayuda de IA (Beyond The Wall).
- Regla: Steven escribe el código; el mentor explica, revisa y pregunta.

## Dónde voy
**Tarea actual:** T1.6

---

## Fase 0: Caja de herramientas (terminal, Git, entorno)
- [x] **T0.1** Moverse en la terminal: `pwd`, `ls`, `cd`, `mkdir`. Crear la carpeta del proyecto.
- [x] **T0.2** Verificar las versiones instaladas (`python --version`, `node --version`, `git --version`) e instalar lo que falte.
- [x] **T0.3** Abrir la carpeta en Cursor y poner `AGENTS.md`, `WORK.md` y `docs/PRD.md` dentro.
- [x] **T0.4** Git básico: `git init`, `git status`, `git add` y `git commit`. Primer commit.
- [x] **T0.5** Subir el repo a GitHub (repo privado) y entender qué es `push`.

## Fase 1: Python de nuevo (backend)
- [x] **T1.1** Script `hola.py` que pregunta tu nombre y saluda: input, variables y f-strings.
- [x] **T1.1b** Manejar errores con `try` / `except`: que el programa no se caiga si la edad no es un número.
- [x] **T1.2** Listas y diccionarios: guardar un "historial de chat" en memoria.
- [x] **T1.3** Funciones y módulos: separar el código en dos archivos e importar.
- [x] **T1.4** Entornos virtuales y paquetes (`uv` o `venv` y `pip`): entender para qué sirven.
- [x] **T1.5** Primer servidor con FastAPI: la ruta `/health` devuelve `{"ok": true}`, y la abres en el navegador.
- [ ] **T1.6** Qué es JSON y qué es una API: crear la ruta `POST /chat` que responde con eco.
- [ ] **T1.7** Primer test con `pytest` para `/health`.

## Fase 2: JavaScript de nuevo y la escena 3D (frontend en el navegador)
- [ ] **T2.1** Crear un proyecto con Vite y entender `npm install` y `npm run dev`.
- [ ] **T2.2** DOM básico: un input y un botón que agregan mensajes a una lista.
- [ ] **T2.3** `fetch`: mandar el mensaje al `POST /chat` del backend y mostrar la respuesta.
- [ ] **T2.4** Three.js paso 1: escena, cámara, luz y un cubo que gira.
- [ ] **T2.5** Three.js paso 2: controles de cámara (OrbitControls).
- [ ] **T2.6** Cargar un modelo 3D gratuito (GLB) en lugar del cubo.
- [ ] **T2.7** Reproducir la animación idle del modelo.

## Fase 3: Conectar la IA
- [ ] **T3.1** Qué es un LLM y una API key. Guardar la clave en `.env` y meter `.env` en `.gitignore`.
- [ ] **T3.2** El backend llama al LLM y devuelve texto real.
- [ ] **T3.3** Pedirle al LLM `{text, emotion}` en JSON y manejar el error si no responde bien.
- [ ] **T3.4** El frontend cambia la animación según `emotion`.
- [ ] **T3.5** Streaming con WebSocket (concepto primero, luego código).

## Fase 4: Convertirlo en app de escritorio
- [ ] **T4.1** Qué es Tauri o Electron y por qué, para decidir con el PRD.
- [ ] **T4.2** Envolver el frontend en Tauri: abre una ventana.
- [ ] **T4.3** Hacer que la app arranque el backend Python sola.
- [ ] **T4.4** Guardar el historial en SQLite.
- [ ] **T4.5** Generar un instalador de Windows.

---

## Glosario (se llena a medida que aparecen términos)
- **Terminal**: un chat con tu computador; en lugar de hacer clic, le escribes órdenes.
- **Ruta (path)**: la dirección de una carpeta, como la dirección de una casa: `C:\Users\steve\Documents\companion-app`.
- **Versión**: el número de edición de un programa; las guías siempre piden una mínima.
- **`.` y `..`**: `.` es "esta carpeta"; `..` es "la carpeta de arriba".
- **Commit**: un punto de guardado del proyecto, con un mensaje que dice qué cambió.
- **Repositorio (repo)**: la carpeta del proyecto con todo su historial de Git.
- **Push**: subir tus commits a GitHub (la nube).
- **Remote (origin)**: la dirección del repo en GitHub.
- **Traceback**: el "reporte del accidente" de Python. Se lee de abajo hacia arriba: qué pasó, y luego en qué archivo y línea.
- **Lista**: una fila ordenada de cosas, `[a, b, c]`; se agrega al final con `.append()`.
- **Diccionario**: una ficha con etiquetas, `{"rol": "usuario", "texto": "hola"}`.
- **Función**: una receta con nombre; `return` entrega el resultado.
- **Módulo**: otro archivo .py del que traes funciones con `import`.
- **.gitignore**: la lista de cosas que Git no debe guardar nunca.
- **Entorno virtual (venv)**: la caja de herramientas propia de cada proyecto.
- **requirements.txt**: la receta con los paquetes y sus versiones para rearmar la caja.
- **Servidor**: un programa que espera pedidos y los responde (el restaurante abierto).
- **localhost:8000**: "este PC, puerta 8000".
- **Ruta / endpoint**: cada plato del menú del servidor (`/`, `/health`).
- **Decorador `@app.get`**: la etiqueta que dice "cuando pidan esta ruta, ejecuta esta función".
- **Booleano**: sí o no. En Python se escribe `True`/`False` y en JSON `true`/`false`.
- **Código 200**: "todo salió bien".

## Notas de sesiones
<!-- AAAA-MM-DD · tarea · qué aprendí · dónde me trabé -->
- 2026-10-03 · T0.1 · pwd, ls, cd, mkdir en PowerShell (Warp); proyecto en `C:\Users\steve\Documents\companion-app` · sin trabas
- 2026-10-03 · T0.2 · todas las herramientas instaladas, nada que instalar · sin trabas
- 2026-10-03 · T0.3 · Move-Item, `.` (aquí) y `..` (carpeta de arriba) · los archivos cayeron en docs y se movieron
- 2026-10-03 · T0.4 · git init/status/add/commit; primer commit `5b45ee3` · sin trabas
- 2026-10-03 · T0.5 · repo privado en GitHub, branch main, remote origin, push · sin trabas. FASE 0 COMPLETA
- 2026-10-03 · T1.1 · input, int(), if/else, f-strings; refactor guardando el resultado en la variable `estado` · aprendí a leer un Traceback (ValueError)
- 2026-10-03 · T1.1b · try/except ValueError dentro de while True con break; hizo el reto extra · pendiente: quitar int() repetido, primer commit de práctica
- 2026-10-03 · commit `be1f0d5` subido a github.com/sPrivado/companion-app
- 2026-10-03 · T1.2 · lista de dicts con role/content/hora, datetime.strftime (lo aprendió preguntando a la IA y lo explicó bien); corrigió el orden del break · pendiente menor: imprimir la respuesta del bot en vivo
- 2026-10-03 · PRUEBA Fase 0 + T1.1–T1.2 · aprobada (~6,5/8) · repasar: commit = guardado LOCAL, push = nube; leer requisitos con cuidado; formatear decimales en f-string
- 2026-10-03 · T1.3 · funciones con return, módulos con import (mesero = chat_app.py, cocina = chat_funciones.py); git restore, git rm; commit `268f792` · se trabó: escribió en el archivo equivocado (chat.py) y ejecutó el archivo equivocado con el botón ▶; subió __pycache__ por error, se arregla con .gitignore
- 2026-10-03 · T1.4 · venv en backend/.venv, pip install fastapi uvicorn, pip freeze > requirements.txt, .gitignore (.venv/, __pycache__/, *.pyc, .env) · requirements.txt quedó en la raíz, se mueve con git mv
- 2026-10-03 · T1.5 · backend/main.py con FastAPI: rutas `/` y `/health` ({"ok": True}); uvicorn main:app --reload; /docs; código 200 · se trabó: copió el ejemplo de la doc sin adaptarlo y no sabía que había que repetir el bloque decorador + función; booleanos True/False
