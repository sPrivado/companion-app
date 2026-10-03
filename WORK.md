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

**Tarea actual:** T0.4

---



## Fase 0: Caja de herramientas (terminal, Git, entorno)

- [x] **T0.1** Moverse en la terminal: `pwd`, `ls`, `cd`, `mkdir`. Crear la carpeta del proyecto.
- [x] **T0.2** Verificar las versiones instaladas (`python --version`, `node --version`, `git --version`) e instalar lo que falte.
- [x] **T0.3** Abrir la carpeta en Cursor y poner `AGENTS.md`, `WORK.md` y `docs/PRD.md` dentro.
- [x] **T0.4** Git básico: `git init`, `git status`, `git add` y `git commit`. Primer commit.
- [x] **T0.5** Subir el repo a GitHub (repo privado) y entender qué es `push`.



## Fase 1: Python de nuevo (backend)

- [ ] **T1.1** Script `hola.py` que pregunta tu nombre y saluda: input, variables y f-strings.
- [ ] **T1.2** Listas y diccionarios: guardar un "historial de chat" en memoria.
- [ ] **T1.3** Funciones y módulos: separar el código en dos archivos e importar.
- [ ] **T1.4** Entornos virtuales y paquetes (`uv` o `venv` y `pip`): entender para qué sirven.
- [ ] **T1.5** Primer servidor con FastAPI: la ruta `/health` devuelve `{"ok": true}`, y la abres en el navegador.
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



## Notas de sesiones



- 2026-10-03 · T0.1 · pwd, ls, cd, mkdir en PowerShell (Warp); proyecto en `C:\Users\steve\Documents\companion-app` · sin trabas
- 2026-10-03 · T0.2 · todas las herramientas instaladas, nada que instalar · sin trabas

