import { useMemo, useState } from "react";
import "./App.css";

export default function App() {
  const [count, setCount] = useState(0);

  const today = useMemo(() => {
    return new Date().toLocaleString();
  }, []);

  return (
    <div className="page">
      <header className="card">
        <div className="badge">Assignment 03 • AWS Elastic Beanstalk</div>

        <h1 className="title">Vite + React (Docker)</h1>
        <p className="subtitle">
          App estática desplegada en AWS Elastic Beanstalk, con imagen en ECR y
          pipeline de GitHub Actions.
        </p>

        <div className="grid">
          <div className="stat">
            <div className="statLabel">Fecha / Hora</div>
            <div className="statValue">{today}</div>
          </div>

          <div className="stat">
            <div className="statLabel">Clicks</div>
            <div className="statValue">{count}</div>
          </div>

          <div className="stat">
            <div className="statLabel">Estado</div>
            <div className="statValue ok">Online</div>
          </div>
        </div>

        <div className="actions">
          <button className="btn" onClick={() => setCount((c) => c + 1)}>
            Incrementar
          </button>
          <button className="btn secondary" onClick={() => setCount(0)}>
            Reset
          </button>
        </div>

        <footer className="footer">
          <span>© {new Date().getFullYear()} Arquitectura de Sistemas II</span>
          <span className="dot">•</span>
          <span>Deploy via Docker + Nginx</span>
        </footer>
      </header>
    </div>
  );
}
