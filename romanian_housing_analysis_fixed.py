# Vizualizációk Python kóddal – Átláthatóbb időtengellyel és formázással
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Beállítások
sns.set(style="whitegrid")
plt.rcParams.update({"axes.titlesize": 16, "axes.labelsize": 12, "xtick.labelsize": 8, "ytick.labelsize": 10})
graph_dir = "abra"
os.makedirs(graph_dir, exist_ok=True)

# Adatok betöltése
file_path = "lakas_adatbazis_kibovitett.csv"
df = pd.read_csv(file_path)

# Időszak tengelyrendezés
df['Időszak'] = pd.Categorical(df['Időszak'], ordered=True, categories=sorted(df['Időszak'].unique(), key=lambda x: (int(x[:4]), x[5:])))

# 1. Lakásárak időbeli alakulása
plt.figure(figsize=(16, 6))
ax = sns.lineplot(data=df, x="Időszak", y="Lakásár (EUR/m²)", hue="Város", linewidth=2)
plt.title("Lakásárak alakulása városonként")
plt.ylabel("EUR/m²")
plt.xlabel("Időszak")
plt.xticks(rotation=90, ha='center')
plt.legend(bbox_to_anchor=(1.01, 1), loc="upper left")
plt.tight_layout()
plt.savefig(f"{graph_dir}/lakasarak_ido.png")
plt.close()

# 2. Bérleti díjak időbeli alakulása
plt.figure(figsize=(16, 6))
ax = sns.lineplot(data=df, x="Időszak", y="Bérleti díj (EUR/hó)", hue="Város", linewidth=2)
plt.title("Bérleti díjak alakulása városonként")
plt.ylabel("EUR/hó")
plt.xlabel("Időszak")
plt.xticks(rotation=90, ha='center')
plt.legend(bbox_to_anchor=(1.01, 1), loc="upper left")
plt.tight_layout()
plt.savefig(f"{graph_dir}/berleti_dij_ido.png")
plt.close()

# 3. Jövedelmek időbeli változása
plt.figure(figsize=(16, 6))
ax = sns.lineplot(data=df, x="Időszak", y="Jövedelem (EUR/hó)", hue="Város", linewidth=2)
plt.title("Jövedelmek alakulása városonként")
plt.ylabel("EUR/hó")
plt.xlabel("Időszak")
plt.xticks(rotation=90, ha='center')
plt.legend(bbox_to_anchor=(1.01, 1), loc="upper left")
plt.tight_layout()
plt.savefig(f"{graph_dir}/atlagber_ido.png")
plt.close()

# 4. Lakásár és bérleti díj kapcsolata
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Lakásár (EUR/m²)", y="Bérleti díj (EUR/hó)", hue="Város", style="Lakás típusa", alpha=0.7)
plt.title("Lakásár és bérleti díj kapcsolata")
plt.xlabel("Lakásár (EUR/m²)")
plt.ylabel("Bérleti díj (EUR/hó)")
plt.tight_layout()
plt.savefig(f"{graph_dir}/lakasar_vs_berletidij.png")
plt.close()

# 5. Megfizethetőség (Lakásár / Jövedelem)
df["Megfizethetoseg"] = df["Lakásár (EUR/m²)"] / df["Jövedelem (EUR/hó)"]
plt.figure(figsize=(16, 6))
ax = sns.lineplot(data=df, x="Időszak", y="Megfizethetoseg", hue="Város", linewidth=2)
plt.title("Lakásmegfizethetőség alakulása")
plt.ylabel("Lakásár / Jövedelem")
plt.xlabel("Időszak")
plt.xticks(rotation=90, ha='center')
plt.legend(bbox_to_anchor=(1.01, 1), loc="upper left")
plt.tight_layout()
plt.savefig(f"{graph_dir}/megfizethetoseg.png")
plt.close()

# 6. Lakásár hőtérkép év és város szerint
pivot = df.groupby(["Város", "Időszak"])["Lakásár (EUR/m²)"].mean().unstack()
plt.figure(figsize=(18, 10))
sns.heatmap(pivot, cmap="YlGnBu", annot=False, linewidths=.4, cbar_kws={'label': 'EUR/m²'})
plt.title("Lakásár hőtérkép városonként és időszakonként")
plt.tight_layout()
plt.savefig(f"{graph_dir}/heatmap_lakasar.png")
plt.close()

# 7. Munkanélküliségi ráta időbeli alakulása
plt.figure(figsize=(16, 6))
ax = sns.lineplot(data=df, x="Időszak", y="Munkanélküliségi ráta (%)", hue="Város", linewidth=2)
plt.title("Munkanélküliségi ráta alakulása városonként")
plt.ylabel("%")
plt.xlabel("Időszak")
plt.xticks(rotation=90, ha='center')
plt.legend(bbox_to_anchor=(1.01, 1), loc="upper left")
plt.tight_layout()
plt.savefig(f"{graph_dir}/munkanelkuliseg_ido.png")
plt.close()

print("✅ Minden vizualizáció frissítve és elmentve a 'abra/' mappába.")

