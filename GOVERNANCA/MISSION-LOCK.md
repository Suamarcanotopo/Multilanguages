# MISSION LOCK — Pandora Survivor Teacher v0.2.0
**Estado:** proposta em branch de trabalho; obrigatório para contribuidores quando integrado à main. **Owner:** mantenedor autorizado do repositório.

## Missão
Construir, em português brasileiro, quatro trilhas iniciais (japonês, inglês, alemão, francês) que habilitem alunos iniciantes, principalmente 14–24 anos, a agir em situações reais de vida no país de destino. Estender idiomas somente sem perda de padrão.

## Requisitos imutáveis sem autorização do Owner
- Ensino por **situação real, progressão pergunta → pedido educado → aprofundamento → resposta → variação**; não apenas glossários.
- Original no idioma + tradução natural pt-BR + aproximação acessível + explicação de uso + contraste entre informalidade/formalidade.
- Áudio/vídeo gratuito institucional quando disponível, e fonte oficial verificável para informações sensíveis; nunca fabricar pronunciamento nativo.
- Uma única chave primária por conteúdo: `idioma + case_id`; índice independente por idioma, um catálogo compartilhado de cenários e de fontes.
- Sem duplicar dependências, arquivos, IDs ou conteúdo canônico. Tradução paralela dos **mesmos cenários em outros idiomas** é necessária e **não é duplicação**.
- Conteúdo para menores: nada de coleta de identidade, contato, geolocalização de menores ou estímulo a encontros arriscados; cenários de relacionamento usam respeito e consentimento.
- Status claros: `planejado` → `rascunho-exemplo` → `revisao-linguistica` → `aprovado`. Nenhuma mudança para `aprovado` sem evidência humana.
- Segurança: sem aconselhamento médico ou jurídico individual; emergências remetem a serviços locais verificados.
- ECP = Engineering Control Plane (plano de controle de engenharia); Coliseum = revisão adversarial, fontes e testes, sem fingir execução autônoma. Aplicar contratos SIN como critérios **sem copiar skills privadas**.
- Não alterar `main` sem PR, testes e aprovação; rollback por revert do commit ou PR.
- Fontes do país e Brasil em ordem de prioridade: órgão público/instituto cultural/rede pública → universidade/instituição educacional → mídia educacional identificada → comunidade com ressalva.
- Todo link externo tem URL, tipo, aplicação, acesso gratuito informado, data de checagem, limite de confiança e responsabilidade de revisita.

## Completion Contract
1. Índice global e quatro índices individuais navegam com links válidos.
2. 30 situações catalogadas sem duplicidade; estado verdadeiro de cada entrega.
3. 30 aulas introdutórias e úteis por idioma (120 aulas em rascunho de primeira etapa); em cada aula quatro falas originais completas com pronúncia aproximada pt-BR, tradução, contexto, duas trocas de diálogo e exercício com solução.
4. Fontes gratuitas institucionais identificadas e separadas de comércio.
5. Validação automática de IDs/arquivos/URLs e CI configurada.
6. Coliseum audita limitações, evita alegar fluência, revisão nativa ou runtime inexistentes.
7. Handoff registra base, branch, PR, testes, próximos pacotes e rollback.

## Fora da missão inicial
Site/App, síntese ou gravação de áudio, certificação CEFR/JF, contas de alunos, pagamento, fóruns, importação integral de conteúdos de terceiros. **As 120 aulas iniciais estão agora no escopo da missão**, mediante solicitação explícita em 2026-11-16. Propor por PR distinto.

## Prioridades
1. Segurança e fontes; 2. quatro caminhos e estrutura; 3. conteúdos essenciais; 4. revisão linguística; 5. experiência audiovisual com licenças e testes; 6. crescimento comercial opcional sem prejudicar acesso gratuito.

## Mudanças
Novo pedido que colida com a missão: registrar delta, risco, opção de rollback e aprovação explícita. Não substituir esta constituição silenciosamente.

## Emenda autoral — índices completos e isolamento (2026-11-16)
- **README raiz:** quatro blocos independentes de 30 assuntos cada; índice do idioma contém seus próprios links, estado e referências. Um único repositório; nenhuma obrigatoriedade de criar repositórios separados por idioma.
- **Não compartilhar progresso:** `catalogo/casos.json` é somente índice de temas; `idiomas/<slug>/aulas/PST-XXX.md` determina estado daquele idioma. Proibir a mesma aula em duas localizações dentro do idioma.
- **Atualização automática controlada:** gerador `scripts/build_indices.py --write` e verificador `--check`, testes e CI. Índices são arquivos derivados, não manuais. Nenhuma PR pode permanecer com índice defasado.
- **Isolamento forte:** branches `feat/idioma-<slug>-...` não podem editar conteúdo de outros idiomas. Alteração de esquema global é decisão separada do Owner.
- **Analogias curtas:** referências culturais a cinco obras, sempre exemplos originais com tradução para pt-BR e pistas de som. Nada de diálogos, imagens ou trechos extensos protegidos; preservar segurança, atribuição e ausência de endosso.
- **Evidência:** CI, testes e links não equivalem à aprovação por professores ou falantes nativos. Manter status de rascunho até revisão.

## Emenda obrigatória v0.2 — Nenhuma fala faltando (2026-11-16)
**Motivo verificado:** PST-002 em japonês e outros idiomas apresentavam respostas da pessoa B entre colchetes sem traduções ou sons. Um iniciante não consegue usar material assim.

### Completion Contract ampliado — exigências para cada uma das 120 aulas iniciais
1. Um arquivo por par idioma+cenário, usando `idiomas/<slug>/aulas/PST-XXX.md`; 30 situações em cada uma das quatro pastas, nível **A0–A1 de sobrevivência cotidiana**, sem conteúdo avançado antecipado.
2. Toda fala ensinada (inclusive as de pessoa B) precisa de **texto original + indicação legível de pronúncia brasileira segmentada + tradução pt-BR**. Japonês acrescenta **romanização Hepburn** e preserva kana/kanji; a escrita em alfabeto latino não substitui som real.
3. **Mini-diálogos completos com turnos A e B preenchidos**; não publicar `[responda...]`, `[explique...]`, `...`, `TODO`, frases vazias ou pedidos para o aluno inventar uma fala ausente.
4. Cada cenário é aula inicial autossuficiente: onde usar, ao menos duas trocas de pergunta e resposta, vocabulário contextual, missão prática simples, solução e fonte gratuita do idioma; perguntas e respostas devem fazer sentido entre si.
5. Pronúncia aproximada é **material autoral auxiliar**, nunca alegação de fonética exata. Dizer explicitamente quais sons não existem no português e remeter a áudio institucional. Revisão por docente/falante nativo **PENDENTE** até comprovada.
6. Não repetir diálogo genérico em todas as situações: cada caso precisa ter assunto e ação próprios, apoiados por frases adequadas. Saúde, emergência, polícia e compras exigem avisos específicos, sem orientação médica ou legal.
7. **O índice pode listar uma aula como 'Rascunho' apenas se arquivo existir e passar verificador de completude.** Nunca confundir arquivo criado, texto escrito e revisão linguística concluída.
8. ECP coordena; Coliseum rejeita placebo didático, placeholder, fonética ausente, mistura de idiomas, prova não existente e declarações exageradas; GitHub CI valida estrutura, mas **não substitui revisão docente**.
9. Preservar o foco em sobrevivência e adaptação, não restringir a aula da caneta. Ordem de abordagem: cumprimentos e comunicação, ajuda e orientação, compras/serviços, vida escolar/social, família e lazer, serviços críticos.

### Protocolo de continuidade/rollback
Missão só fica concluída quando o repositório apresentar contagem comprovada de 30 arquivos por idioma, índices coerentes, testes automatizados aprovados e nenhum turno sem tradução/pronúncia. Revisão humana e áudio individualizado são gates **separados**, pendentes até evidência. Commits sempre em PR Draft, com rollback por revert; não modificar main automaticamente.
