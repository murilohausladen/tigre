"""Gera dashboard-projetos-tigre.html (arquivo único, autocontido) a partir de template.html.
Uso: python3 build.py [rows.json]   (rows.json = snapshot offline; opcional)"""
import base64, json, sys, datetime, pathlib
root = pathlib.Path(__file__).parent
b64 = lambda p: base64.b64encode((root/'assets'/p).read_bytes()).decode()
rows = json.loads(pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else root/'snapshot.json').read_text())
if rows and 'e' in rows[0]:  # formato compacto -> formato da API
    rows = [dict(portao=r['portao'], elegivel_2026=r['e'], area=r['area'], p0=r['p0'], p1=r['p1'], p2=r['p2'], bu=r['bu'], projeto=r['projeto'],
                 tamanho=r['tamanho'], inicio=r['inicio'], fim_planejado=r['fim'], data_entrega=r['entrega'], impacto_anual=r['ia'],
                 impacto_2026=r['i26'], impacto_2027=r['i27'], capex=r['capex']) for r in rows]
metas = [("Masterplan","Willian",40e6,20e6,10e6),("Engenharia","Matheus Machion",14e6,7e6,3.5e6),("Materiais","Rafaela Mauli",16e6,8e6,4e6),
         ("Manut/CDM","Alexandre Zanao",18e6,9e6,4.5e6),("Transf. Digital","Bruno Okazaki",10e6,5e6,2.5e6)]
snap = dict(at=datetime.date.today().strftime('%d/%m/%Y'), projetos=rows,
            metas=[dict(escopo=a,responsavel=b,meta_p0=c,meta_p1=d,meta_p2=e) for a,b,c,d,e in metas])
html = (root/'template.html').read_text()
for k, v in {'__F400__': b64('2c8444021a6f937c66e0001d4cb122de.woff2'), '__F500__': b64('ec93e75d3384a849c03256fa05728b3e.woff2'),
             '__F700__': b64('cfe4adce3660808df3301758e246bb80.woff2'), '__X800__': b64('79176845666fa620a2efcbb89f51b393.woff2'),
             '__LOGO__': b64('207ba4ab544152cf2601acc40f267108.png'),
             '__SBURL__': 'https://kaymumapadfrrixooiiv.supabase.co',
             '__SBKEY__': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtheW11bWFwYWRmcnJpeG9vaWl2Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTMxNzA3MjEsImV4cCI6MjEwODc0NjcyMX0.ARhZin7JQ5y1rMHe-ieNWQxP0Mh9bXcG_iR7UCuSaok',
             '__SNAP__': json.dumps(snap, ensure_ascii=False, separators=(',', ':'))}.items():
    html = html.replace(k, v)
(root/'dashboard-projetos-tigre.html').write_text(html)
print('ok', len(html)//1024, 'KB')
