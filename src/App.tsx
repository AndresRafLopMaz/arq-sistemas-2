export default function App() {
  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 flex items-center justify-center">
      <div className="text-center p-8 rounded-xl bg-slate-800 shadow">
        <h1 className="text-4xl font-extrabold text-emerald-400">Tailwind OK ✅</h1>
        <p className="mt-3 text-slate-300">
          Si ves fondo oscuro y el título verde, Tailwind está aplicando colores.
        </p>
        <button className="mt-6 px-4 py-2 rounded bg-emerald-500 text-black font-semibold hover:bg-emerald-400">
          Botón de prueba
        </button>
      </div>
    </div>
  );
}
