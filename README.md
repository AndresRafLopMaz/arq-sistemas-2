# Assignment 02 — Vite + React + Tailwind en CDN (AWS S3 + CloudFront)

Aplicación web estática creada con **Vite + React + TypeScript + Tailwind** y publicada en un **CDN de AWS (S3 + CloudFront)**.  
Despliegue automático con **GitHub Actions**: build → upload a S3 → invalidate CloudFront.

---

## ✅ URL pública (CDN)
- CloudFront: https://d10lh0klntq5rq.cloudfront.net/

---

## 🧱 Tecnologías
- Vite + React + TypeScript
- TailwindCSS
- AWS S3
- AWS CloudFront
- Doppler
- GitHub Actions

---

## 📦 Build local
```bash
npm install
npm run build


---

## Segmento 2/3 — Doppler + GitHub Secrets (con capturas)

```md
## 🔐 Doppler

### Config Syncs (Doppler ↔ GitHub)
<img width="1561" height="377" alt="Screenshot From 2026-02-22 17-46-39" src="https://github.com/user-attachments/assets/3b684b82-69e9-402f-a0d3-53d2b5568155" />

### Variables / Secrets en Doppler (valores ocultos)

<img width="1561" height="665" alt="Screenshot From 2026-02-22 17-46-56" src="https://github.com/user-attachments/assets/70e3b8db-23b8-4bc6-a22f-07e4e4173135" />

Secrets usados en Doppler:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION
- S3_BUCKET
- CLOUDFRONT_DISTRIBUTION_ID

---

## 🔑 GitHub Secrets

<img width="1830" height="964" alt="Screenshot From 2026-02-22 17-47-41" src="https://github.com/user-attachments/assets/2998573e-a749-4f4a-96c1-ed47fd72eea2" />


## ⚙️ GitHub Actions Pipeline

Workflow:
- `.github/workflows/deploy-cdn.yml`

Acciones del pipeline:
1. **Build**: `npm ci` y `npm run build`
2. **Upload**: sube el contenido de `dist/` al **root** del bucket S3
3. **Invalidate**: invalida CloudFront (`/*`)

---

## 🖼️ Evidencia de la aplicación
<img width="1830" height="1014" alt="Screenshot From 2026-02-22 17-48-23" src="https://github.com/user-attachments/assets/694329b7-afdd-4989-b53c-3081b74414bb" />


---

## 📌 Entregables
- Repositorio: https://github.com/AndresRafLopMaz/arq-sistemas-2
- Rama: `assignment-02`
- URL pública (CDN): https://d10lh0klntq5rq.cloudfront.net/





