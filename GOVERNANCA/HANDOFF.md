# HANDOFF — Pandora Survivor Teacher
Atualizado: 2026-11-16. Release proposta: `0.1.0-rc.1`.

## Estado verdadeiro
- Base auditada `main`: commit `29ccce4dde6eef331df4c47a7b3584185c64fe1d`, árvore `f29efbce8903bfdfe9780882b0ddda2cefe0313a`, contendo somente `README.md` de apresentação.
- Branch de trabalho: `feat/pandora-survivor-teacher-foundation`. PR em Draft para revisão; **não representa integração na main**.
- Escopo proposto nesta fundação: 4 trilhas, 30 situações no catálogo, 2 aulas demonstrativas por idioma, glossários iniciais, links gratuitos e regras de manutenção.
- **Pendente:** 28 cenários em cada idioma; revisão por professor/nativo; gravações de áudio; acessibilidade revisada com usuários; testes reais de aprendizagem; auditoria humana dos portais de compra; validação operacional de todos os URLs periodicamente.
- Não há alegação de instalação de skills externas, teste de eficácia com estudantes ou aprovação linguística nativa.

## Como continuar em nova IA
1. Ler `AGENTS.md` e `GOVERNANCA/MISSION-LOCK.md`.
2. Consultar `catalogo/casos.json`, escolher caso ainda planejado e `idiomas/<slug>/INDEX.md`.
3. Acrescentar **somente** `idiomas/<slug>/aulas/PST-XXX.md` e atualizar o respectivo `INDEX.md` e `catalogo/casos.json` conforme política de status (catálogo registra status comum dos exemplos iniciais, depois migrar para progresso por idioma).
4. Conferir fonética com áudio de fonte nativa; registrar revisor, data, variante, evidência; se sem revisão, usar rascunho.
5. Rodar `python3 scripts/validate_catalog.py`. Registrar resultado em PR.
6. Coliseum: contesta plausibilidade, informações perigosas, direitos, links falsos, duplicação, traduções literais e falsa segurança.
7. Solicitar revisão e aprovar antes do merge. Rollback: reverter PR/commit, nunca apagar histórico.

## Próxima melhoria do esquema
Mover estado de cada `idioma + case_id` para `catalogo/progresso.json` para acompanhar diferença de maturidade entre idiomas, em vez de um estado compartilhado da pauta. A fundação não deve confundir status da pauta com status de tradução revisada.

## Manutenção
- Renovar verificação dos links em intervalos definidos, especialmente cursos, número de emergência, compras e recursos regionais.
- Adotar avaliações por pré-teste / pós-teste e repetição espaçada quando houver dados consentidos; coleta para menores exige projeto específico de privacidade.
- Evitar expansão horizontal de 120 aulas incompletas antes de homologar os primeiros cenários de maior risco e utilidade.

## Complemento: provas por aula (2026-11-16)
- `catalogo/evidencias.json` separa material que demonstra uma **estrutura ou tema** de evidência de **frase literal**. Todos os 8 pares idioma/caso têm ao menos uma fonte adicional de estudo, e **nenhuma** prova revisão da frase exata inteira.
- Os links específicos estão na seção 8 de cada aula. Revisor futuro deve promover um vínculo por frase somente se encontrar e registrar transcrição/áudio correspondente.
- CI estrutural deve checar evidências além dos IDs e da árvore do projeto. PR #1 continua em Draft.

## Onda 2 — indexação completa, analogias e proteção (2026-11-16)
- PR #1: 4 x 30 linhas independentes no README raiz + `idiomas/<slug>/INDEX.md` em cada trilha; `idiomas/<slug>/README.md` facilita navegar no diretório pelo GitHub.
- Catálogo `catalogo/casos.json` passou a manter apenas assuntos, IDs e prioridades; cada arquivo de aula é a fonte única de sua situação. Não atualizar estado global de conteúdo.
- Script `scripts/build_indices.py --write` gera índices; `--check` e `scripts/validate_catalog.py` fiscalizam links, status e isolamento. `tests/test_indices.py` testa nova aula apenas em um idioma; `scripts/check_scope.py` protege branches com slug explícito.
- Foram criados `idiomas/<slug>/ANALOGIAS.md` com exemplos didáticos **não atribuídos** a obras e com orientações de pronúncia provisórias; 12 analogias na fundação.
- Continuar: escolher um único `<slug>`, criar `aulas/PST-XXX.md`, registrar `**Status:**`, conferir fontes e áudio, executar gerador e testes, abrir PR Draft; não misturar com outras línguas.
- 8 aulas iniciais continuam rascunhos sem homologação nativa. Não confundir índice preenchido com 120 aulas produzidas.
