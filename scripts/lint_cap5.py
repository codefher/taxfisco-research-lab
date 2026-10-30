# -*- coding: utf-8 -*-
"""Linter del borrador de Capitulo V contra las reglas duras v7 (revisado)."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

path = sys.argv[1]
text = open(path, encoding="utf-8").read()

# --- limpieza estructural -------------------------------------------------
clean = []
for ln in text.splitlines():
    s = ln.strip()
    if not s or s.startswith("#") or s.startswith("|") or s.startswith("!["):
        continue
    if re.match(r"^\d+\.\s", s):          # marcadores de lista numerada
        s = re.sub(r"^\d+\.\s*", "", s)
    clean.append(s)
body = "\n".join(clean)

# separar los incisos en negrita (**...**) como unidades propias
body = re.sub(r"\*\*(.+?)\*\*", lambda m: "\x01" + m.group(1) + "\x02", body, flags=re.S)
body = body.replace("*", "")

# partir en unidades: alterna cuerpo / inciso en negrita
units = []
for chunk in body.split("\x01"):
    if not chunk.strip():
        continue
    if "\x02" in chunk:
        lead, rest = chunk.split("\x02", 1)
        units.append((lead.strip(), True))
        if rest.strip():
            units.append((rest.strip(), False))
    else:
        units.append((chunk.strip(), False))

def words(s):
    s = re.sub(r"[*_`\x01\x02]", "", s)
    return len([w for w in s.split() if re.search(r"[0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]", w)])

CONJ = ("y", "ni", "o", "pero", "sino")

PAST = r"\b\w+(?:aron|ieron|aba|aban|ió|isteis)\b"
FUT  = r"\b\w+(?:ará|erán|irán|aría|erían|iría)\b"
ANTE = r"\b(?:ha|han|había|habían|hubo|hubieron)\s+\w+(?:ado|ido)\b"
PERI = r"\b(?:va|van)\s+a\s+\w+\b"

NUM_Y = r"\b(?:veinte|treinta|cuarenta|cincuenta|sesenta)\s+y\s+(?:dos|tres|cuatro|cinco|seis|siete|nueve|diez)\b"

problems = []
report = []

for text_unit, is_lead in units:
    sents = [s.strip() for s in re.split(r"(?<=[.;])\s+", text_unit) if s.strip()]
    for sent in sents:
        plain = re.sub(r"[*_`\x01\x02]", "", sent).strip()
        if not plain:
            continue
        # neutralizar el "y" de los cardinales compuestos (cuarenta y dos)
        plain_count = re.sub(NUM_Y, "NUM", plain)
        w = words(plain)
        report.append((w, is_lead, plain))

        n_y = len(re.findall(r"\by\b", plain_count, flags=re.IGNORECASE))
        if n_y > 2:
            problems.append(f"[Y x{n_y}] {plain}")

        for m in re.finditer(r",\s+(" + "|".join(CONJ) + r")\b", plain, flags=re.IGNORECASE):
            problems.append(f"[COMA ANTES DE '{m.group(1)}'] ...{plain[max(0,m.start()-80):m.end()+45]}...")

        for m in re.finditer(r"\b(" + "|".join(CONJ) + r")\s+,", plain, flags=re.IGNORECASE):
            problems.append(f"[COMA DESPUES DE '{m.group(1)}'] ...{plain[max(0,m.start()-55):m.end()+55]}...")

        for m in re.finditer(r":", plain):
            before = plain[:m.start()]
            if re.search(r"\d{4}$", before) or re.search(r"\d\s*$", before) or "http" in plain:
                continue
            problems.append(f"[DOS PUNTOS] ...{plain[max(0,m.start()-30):m.start()+40]}...")

        if "\u2014" in plain:
            problems.append(f"[RAYA LARGA] {plain[:130]}")

        for pat, tag in ((PAST, "PRET"), (FUT, "FUTURO"), (ANTE, "ANTEPRESENTE"), (PERI, "PERIFRASTICO")):
            hits = re.findall(pat, plain, flags=re.IGNORECASE)
            if hits:
                problems.append(f"[{tag} {hits}] {plain[:150]}")

        if not is_lead and w < 18:
            problems.append(f"[CORTA {w}w] {plain}")

print("=== LONGITUD DE ORACIONES ===")
for i, (w, lead, plain) in enumerate(report, 1):
    print(f"{i:>3} {w:>3}w{' [lead]' if lead else '':>8}  {plain[:78]}")

print(f"\n=== PROBLEMAS ({len(problems)}) ===")
for p in problems:
    print(p)
