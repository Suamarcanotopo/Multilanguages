# HANDOFF CANÔNICO — Pandora Survivor Teacher
**Data:** 2026-11-16 · **Missão:** `GOVERNANCA/MISSION-LOCK.md` v0.2.0 · **Repositório:** `Suamarcanotopo/Multilanguages` · **PR:** [#1 em Draft](https://github.com/Suamarcanotopo/Multilanguages/pull/1).

## Estado da verdade, nunca presumir execução
- **Main intacta:** referência de base original `29ccce4dde6eef331df4c47a7b3584185c64fe1d`. Esta entrega permanece em `feat/pandora-survivor-teacher-foundation` até aprovação e merge humano.
- **Conteúdo gravado e confirmado por árvore Git:** **30 aulas japonesas + 30 inglesas + 30 alemãs + 30 francesas = 120 arquivos A0–A1**, IDs `PST-001` ... `PST-030`. Não existem as mesmas aulas repetidas em duas pastas dentro do mesmo idioma.
- **Diálogos por aula:** quatro turnos preenchidos `A/B/A/B`, total mínimo de **480 falas**, com original no idioma, leitura segmentada para brasileiros, tradução pt-BR e Hepburn para japonês.
- **Exercício resolvido:** cada aula inclui pequena missão, modelo de solução, avisos proporcionais e fontes institucionais gratuitas da língua.
- **Roteiro/Painel:** `README.md` lista integralmente 120 posições e `idiomas/<slug>/INDEX.md` mostra 30 aulas naquele idioma. Gerados por `python3 scripts/build_indices.py --write`; conferir com `--check`.
- **Evidências técnicas:** GitHub Actions [run 43964373305 — SUCCESS](https://github.com/Suamarcanotopo/Multilanguages/actions/runs/43964373305) no commit `771681a75b1a085b548a1023a59b510382d9964c`. Nesse run, índice, validador estrutural, testes unitários e isolamento de paths passaram.
- **Gates pendentes (não declarar PASS):** revisão humana/nativa **0/120 documentadas**; comparação de cada uma das 480 falas com áudio específico; AFI/IPA sistemático; testes com alunos; eficácia de comunicação em situação real; todos os links rechecados recentemente.

## Origem de erro e prevenção permanente
**Falha anterior:** aula da caneta (PST-002 japonês e outras línguas) continha turnos da pessoa B como instruções entre colchetes. A partir da missão v0.2, nenhum roteiro ou resposta pode depender de o aluno criar a frase inexistente.

**Proteção:** `scripts/validate_catalog.py` rejeita fala vazia, resposta sem som/tradução, conversas com menos de quatro turnos, mismatch entre frase do diálogo e tabela, falta de Hepburn japonês, placeholder e índice desatualizado. Diferenças gramaticais e fonéticas ainda precisam de revisão qualificada.

## Onde fica cada arquivo e como continuar
- `catalogo/casos.json`: pauta única de 30 temas, **não é contagem de conteúdos aprovados**.
- `idiomas/japones/aulas/PST-XXX.md`, `idiomas/ingles/aulas/PST-XXX.md`, `idiomas/alemao/aulas/PST-XXX.md`, `idiomas/frances/aulas/PST-XXX.md`: conteúdo canônico, sem intercâmbio de idiomas.
- `idiomas/<slug>/INDEX.md`: índice calculado pelas aulas reais, não por promessas.
- `idiomas/<slug>/GLOSSARIO.md`, `FONTES.md`, `COMPRAS-ONLINE.md`, `ANALOGIAS.md`: suportes por idioma, não duplicações.
- `catalogo/fontes.json` e `catalogo/evidencias.json`: fontes institucionais e vínculos de evidência, não atestados de tradução frase-a-frase.
- `DIDATICA/PRONUNCIA-BR.md`: política de aproximação; `DIDATICA/GUIA-DE-SONS.md`: como brasileiros devem ler as pistas e suas limitações.

**Passos para próxima IA/LLM:** (1) ler Mission Lock + AGENTS + este Handoff; (2) escolher **um idioma e uma aula**; (3) verificar falas, formalidade, escrita, pronúncia e fontes com especialista e áudio; (4) atualizar só o arquivo da aula e registros de evidência verificáveis; (5) executar `python3 scripts/build_indices.py --write` e `python3 scripts/validate_catalog.py` e testes; (6) submeter PR específica `feat/idioma-<slug>-...` sem tocar em outro idioma; (7) informar com contagem de arquivos, status, gaps, hash e URL de PR.

## Evidência ≠ conclusão
As 120 aulas são **rascunhos preenchidos**, não certificações ou cursos homologados. As pistas pt-BR não são a notação internacional AFI e podem estar imprecisas. As fontes institucionais permitem escuta e estudo, mas suas páginas iniciais não provam cada frase do conteúdo. **Jamais alterar `rascunho-exemplo` para `aprovado` sem revisor, variante, data e prova direta**.

## Proteção de downside e rollback
A biblioteca continua gratuita e aproveitável como corpus de tradução, roteiro para vídeos e material de ensino, mesmo se uma oferta comercial não for criada. Em erro grave, bloquear promoção, reverter o commit/PR no GitHub, preservar logs e reaplicar a última versão verificada. `main` não deve ser alterada automaticamente.
