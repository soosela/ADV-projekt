# Lakásárak és Bérleti Díjak Vizualizációs Projekt

## 📌 Projekt leírása

Ez a projekt a lakásárak, bérleti díjak és jövedelmek időbeli alakulását vizsgálja különböző magyarországi városokban 2010 és 2024 között. A cél az, hogy érthető és látványos adatvizualizációkon keresztül bemutassuk az ingatlanpiac főbb trendjeit, összefüggéseit, és azok gazdasági hatásait.

A projekt egy statikus weboldalt is tartalmaz, ahol a felhasználó áttekintheti az elkészült ábrákat, valamint választ kaphat az alábbi kérdésekre:

- Miről szól a projekt?
- Milyen adatokat használtunk?
- Miért érdekesek ezek az adatok?
- Ki a célfelhasználó?
- Mit tanulhat a felhasználó ezekből az ábrákból?
- Mennyire skálázható és automatizálható a megoldás?
- Mivel lehetne bővíteni a jövőben?

---

## 📊 Vizualizációk

A projekt összesen 7 különböző vizualizációt tartalmaz:

1. **Lakásárak alakulása városonként (oszlopdiagram)**
2. **Bérleti díjak alakulása városonként (oszlopdiagram)**
3. **Jövedelmek alakulása városonként (oszlopdiagram)**
4. **Lakásár és bérleti díj közti kapcsolat (szórásdiagram)**
5. **Megfizethetőség (Lakásár / Jövedelem arány)**
6. **Lakásárak hőtérképe város és év szerint**
7. **Munkanélküliségi ráta időbeli alakulása**



---

## 🗃️ Használt adatok

- Forrás: `lakas_adatbazis_2010_2024.csv`
- Típusok: numerikus gazdasági mutatók (EUR/m², EUR/hó, %, stb.)
- Feldolgozási lépések: Év kivonása, oszlopok átnevezése, új mutatók számítása (pl. megfizethetőség)

---

## 👩‍💻 Készítők

A projektet készítette:

- **Soós Mária Izabela**
- **Sólyom Anett**

---

## ⚙️ Technológiák

- Python (pandas, matplotlib, seaborn)
- HTML, CSS
- Grafikonmentés PNG formátumban

---

## 🔄 Automatizálás és bővíthetőség

- A projekt teljesen automatizálható újabb adatok hozzáadásával.
- Bővíthető további mutatókkal (pl. infláció, GDP).
- Lehetőség van interaktív webes megjelenítésre (pl. Plotly, Dash, Streamlit használatával).

---

