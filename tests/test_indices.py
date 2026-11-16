"""Testes de isolamento e sincronizacao dos caminhos de idiomas."""
import json
import pathlib
import sys
import tempfile
import unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]/"scripts"))
import build_indices as b

class IsolationTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=pathlib.Path(self.tmp.name)
        (self.root/"catalogo").mkdir()
        self.cases=[{"id":"PST-001","titulo":"Saudacao","prioridade":"essencial"},
                    {"id":"PST-002","titulo":"Socorro","prioridade":"essencial"}]
        self.langs=[{"slug":s,"nome":s.title(),"variante":"padrao"} for s in b.ORDER]
        (self.root/"catalogo/casos.json").write_text(json.dumps({"casos":self.cases}),encoding="utf-8")
        (self.root/"catalogo/idiomas.json").write_text(json.dumps({"idiomas":self.langs}),encoding="utf-8")
        for lang in self.langs: (self.root/"idiomas"/lang["slug"]/"aulas").mkdir(parents=True)
    def tearDown(self): self.tmp.cleanup()
    def lesson(self,slug,id_,status="rascunho-exemplo"):
        (self.root/"idiomas"/slug/"aulas"/(id_+".md")).write_text(
            "# "+id_+" — Aula\n**Status:** "+b.Q+status+b.Q+"\n",encoding="utf-8")
    def test_japanese_lesson_not_created_in_other_language(self):
        self.lesson("japones","PST-002")
        state=b.progress(self.root,self.cases,self.langs)
        self.assertEqual(state["japones"],{"PST-002":"rascunho-exemplo"})
        for slug in ("ingles","alemao","frances"):
            self.assertEqual(state[slug],{})
        self.assertIn("Rascunho",b.language_index(self.cases,self.langs[0],state))
        self.assertNotIn("Rascunho",b.language_index(self.cases,self.langs[1],state))
    def test_unknown_case_fails(self):
        self.lesson("frances","PST-999")
        with self.assertRaises(ValueError): b.progress(self.root,self.cases,self.langs)
    def test_invalid_status_fails(self):
        self.lesson("ingles","PST-001","invalid")
        with self.assertRaises(ValueError): b.progress(self.root,self.cases,self.langs)

if __name__=="__main__": unittest.main()
