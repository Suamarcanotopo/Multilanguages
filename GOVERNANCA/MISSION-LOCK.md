# MISSION LOCK — Pandora Survivor Teacher v0.1
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
3. 2 aulas demonstrativas em cada um dos 4 idiomas; 4 componentes por frase (original, pronúncia, tradução, uso).
4. Fontes gratuitas institucionais identificadas e separadas de comércio.
5. Validação automática de IDs/arquivos/URLs e CI configurada.
6. Coliseum audita limitações, evita alegar fluência, revisão nativa ou runtime inexistentes.
7. Handoff registra base, branch, PR, testes, próximos pacotes e rollback.

## Fora da missão inicial
Site/App, síntese ou gravação de áudio, certificação CEFR/JF, tradução de todas as 120 aulas, contas de alunos, pagamento, fóruns, importação integral de conteúdos de terceiros. Propor por PR distinto.

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
