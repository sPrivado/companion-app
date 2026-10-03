# AGENTS.md

Contexto para agentes de código que trabajan en este repo.

## Proyecto
Una app de escritorio con un personaje 3D interactivo y chat con IA. Lee `docs/PRD.md` antes de cambiar cualquier cosa; es la fuente de verdad del alcance.

## Stack
- `apps/desktop`: Tauri, TypeScript, Vite y Three.js.
- `backend`: Python 3.11+ con FastAPI. Se comunica por WebSocket en localhost (ver el contrato en el PRD, sección 6).

## Comandos
<!-- Completar cuando exista el esqueleto (M0) -->
- Frontend: `pnpm install` · `pnpm tauri dev` · `pnpm test`
- Backend: `uv sync` · `uv run uvicorn app.main:app --reload` · `uv run pytest`

## Reglas
- Trabaja solo dentro del hito actual del PRD. No agregues features fuera de alcance.
- No cambies el contrato de mensajes sin actualizar el PRD y los tipos en los dos lados.
- Nunca subas claves, `.env` ni modelos 3D sin licencia verificada.
- Cada cambio en el backend necesita su test en `backend/tests`.
- Haz cambios pequeños y explica el porqué en el PR.
- Si algo del PRD es ambiguo, pregunta en lugar de suponer.
