import "./App.css";

export default function App() {
  return (
    <div className="page">
      <header className="card">
        <h1>Assignment 04 — Vite + React + Docker</h1>
        <p>
          Interfaz estática sencilla: tipografía, color y layout limpio.
          Publicada como imagen Docker con tags <code>latest</code> y <code>SHA</code>.
        </p>
        <div className="chips">
          <span className="chip">Vite</span>
          <span className="chip">React</span>
          <span className="chip">Docker</span>
          <span className="chip">GitHub Actions</span>
          <span className="chip">Doppler</span>
        </div>
      </header>

      <main className="grid">
        <section className="panel">
          <h2>Objetivo</h2>
          <p>
            Automatizar build y publicación de contenedor a Docker Hub en cada commit.
          </p>
        </section>

        <section className="panel">
          <h2>Tags</h2>
          <ul>
            <li><strong>latest</strong>: siempre apunta a la imagen más reciente.</li>
            <li><strong>SHA</strong>: una imagen por commit (histórico).</li>
          </ul>
        </section>

        <section className="panel">
          <h2>Entrega</h2>
          <p>
            README con captura de la app, URL de la imagen y captura de tags en Docker Hub.
          </p>
        </section>
      </main>

      <footer className="footer">
        <small>Arquitectura de Sistemas II • 2026 (commit 2)</small>
      </footer>
    </div>
  );
}
