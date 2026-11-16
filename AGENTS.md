# Instruções para qualquer agente ou IA — Pandora Survivor Teacher
1. Leia, nesta ordem, `GOVERNANCA/MISSION-LOCK.md`, `GOVERNANCA/HANDOFF.md`, `catalogo/casos.json`, `catalogo/idiomas.json` e índice do idioma a editar.
2. Não afirme que uma skill foi executada, que nativos revisaram uma frase, ou que áudio foi validado sem evidência de execução.
3. Escopo mínimo: altere **apenas o idioma e cenário solicitados**, sem regenerar conteúdo de outros idiomas. Para mudar o esquema compartilhado, abra alteração separada revisada.
4. Uma aula = exatamente um par `idioma + case_id`; caminho canônico `idiomas/<idioma>/aulas/<case_id>.md`. Não crie cópias, aliases de conteúdo ou dependências paralelas. Links transversais são permitidos.
5. Fonte canônica das pautas: `catalogo/casos.json`; fonte canônica de URLs gratuitas: `catalogo/fontes.json`. Não duplique IDs; não copie vídeos ou materiais protegidos.
6. Cada aula nova precisa: frase original, tradução pt-BR, pista de pronúncia, formalidade, uso/alerta, substituição, mini-diálogo, desafio, resposta, recursos oficiais e estado de revisão.
7. Para japonês, preserve kana/kanji + Hepburn; para outras línguas, preserve original e registre variante regional. PT-BR é **aproximação não certificada**; não substitui áudio nativo.
8. Frases perigosas (saúde, polícia, emergência, golpes) exigem revisão especializada, alerta de limites e proíbem inventar números de emergência. Dado variável precisa de fonte oficial do país e data.
9. Crie branches como `feat/idioma-<slug>-pst-<id>`; revisão por Pull Request em Draft. Nada de merge automático ou escrita em outros repositórios.
10. Antes de PR, rode `python3 scripts/validate_catalog.py`; registre testes, revisão humana e reversão em `GOVERNANCA/HANDOFF.md`.
11. Fontes gratuitas são priorizadas. Não afirmar que órgão endossa o projeto; distinguir portal de aprendizagem, canal em vídeo, fonte linguística e fonte de proteção ao consumidor.
12. Se a missão mudar, proponha emenda explícita ao Mission Lock antes de executar. Respeite permissões, histórico, direitos autorais e integridade de conteúdo.

## Índices e isolamento — emenda de 16/11/2026
13. Antes de editar, ler o Mission Lock e o índice exclusivo do idioma. Escrever conteúdo da aula somente em `idiomas/<slug>/aulas/PST-XXX.md`.
14. O catálogo `catalogo/casos.json` registra **somente temas**, nunca o progresso geral de um idioma. O campo `**Status:**` fica no arquivo de aula.
15. Após incluir ou revisar uma aula, executar `python3 scripts/build_indices.py --write`; o script altera só `README.md` e os quatro `INDEX.md` gerados quando estiverem desatualizados. Depois executar `python3 scripts/validate_catalog.py` e testes.
16. É proibido incluir link para aula de outro idioma dentro de `idiomas/<slug>/`. Nas branches `feat/idioma-<slug>-...` o CI rejeita alterações em diretórios de outros idiomas.
17. Analogias com Naruto, Dragon Ball, Harry Potter, The Walking Dead e O Senhor dos Anéis são **exercícios originais**, não falas/cenas reais, com pronúncia aproximada ainda não homologada.
