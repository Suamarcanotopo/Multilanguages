#!/usr/bin/env python3
"""Valida alteracoes em branches por idioma, com git diff."""
import argparse
import re
import subprocess
import sys
p=argparse.ArgumentParser()
p.add_argument("--branch",required=True)
p.add_argument("--base",required=True)
a=p.parse_args()
m=re.match(r"^feat/idioma-(japones|ingles|alemao|frances)(?:-|/).+",a.branch)
if not m:
    print("SKIP: branch nao especifica idioma, auditoria geral.")
    sys.exit(0)
slug=m.group(1)
r=subprocess.run(["git","diff","--name-only","--diff-filter=ACMR",
                  "origin/"+a.base+"...HEAD"],capture_output=True,text=True)
if r.returncode:
    print("FAIL: nao foi possivel calcular o diff:",r.stderr)
    sys.exit(1)
cross=[f for f in r.stdout.splitlines()
       if f.startswith("idiomas/") and not f.startswith("idiomas/"+slug+"/")]
if cross:
    print("FAIL: branch de",slug,"modificou diretórios de outros idiomas:",*cross,sep="\n")
    sys.exit(1)
print("PASS: branch manteve isolamento do idioma",slug)
