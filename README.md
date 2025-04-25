<h1>🎵 Music Popularity Prediction API</h1>

<p>Esta solución permite <strong>predecir la popularidad de canciones</strong> basado en las variables propias de la canción.</p>

<h2>📊 Variables de Entrada</h2>

<p>Las siguientes características deben ser enviadas en formato JSON para realizar la predicción:</p>

<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Tipo</th>
      <th>Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>duration_ms</code></td><td>float</td><td>Duración de la canción en milisegundos</td></tr>
    <tr><td><code>danceability</code></td><td>float</td><td>Puntaje de bailabilidad</td></tr>
    <tr><td><code>energy</code></td><td>float</td><td>Nivel de energía</td></tr>
    <tr><td><code>loudness</code></td><td>float</td><td>Nivel de volumen (loudness)</td></tr>
    <tr><td><code>speechiness</code></td><td>float</td><td>Puntaje de habla</td></tr>
    <tr><td><code>acousticness</code></td><td>float</td><td>Puntaje de acústica</td></tr>
    <tr><td><code>instrumentalness</code></td><td>float</td><td>Puntaje de instrumentalidad</td></tr>
    <tr><td><code>liveness</code></td><td>float</td><td>Puntaje de "vivacidad" (presencia en vivo)</td></tr>
    <tr><td><code>valence</code></td><td>float</td><td>Puntaje de positividad</td></tr>
    <tr><td><code>tempo</code></td><td>float</td><td>Tempo (BPM)</td></tr>
    <tr><td><code>explicit</code></td><td>int</td><td>Bandera de explícito (0 = No, 1 = Sí)</td></tr>
    <tr><td><code>mode</code></td><td>int</td><td>Modo (0 = menor, 1 = mayor)</td></tr>
    <tr><td><code>time_signature</code></td><td>int</td><td>Compás (ejemplo: 4 para 4/4)</td></tr>
  </tbody>
</table>

<h2>🚀 Componentes de la Solución</h2>

<p>La API está compuesta por los siguientes archivos:</p>
<ul>
  <li><strong><code>api_popularity.py</code></strong>:<br>
    Interfaz de la API, que puede ser ejecutada vía HTTP utilizando el método <strong>POST</strong>.<br>
    Recibe un JSON con los parámetros descritos arriba y retorna un valor de predicción entre <strong>0 y 100</strong> representando la popularidad estimada de la canción.
  </li>
  <li><strong><code>predict_popularity.py</code></strong>:<br>
    Encargado del tratamiento de datos, incluyendo la codificación y estandarización de las variables.<br>
    Luego invoca al modelo entrenado para realizar la predicción.
  </li>
  <li><strong><code>trackspopularity_clf.pkl</code></strong>:<br>
    Archivo que contiene el <strong>modelo entrenado</strong> empaquetado.<br>
    Debe estar presente junto con la solución para que funcione correctamente.
  </li>
  <li><strong><code>requirements.txt</code></strong>:<br>
    Archivo que incluye todos los requerimientos y dependencias necesarios para instalar y ejecutar la solución.<br>
    Se pueden instalar con:<br>
    <code>pip install -r requirements.txt</code>
  </li>
</ul>

<h2>📝 Ejemplo de Uso</h2>

<p>Realizar una petición POST a la API con el siguiente JSON:</p>

<pre>
<code>{
  "duration_ms": 151387,
  "danceability": 0.683,
  "energy": 0.511,
  "loudness": -4.749,
  "speechiness": 0.0279,
  "acousticness": 0.0107,
  "instrumentalness": 0.215,
  "liveness": 0.156,
  "valence": 0.515,
  "tempo": 104.99,
  "explicit": 0,
  "mode": 1,
  "time_signature": 4
}
</code>
</pre>

<h2>💡 Resultado</h2>

<p>La respuesta de la API será un JSON con el campo <code>result</code> que indica la popularidad predicha:</p>

<pre>
<code>{
  "result": 72.5
}
</code>
</pre>

<h2>⚙️ Instalación y Ejecución</h2>

<ol>
  <li>Clonar el repositorio.</li>
  <li>Crear un entorno virtual:<br><code>python3 -m venv venv</code></li>
  <li>Activar el entorno virtual:<br><code>source venv/bin/activate</code></li>
  <li>Instalar dependencias:<br><code>pip install -r requirements.txt</code></li>
  <li>Ejecutar la API:<br><code>python3 api_popularity.py</code></li>
</ol>

<p>La API estará disponible en <code>http://localhost:5000/</code>.</p>
