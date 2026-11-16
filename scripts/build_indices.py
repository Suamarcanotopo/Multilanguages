#!/usr/bin/env python3
"""Gera índices por idioma; aulas e fontes permanecem intocadas."""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
ORDER = ("japones", "ingles", "alemao", "frances")
FLAGS = {"japones": "🇯🇵", "ingles": "🇺🇸", "alemao": "🇩🇪", "frances": "🇫🇷"}
DISPLAY = {"rascunho-exemplo": "Rascunho", "revisao-linguistica": "Em revisão", "aprovado": "Aprovada"}
START = "<!-- PANDORA:ROOT-INDEX:START -->"
END = "<!-- PANDORA:ROOT-INDEX:END -->"
Q = chr(96)
STATUS = re.compile(r"\*\*Status:\*\*\s*"+Q+r"?([a-z-]+)"+Q+r"?", re.I)

def data(root=ROOT):
    cases = json.loads((root/"catalogo/casos.json").read_text(encoding="utf-8"))["casos"]
    langs = json.loads((root/"catalogo/idiomas.json").read_text(encoding="utf-8"))["idiomas"]
    language_map = {lang["slug"]: lang for lang in langs}
    if set(language_map) != set(ORDER) or len(langs) != len(ORDER):
        raise ValueError("Os quatro idiomas devem ter slugs únicos e válidos.")
    ids = [c["id"] for c in cases]
    if len(ids) != len(set(ids)) or not all(re.fullmatch(r"PST-\d{3}", i) for i in ids):
        raise ValueError("IDs de cenário duplicados ou inválidos.")
    return cases, [language_map[k] for k in ORDER]

def progress(root, cases, langs):
    available = {c["id"] for c in cases}
    result = {}
    for lang in langs:
        slug = lang["slug"]
        found = {}
        for p in sorted((root/"idiomas"/slug/"aulas").glob("*.md")):
            if p.stem not in available or p.name != p.stem+".md":
                raise ValueError(f"Aula fora do catálogo: {p}")
            m = STATUS.search(p.read_text(encoding="utf-8"))
            if not m or m.group(1) not in DISPLAY:
                raise ValueError(f"Status ausente ou inválido: {p}")
            found[p.stem] = m.group(1)
        result[slug] = found
    return result

def root_index(cases, langs, states):
    lines = [START, "## Índice completo por idioma",
      "> Cada trilha tem arquivos e links próprios. Português brasileiro aparece apenas em traduções e explicações; o progresso de um idioma não altera outro.", ""]
    for lang in langs:
        slug = lang["slug"]
        found = states[slug]
        lines += [
          f'### {FLAGS[slug]} {lang["nome"]} — {len(found)}/{len(cases)} aulas criadas',
          f'**[Índice exclusivo de {lang["nome"]}](idiomas/{slug}/INDEX.md)** · [Analogias](idiomas/{slug}/ANALOGIAS.md) · [Fontes e vídeos](idiomas/{slug}/FONTES.md)',
          "", "| Código | Situação do cotidiano | Estado | Aula neste idioma |",
          "|---|---|---|---|"]
        for c in cases:
            cid = c["id"]
            status = DISPLAY.get(found.get(cid), "Planejada")
            link = f"[Abrir](idiomas/{slug}/aulas/{cid}.md)" if cid in found else "A produzir"
            lines.append(f'| {cid} | {c["titulo"]} | {status} | {link} |')
        lines.append("")
    lines += [
       "**Sincronizar:** "+Q+"python3 scripts/build_indices.py --write"+Q+
       " · **Conferir:** "+Q+"python3 scripts/build_indices.py --check"+Q+
       ". O GitHub bloqueia PR com índice desatualizado.",
       "", END]
    return "\n".join(lines)

def language_index(cases, lang, states):
    slug = lang["slug"]
    found = states[slug]
    approved = sum(v == "aprovado" for v in found.values())
    lines = [
      f'# {lang["nome"]} — Índice completo da trilha',
      f'**Variante:** {lang["variante"]}. **Explicação:** português brasileiro. **Público:** a partir de 14 anos.',
      "",
      f"**Progresso deste idioma:** {len(found)}/{len(cases)} aulas criadas; {approved} homologadas. As outras línguas não são incluídas aqui.",
      "",
      "## Comece por aqui",
      "1. [Guia de pronúncia para brasileiros](../../DIDATICA/PRONUNCIA-BR.md).",
      "2. Escolha um caso com material disponível e pratique a pergunta, o pedido e a resposta.",
      "3. [Escute conteúdos gratuitos de instituições identificadas](FONTES.md).",
      "4. [Aplique analogias com séries, filmes e animes](ANALOGIAS.md).",
      "",
      "## Índice de todas as situações",
      "| Código | Tema | Prioridade | Estado | Aula deste idioma |",
      "|---|---|---|---|---|"]
    for c in cases:
        cid = c["id"]
        status = DISPLAY.get(found.get(cid), "Planejada")
        link = f"[Ler aula](aulas/{cid}.md)" if cid in found else "Ainda não criada"
        lines.append(f'| {cid} | {c["titulo"]} | {c["prioridade"]} | {status} | {link} |')
    lines += [
       "",
       "## Biblioteca exclusiva deste idioma",
       "- [Glossário por assunto](GLOSSARIO.md)",
       "- [Fontes oficiais, vídeos e áudio](FONTES.md)",
       "- [Compras online e segurança](COMPRAS-ONLINE.md)",
       "- [Analogias e missões curtas](ANALOGIAS.md)",
       "",
       "## Atualização sem misturar os idiomas",
       "A fonte da verdade é cada arquivo de aula em "+Q+"idiomas/"+slug+"/aulas/PST-XXX.md"+Q+
       ", com campo "+Q+"**Status:**"+Q+". Esta página é um índice gerado, nunca uma segunda cópia das aulas.",
       "",
       "**Gerar:** "+Q+"python3 scripts/build_indices.py --write"+Q+
       " · **Verificar:** "+Q+"python3 scripts/build_indices.py --check"+Q+
       ". A aprovação linguística exige evidências humanas.",
       ""]
    return "\n".join(lines)

def outputs(root=ROOT):
    cases, langs = data(root)
    states = progress(root, cases, langs)
    path = root/"README.md"
    readme = path.read_text(encoding="utf-8")
    if readme.count(START)!=1 or readme.count(END)!=1 or readme.index(START)>readme.index(END):
        raise ValueError("README sem marcadores únicos de índice.")
    new_readme = readme[:readme.index(START)] + root_index(cases, langs, states) + readme[readme.index(END)+len(END):]
    output = {path:new_readme}
    for lang in langs:
        output[root/"idiomas"/lang["slug"]/"INDEX.md"] = language_index(cases, lang, states)
    return output

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        docs = outputs()
        changed = [p for p, text in docs.items() if not p.exists() or p.read_text(encoding="utf-8")!=text]
        if args.write:
            for p in changed:
                p.write_text(docs[p], encoding="utf-8")
            print(f"UPDATED {len(changed)} of 5 controlled indices.")
            return 0
        if changed:
            for p in changed:
                print("STALE",p.relative_to(ROOT))
            print("Run: python3 scripts/build_indices.py --write")
            return 1
        print("PASS: complete index synced in README and 4 isolated languages.")
        return 0
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print("FAIL:",exc)
        return 1

if __name__ == "__main__":
    sys.exit(main())
