#!/usr/bin/env python3
"""Pandora Survivor Teacher — gate de conteudo e indices, sem inferir homologacao linguistica."""
import json
import pathlib
import re
import sys
from urllib.parse import urlparse
import build_indices as idx

ROOT=pathlib.Path(__file__).resolve().parents[1]
ERRORS=[]
def fail(msg): ERRORS.append(msg)
def read_json(name): return json.loads((ROOT/name).read_text(encoding="utf-8"))
def unique(vals,label):
    if len(vals)!=len(set(vals)): fail("ID duplicado: "+label)
def verify_lesson(lang,case_id,path,state):
    text=path.read_text(encoding="utf-8")
    short=f"{lang}/{case_id}"
    if not text.startswith(f"# {case_id} —"): fail(short+": cabecalho incorreto")
    if state=="rascunho-exemplo" and "PENDENTE" not in text: fail(short+": nao informa revisao pendente")
    if state=="aprovado":
        for tag in ("**Revisor responsável:**","**Data da revisão:**","**Fonte de áudio revisada:**"):
            if tag not in text: fail(short+": falta prova para status aprovado: "+tag)
        if "PENDENTE" in text: fail(short+": aprovado com revisao pendente")
    forbidden=(r"\[\s*[Rr]esponda[^\]]*\]",r"\[\s*[Ee]xplique[^\]]*\]",
               r"\[\s*[Cc]omplete[^\]]*\]",r"\[\s*[Tt]raduz[^\]]*\]",r"\bTODO\b",r"\bTBD\b",
               r"\.{3}")
    for pattern in forbidden:
        if re.search(pattern,text): fail(short+": placeholder detectado "+pattern)
    # Conteudo completo; cada frase original, seu som e sua traducao devem acompanhar a pessoa correta.
    lines=text.splitlines()
    markers={
       "japones":("Romanização","Como falar","Tradução"),
       "ingles":("Como falar","Tradução"),
       "alemao":("Como pronunciar","Tradução para o português"),
       "frances":("Como falar","Em português"),
    }[lang]
    turns=[]
    pattern=re.compile(r"^\*\*Pessoa ([AB])(?: — [^\n*]+)?:\*\*\s*(.+)$")
    for num,line in enumerate(lines):
        found=pattern.fullmatch(line.strip())
        if not found: continue
        role,original=found.groups()
        if not original.strip(): fail(short+": fala original vazia")
        fields={}
        for offset,label in enumerate(markers,1):
            if num+offset>=len(lines):
                fail(short+": fala com campos faltantes")
                break
            prefix=f"- **{label}:** "
            next_line=lines[num+offset]
            if not next_line.startswith(prefix):
                fail(short+": falta "+label+" depois da fala "+str(len(turns)+1))
            else:
                value=next_line[len(prefix):].strip()
                if not value or value in ("—","-","?"):
                    fail(short+": campo "+label+" vazio")
                fields[label]=value
        turns.append((role,original,fields))
    if len(turns)!=4 or [t[0] for t in turns]!=["A","B","A","B"]:
        fail(short+": dialogo deve ter A/B/A/B, quatro falas completas")
    table=[]
    for line in lines:
        if not (line.startswith("| Pessoa A | ") or line.startswith("| Pessoa B | ")): continue
        values=[x.strip() for x in line.split("|")[1:-1]]
        expected_cols=5 if lang=="japones" else 4
        if len(values)!=expected_cols or any(not item for item in values):
            fail(short+": linha de tabela com campos vazios")
        table.append(values)
    if len(table)!=4: fail(short+": tabela precisa ter 4 linhas de fala completas")
    if len(table)==4 and len(turns)==4:
        for i,(role,original,fields) in enumerate(turns):
            row=table[i]
            if row[0]!=f"Pessoa {role}" or row[1]!=original:
                fail(short+": frase da tabela e dialogo nao correspondem no turno "+str(i+1))
            sound=row[3] if lang=="japones" else row[2]
            sound=sound.strip("* ")
            glossary_label="Como falar" if lang in ("japones","ingles","frances") else "Como pronunciar"
            if fields.get(glossary_label)!=sound:
                fail(short+": fonetica da tabela difere do dialogo no turno "+str(i+1))
            translation=row[-1]
            label="Tradução" if lang in ("japones","ingles") else ("Tradução para o português" if lang=="alemao" else "Em português")
            if fields.get(label)!=translation:
                fail(short+": traducao da tabela difere do dialogo no turno "+str(i+1))
            if lang=="japones" and fields.get("Romanização")!=row[2]:
                fail(short+": Hepburn da tabela difere do dialogo no turno "+str(i+1))
    if "../FONTES.md" not in text:
        fail(short+": faltou link para fontes gratuitas do idioma")
    if "PENDENTE" not in text and state!="aprovado":
        fail(short+": revisão não indicada como pendente")
    if not ("Modelo" in text or "Solução" in text or "solução" in text or "modelo" in text):
        fail(short+": falta resposta do exercicio")
    if "https://" not in text: fail(short+": falta URL da fonte gratuita")
try:
    cases,languages=idx.data(ROOT)
    states=idx.progress(ROOT,cases,languages)
    if len(cases)!=30 or len(languages)!=4:
        fail("Contrato de 30 cenarios por idioma e 4 idiomas nao atendido")
    if any("status" in c for c in cases): fail("Status proibido no catalogo compartilhado de temas")
    if any("status" in l for l in languages): fail("Status proibido no catalogo compartilhado de idiomas")
    sources=read_json("catalogo/fontes.json")["fontes"]
    shops=read_json("catalogo/lojas.json")["lojas"]
    evidence=read_json("catalogo/evidencias.json")["entries"]
    unique([s["id"] for s in sources],"fontes")
    unique([s["id"] for s in shops],"lojas")
    unique([s["id"] for s in evidence],"evidencias")
    unique([s["url"] for s in sources],"URLs fontes")
    slugs={l["slug"] for l in languages}
    ids={c["id"] for c in cases}
    for entry in sources+shops+evidence:
        url=entry.get("url","")
        parsed=urlparse(url)
        if parsed.scheme!="https" or not parsed.netloc or any(ch.isspace() for ch in url):
            fail("URL malformada: "+url)
    for entry in evidence:
        if entry.get("idioma") not in slugs or entry.get("case_id") not in ids:
            fail("Evidencia orfa: "+entry.get("id","?"))
        if entry.get("confirmacao_frase_exata") and not entry.get("revisor"):
            fail("Fonte por frase sem comprovacao do revisor: "+entry.get("id","?"))
    for lang in languages:
        slug=lang["slug"]
        folder=ROOT/"idiomas"/slug
        for f in ("README.md","INDEX.md","GLOSSARIO.md","FONTES.md","COMPRAS-ONLINE.md","ANALOGIAS.md"):
            if not (folder/f).is_file(): fail("Arquivo do idioma ausente: "+slug+"/"+f)
        if set(states[slug])!=ids:
            fail(slug+": esperadas 30 aulas, faltam "+str(sorted(ids-set(states[slug]))))
        if not any(s["idioma"]==slug and s.get("acesso")=="gratuito-institucional" for s in sources):
            fail(slug+": falta fonte institucional gratuita")
        for md in folder.rglob("*.md"):
            content=md.read_text(encoding="utf-8")
            for other in slugs-{slug}:
                if ("idiomas/"+other+"/") in content or ("../"+other+"/") in content:
                    fail("Contaminacao cruzada: "+str(md.relative_to(ROOT))+" => "+other)
        for case_id,status in states[slug].items():
            verify_lesson(slug,case_id,folder/"aulas"/(case_id+".md"),status)
        analogy=(folder/"ANALOGIAS.md").read_text(encoding="utf-8")
        if "Pista para brasileiros" not in analogy or "Tradução em português" not in analogy:
            fail("Analogia sem som e traducao: "+slug)
    generated=idx.outputs(ROOT)
    for path,text in generated.items():
        if not path.is_file() or path.read_text(encoding="utf-8")!=text:
            fail("Indice gerado divergiu: "+str(path.relative_to(ROOT)))
    portal=(ROOT/"INDICES/INDEX.md").read_text(encoding="utf-8")
    for slug in slugs:
        if "idiomas/"+slug+"/INDEX.md" not in portal:
            fail("Portal sem o indice do idioma: "+slug)
except (ValueError,OSError,json.JSONDecodeError) as err:
    fail(str(err))
if ERRORS:
    print("FAIL",len(ERRORS),"erros")
    for item in ERRORS: print(" -",item)
    sys.exit(1)
print("PASS: 120 aulas A0-A1, 480 falas A/B com original, som e traducao, 4 indices e fontes.")
print("ATENCAO: completude estrutural nao valida fonetica, traducao, contexto cultural ou som nativo.")
