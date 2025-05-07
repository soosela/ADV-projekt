import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Beállítások
sns.set(style="ticks")  # Eltávolítja a háttér színeket
plt.rcParams.update({
    "axes.titlesize": 18,
    "axes.labelsize": 14,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
    "figure.figsize": (16, 8),  # Nagyobb ábra
    "axes.facecolor": "white",  # Fehér háttér a grafikonoknak
    "figure.facecolor": "white",  # Fehér háttér a teljes ábra mögött
    "grid.alpha": 0.2  # A hálózat (grid) áttetszősége
})
output_dir = "abra"
os.makedirs(output_dir, exist_ok=True)

# 🔽 Adatok betöltése
df = pd.read_csv("lakas_adatbazis_2010_2024.csv")

# 🔧 Az Év oszlopból csak a számot vesszük ki (pl. '2010-Q1' -> 2010)
df["Év"] = df["Év"].astype(str).str[:4].astype(int)

# 🔧 Jövedelem oszlop átnevezése
df.rename(columns={"Nettó jövedelem (EUR/hó)": "Jövedelem (EUR/hó)"}, inplace=True)

# A következő lépésben Pivot táblát készítünk, hogy több oszlopot jeleníthessünk meg:

# 1. Lakásárak időbeli alakulása - Oszlopdiagram (Pivot tábla használata)
plt.figure(figsize=(18, 8))  # Nagyobb ábra
df_pivot_lakasar = df.pivot_table(index="Év", columns="Város", values="Lakásár (EUR/m²)", aggfunc="mean")
df_pivot_lakasar.plot(kind="bar", ax=plt.gca(), width=0.8)  # Oszlopdiagram
plt.title("Lakásárak alakulása városonként")
plt.ylabel("EUR/m²")
plt.xlabel("Év")
plt.xticks(rotation=45)
plt.legend(title='Város', loc='upper left', bbox_to_anchor=(1, 1))  # Jelmagyarázat pozicionálása
plt.tight_layout()
plt.savefig(f"{output_dir}/1_lakasarak_ido_bar.png")
plt.close()

# 2. Bérleti díjak időbeli alakulása - Oszlopdiagram (Pivot tábla használata)
plt.figure(figsize=(18, 8))  # Nagyobb ábra
df_pivot_berletidij = df.pivot_table(index="Év", columns="Város", values="Bérleti díj (EUR/hó)", aggfunc="mean")
df_pivot_berletidij.plot(kind="bar", ax=plt.gca(), width=0.8)  # Oszlopdiagram
plt.title("Bérleti díjak alakulása városonként")
plt.ylabel("EUR/hó")
plt.xlabel("Év")
plt.xticks(rotation=45)
plt.legend(title='Város', loc='upper left', bbox_to_anchor=(1, 1))  # Jelmagyarázat pozicionálása
plt.tight_layout()
plt.savefig(f"{output_dir}/2_berletidij_ido_bar.png")
plt.close()

# 3. Jövedelmek időbeli alakulása - Oszlopdiagram (Pivot tábla használata)
plt.figure(figsize=(18, 8))  # Nagyobb ábra
df_pivot_jovedelem = df.pivot_table(index="Év", columns="Város", values="Jövedelem (EUR/hó)", aggfunc="mean")
df_pivot_jovedelem.plot(kind="bar", ax=plt.gca(), width=0.8)  # Oszlopdiagram
plt.title("Jövedelmek alakulása városonként")
plt.ylabel("EUR/hó")
plt.xlabel("Év")
plt.xticks(rotation=45)
plt.legend(title='Város', loc='upper left', bbox_to_anchor=(1, 1))  # Jelmagyarázat pozicionálása
plt.tight_layout()
plt.savefig(f"{output_dir}/3_jovedelem_ido_bar.png")
plt.close()

# 4. Lakásár és bérleti díj kapcsolata
plt.figure(figsize=(14, 8))
sns.scatterplot(data=df, x="Lakásár (EUR/m²)", y="Bérleti díj (EUR/hó)", hue="Város", 
                style="Lakástípus", alpha=0.7, s=100, marker="o")  # Pontok kiemelése
plt.title("Lakásár és bérleti díj kapcsolata")
plt.legend(title='Város', loc='upper left', bbox_to_anchor=(1, 1))  # Jelmagyarázat pozicionálása
plt.tight_layout()
plt.savefig(f"{output_dir}/4_lakasar_vs_berletidij.png")
plt.close()

# 5. Megfizethetőség (Lakásár / Jövedelem)
df["Megfizethetőség"] = df["Lakásár (EUR/m²)"] / df["Jövedelem (EUR/hó)"]
plt.figure(figsize=(18, 8))  # Nagyobb ábra
df_pivot_megfizethetoseg = df.pivot_table(index="Év", columns="Város", values="Megfizethetőség", aggfunc="mean")
df_pivot_megfizethetoseg.plot(kind="bar", ax=plt.gca(), width=0.8)  # Oszlopdiagram
plt.title("Megfizethetőség alakulása városonként")
plt.ylabel("Lakásár / Jövedelem")
plt.xlabel("Év")
plt.xticks(rotation=45)
plt.legend(title='Város', loc='upper left', bbox_to_anchor=(1, 1))  # Jelmagyarázat pozicionálása
plt.tight_layout()
plt.savefig(f"{output_dir}/5_megfizethetoseg.png")
plt.close()

# 6. Lakásár hőtérkép év és város szerint
pivot = df.pivot_table(index="Város", columns="Év", values="Lakásár (EUR/m²)", aggfunc="mean")
plt.figure(figsize=(18, 8))  # Nagyobb ábra
sns.heatmap(pivot, cmap="YlOrBr", annot=True, fmt=".1f", cbar_kws={'label': 'EUR/m²'})
plt.title("Lakásárak hőtérképe (év és város szerint)")
plt.tight_layout()
plt.savefig(f"{output_dir}/6_heatmap_lakasar.png")
plt.close()

# 7. Munkanélküliségi ráta időbeli alakulása
plt.figure(figsize=(18, 8))  # Nagyobb ábra
sns.lineplot(data=df, x="Év", y="Munkanélküliségi ráta (%)", hue="Város", 
             style="Város", markers=False, dashes=False, linewidth=2)
plt.title("Munkanélküliségi ráta alakulása városonként")
plt.ylabel("%")
plt.xlabel("Év")
plt.xticks(sorted(df["Év"].unique()))
plt.legend(title='Város', loc='upper left', bbox_to_anchor=(1, 1))  # Jelmagyarázat pozicionálása
plt.tight_layout()
plt.savefig(f"{output_dir}/7_munkanelkuliseg_ido.png")
plt.close()

print("✅ Az összes vizualizáció elmentve az 'abra/' mappába.")
