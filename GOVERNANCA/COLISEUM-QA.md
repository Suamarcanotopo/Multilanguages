# Coliseum — Revisão adversarial da fundação
Objeto: proposta de currículo inicial em 4 idiomas.
## Matriz
| Arena | Teste | Resultado inicial |
|---|---|---|
| Escopo | 4 idiomas e 30 casos com IDs únicos | checagem estrutural automatizável |
| Verdade | Status de aula rascunho separado de aprovada | previsto |
| Segurança | emergência, menores e saúde com limites | previsto |
| Pronúncia | pistas pt-BR + áudio oficial; nativo revisou? | **RETEST: não revisado** |
| Fontes | recursos gratuitos institucionais conferidos | **ACCEPT para catalogação, não para cada frase** |
| Direitos | links e resumos próprios; sem copiar materiais | previsto |
| Disponibilidade | acesso real a todos os vídeos e portais em diferentes países | **RETEST: variável** |
| Eficácia | aluno compreende e consegue se comunicar? | **RETEST: teste com usuários não realizado** |
| CI | verificador de estrutura | depende de execução |
| Merge | aprovação humana do PR | pendente |
## Ataques de revisão
- Japonês sem kana/kanji ou marca de vogal longa → bloquear.
- Alemão tratado sempre por `du` com desconhecidos → bloquear.
- Francês com nasalidade ignorada → bloquear homologação.
- Inglês `lend` vs `borrow` confundidos → bloquear.
- Links de compras tratados como recomendação de segurança → bloquear.
- Mesmo `case_id` repetido dentro do mesmo idioma → bloquear.
- Fonte geral usada como 'prova' de frase sem correspondência real → marcar evidência insuficiente.

**Veredito projetado:** `RETEST` antes de promoção para curso homologado. A fundação é candidata e pode entrar como rascunho informativo após testes, não como curso certificado.
