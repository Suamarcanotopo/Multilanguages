#!/usr/bin/env python3
"""Valida estrutura, conteúdo mínimo e referências do projeto Pandora, sem rede."""
import json
import pathlib
import re
import sys

ROOT=pathlib.Path(__file__).resolve().parents[1]
ERRORS=[]
def load(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8"))
cases=load("catalogo/casos.json")["casos"]
langs=load("catalogo/idiomas.json")["idiomas"]
sources=load("catalogo/fontes.json")["fontes"]
stores=load("catalogo/lojas.json")["lojas"]
def unique(items,label):
    if len(items)!=len(set(items)):
        ERRORS.append(f"ID duplicado: {label}")
unique([c["id"] for c in cases],"cases")
unique([l["slug"] for l in langs],"languages")
unique([s["id"] for s in sources],"sources")
unique([s["url"] for s in sources],"source URLs")
unique([s["id"] for s in stores],"shop IDs")
assert len(langs)==4, "A fundação requer quatro idiomas"
assert len(cases)>=30, "A fundação requer 30 cenários"
expected={"PST-002","PST-006"}
for l in langs:
    slug=l["slug"]
    path=ROOT/"idiomas"/slug
    for f in ("INDEX.md","GLOSSARIO.md","FONTES.md","COMPRAS-ONLINE.md"):
        if not (path/f).is_file():
            ERRORS.append(f"Falta {path/f}")
    actual={p.stem for p in (path/"aulas").glob("*.md")}
    if actual!=expected:
        ERRORS.append(f"{slug}: aulas encontradas {sorted(actual)} vs esperadas {sorted(expected)}")
    for id_ in actual:
        content=(path/"aulas"/(id_+".md")).read_text(encoding="utf-8")
        for marker in ("rascunho-exemplo","Tradução natural","PENDENTE","Fontes gratuitas"):
            if marker not in content:
                ERRORS.append(f"{slug}/{id_}: falta '{marker}'")
    if not any(s["idioma"]==slug and s["acesso"]=="gratuito-institucional" for s in sources):
        ERRORS.append(f"{slug}: sem fonte institucional gratuita")
for item in sources+stores:
    if not item["url"].startswith("https://"):
        ERRORS.append(f"URL inválida: {item['url']}")
    if re.search(r"\s",item["url"]):
        ERRORS.append(f"Espaço na URL: {item['url']}")
for c in cases:
    if c["id"] in expected and c["status"]!="rascunho-exemplo":
        ERRORS.append(f"status incorreto {c['id']}")
    if c["id"] not in expected and c["status"]!="planejado":
        ERRORS.append(f"status não comprovado {c['id']}")
if ERRORS:
    print("FAIL: "+str(len(ERRORS))+" erro(s)")
    for err in ERRORS: print(" - "+err)
    sys.exit(1)
print(f"PASS: {len(langs)} idiomas; {len(cases)} cenários; 8 aulas-exemplo; {len(sources)} fontes; {len(stores)} lojas; IDs e arquivos sem colisão.")
print("NOT TESTED: links online ao vivo, áudio real, correção nativa, eficácia didática.")
