# Dashboard · Pipeline de Projetos (Grupo Tigre)

Dashboard HTML único (`dashboard-projetos-tigre.html`), identidade visual Tigre, otimizado para tela de notebook (sem rolagem).
Lê os dados ao vivo do Supabase e, se estiver offline, usa o snapshot embutido no arquivo.

## Dados (Supabase)
- Projeto: `tigre-dashboard-projetos` (ref `kaymumapadfrrixooiiv`, região sa-east-1)
- `public.projetos` — 139 projetos (origem: `lista_projetos.xlsx`). Edite no **Table Editor** do Supabase; o dashboard reflete ao clicar em *Atualizar* (ou a cada 2 min).
- `public.metas` — metas por escopo (`Masterplan`, `Engenharia`, `Materiais`, `Manut/CDM`, `Transf. Digital`): `meta_p0` (80%), `meta_p1` (100%), `meta_p2` (120%), em R$.
  O `escopo` precisa ser igual ao valor da coluna `area` de `projetos` para o velocímetro achar a meta ao filtrar por área.
- RLS: leitura pública (chave anon); escrita só por quem tem acesso ao projeto Supabase.

## Regra do velocímetro
Atingimento = 80% × min(P0/meta_p0, 1) + 20% × min(P1/meta_p1, 1) + 20% × min(P2/meta_p2, 1), onde P0/P1/P2 = soma do `impacto_anual` dos projetos com a flag `p0`/`p1`/`p2` verdadeira, respeitando os filtros ativos.

## Regerar o HTML
`python3 build.py` (usa `template.html`, `assets/` e `snapshot.json`).
