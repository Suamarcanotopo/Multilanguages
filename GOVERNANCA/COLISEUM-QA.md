# Coliseum — Aulas iniciais 120 × quatro turnos

## Resumo da auditoria executada (16/11/2026)
**Escopo técnico comprovado:** árvore Git contém 30 arquivos por idioma; README e quatro índices incluem conteúdos correspondentes; CI GitHub Actions run `43964373305` concluiu com **success** para validação do corpus após corrigir as verificações antigas.

## Arenas e veredictos
| Arena | Evidência | Veredito |
|---|---|---|
| Integridade de arquivos | 120 aulas distribuídas 30/idioma | ACCEPT (estrutura) |
| Diálogos A/B/A/B | 480 turnos com original, som brasileiro e tradução | ACCEPT (estrutura) |
| Ausência de placeholders | validador bloqueia respostas em colchetes, TODO e reticências vazias | ACCEPT (gate) |
| Pronúncia por brasileiro | pistas segmentadas nos turnos; sons sem equivalente explícitos no guia | ACCEPT como auxílio inicial, **RETEST precisão** |
| Romanização japonesa | Hepburn presente nos turnos japoneses | ACCEPT presença, **RETEST fidelidade** |
| Qualidade da tradução e naturalidade | 120 rascunhos sem parecer nativo registrado | RETEST |
| Fonte oficial por frase | links institucionais de estudo; correspondência literal não comprovada | RETEST |
| Acessibilidade real | não testada com alunos | RETEST |
| Segurança | avisos para farmácia, hospital, alergia, polícia, dinheiro, sites | RETEST especialistas |
| Publicação em main | PR #1 Draft | BLOQUEADA para merge automático |

## Gaps observados e consertados
1. PST-002 trazia respostas B não produzidas: todos os turnos foram reescritos.
2. Validador inicial se guiava pelo título literal de seção 'Fontes gratuitas', reprovando inglês/francês apesar de haver links. Substituído por regra sobre **URL/arquivo de fonte existente** e conferência de turnos; run final aprovado.
3. Os índices só exibiam 2/30: passaram a mostrar 30/30 em cada idioma, mantendo status *Rascunho*.
4. O Handoff antigo descrevia '28 pendentes por idioma' e foi substituído por estado atual explícito.

## Limites de confiança
Nenhum ECP/Coliseum autônomo foi executado em host separado; a revisão seguiu seus **contratos documentados**. CI prova invariantes estruturais e não pode certificar que uma pista escrita reproduz o som real. Revisão linguística especializada é bloqueador para status *aprovado*.

## Próximo gate independente
Professor/falante competente verifica amostra do conteúdo, prioriza aulas críticas (PST-005, 006, 022, 024), compara cada frase com material de áudio, corrige incorreções e registra fonte/revisão. Só depois libera aprovação por idioma e cenário.
