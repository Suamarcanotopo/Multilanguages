#!/usr/bin/env python3
"""Validacao offline de catalogo, independencia dos idiomas e indices gerados."""
import json
import pathlib
import re
import sys
from urllib.parse import urlparse
import build_indices as index

ROOT=pathlib.Path(__file__).resolve().parents[1]
errors=[]
def err(s): errors.append(s)
def read(p): return json.loads((ROOT/p).read_text(encoding="utf-8"))
def unique(values,label):
    if len(values)!=len(set(values)): err("Duplicado: "+label)
try:
    cases, langs=index.data(ROOT)
    progress=index.progress(ROOT,cases,langs)
    sources=read("catalogo/fontes.json")["fontes"]
    shops=read("catalogo/lojas.json")["lojas"]
    evidence=read("catalogo/evidencias.json")["entries"]
    slugs={l["slug"] for l in langs}
    ids={c["id"] for c in cases}
    unique([x["id"] for x in sources],"fontes")
    unique([x["id"] for x in shops],"lojas")
    unique([x["id"] for x in evidence],"evidencias")
    unique([x["url"] for x in sources],"URLs fontes")
    if len(cases)!=30 or len(langs)!=4: err("Base deve conter 30 temas e 4 idiomas.")
    if any("status" in c for c in cases): err("Catalogo global nao pode ter status de aula.")
    if any("status" in l for l in langs): err("Catalogo global nao pode ter status do idioma.")
    for item in sources+shops+evidence:
        u=item.get("url","")
        p=urlparse(u)
        if p.scheme!="https" or not p.netloc or any(c.isspace() for c in u): err("URL invalida: "+u)
    for e in evidence:
        if e.get("idioma") not in slugs or e.get("case_id") not in ids: err("Evidencia orfa: "+e["id"])
        if e.get("confirmacao_frase_exata") is True and not e.get("revisor"):
            err("Alegacao literal sem revisor: "+e["id"])
    for lang in langs:
        slug=lang["slug"]
        folder=ROOT/"idiomas"/slug
        for name in ("README.md","INDEX.md","GLOSSARIO.md","FONTES.md","COMPRAS-ONLINE.md","ANALOGIAS.md"):
            if not (folder/name).is_file(): err("Falta arquivo "+slug+"/"+name)
        if not any(x["idioma"]==slug and x.get("acesso")=="gratuito-institucional" for x in sources):
            err("Falta fonte gratuita para "+slug)
        for md in folder.rglob("*.md"):
            content=md.read_text(encoding="utf-8")
            for other in slugs-{slug}:
                if "idiomas/"+other+"/" in content or "../"+other+"/" in content:
                    err("Link cruzado de idiomas: "+str(md.relative_to(ROOT)))
        for cid,status in progress[slug].items():
            p=folder/"aulas"/(cid+".md")
            content=p.read_text(encoding="utf-8")
            if not content.lstrip().startswith("# "+cid+" —"): err("Titulo nao corresponde ao arquivo: "+str(p))
            if status=="rascunho-exemplo":
                for marker in ("Tradução natural","Fontes gratuitas","PENDENTE"):
                    if marker not in content: err("Rascunho incompleto: "+str(p))
            if status=="aprovado":
                for marker in ("**Revisor responsável:**","**Data da revisão:**","**Fonte de áudio revisada:**"):
                    if marker not in content: err("Aprovacao sem evidencia: "+str(p))
                if "Revisão linguística/nativa: **PENDENTE**" in content:
                    err("Aprovacao falsa: "+str(p))
        analogy=(folder/"ANALOGIAS.md").read_text(encoding="utf-8")
        if "Pista para brasileiros" not in analogy or "Tradução em português" not in analogy:
            err("Analogia incompleta: "+slug)
    if sum(map(len,progress.values()))<8: err("Regressao: menos de 8 aulas criadas.")
    for p,text in index.outputs(ROOT).items():
        if not p.exists() or p.read_text(encoding="utf-8")!=text:
            err("Indice desatualizado: "+str(p.relative_to(ROOT)))
    gateway=(ROOT/"INDICES/INDEX.md").read_text(encoding="utf-8")
    for slug in slugs:
        if "idiomas/"+slug+"/INDEX.md" not in gateway:
            err("Trilha ausente do portal: "+slug)
except (ValueError,OSError,json.JSONDecodeError) as e:
    err(str(e))
if errors:
    print("FAIL",len(errors),"error(s)")
    for e in errors: print(" -",e)
    sys.exit(1)
print("PASS: 4 idiomas independentes, 30 temas, 5 indices, fontes e evidencias.")
print("NOT TESTED: revisao humana, audio, eficacia e URLs ao vivo.")
