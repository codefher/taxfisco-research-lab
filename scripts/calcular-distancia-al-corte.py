import sys

sys.stdout.reconfigure(encoding="utf-8")

N = 30
# Instrumento, cumplimiento del antes, numero de items, denominacion del diagnostico
FILAS = [
    (13, 47.78, 3, "Capacitación y cobertura"),
    (7, 47.92, 2, "Retención y acceso a evidencias"),
    (1, 48.54, 4, "Detección y registro de eventos"),
    (4, 49.17, 3, "Lecciones aprendidas y mejora"),
    (8, 49.72, 3, "Accesos y mínimos privilegios"),
    (10, 50.56, 3, "Gestión de vulnerabilidades"),
]
CORTE = 51.0

print(f"{'Instr':<7}{'Subdimensión':<38}{'Antes':>8}{'Falta':>8}{'Paso mín.':>11}{'Equivale a':>12}")
print("-" * 86)
total_pasos = []
for num, antes, items, nombre in FILAS:
    falta = CORTE - antes
    # Un punto de un solo respondente en un solo reactivo
    paso = 100.0 / (N * items * 4)
    equiv = -(-falta // paso)  # redondeo hacia arriba
    total_pasos.append(equiv)
    print(f"{num:<7}{nombre:<38}{antes:>7.2f} %{falta:>7.2f} p{paso:>10.3f} {int(equiv):>10d}")

print()
print("Rango necesario: de", int(min(total_pasos)), "a", int(max(total_pasos)),
      "cambios unitarios de un respondente.")

# El global ya esta en Gestionado
glob = 52.70
items_tot = 42
paso_global = 100.0 / (N * items_tot * 4)
print()
print(f"Madurez global antes: {glob:.2f} % (ya en Gestionado)")
print(f"Para llegar al corte del nivel Optimizado (76 %) faltan {76 - glob:.2f} puntos,")
print(f"lo que equivale a {int((76 - glob) / paso_global):d} cambios unitarios de un respondente.")
print(f"Paso mínimo global: {paso_global:.4f} puntos porcentuales.")