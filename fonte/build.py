# Monta o site do Glossário de Marketing num HTML único (vídeos embutidos).
# Uso: python3 build.py  -> gera index.html nesta pasta
import base64, os
D=os.path.dirname(os.path.abspath(__file__))
src=open(f'{D}/site.src.html').read(); t=open(f'{D}/termos.js').read()
h=src.replace('__LOGO_CAFE__',open(f'{D}/logo_cafe.b64').read().strip()).replace('__LOGO_LEITE__',open(f'{D}/logo_leite.b64').read().strip()).replace('__TERMOS__',t)
for f in sorted(os.listdir(f'{D}/videos')):
    n,ext=os.path.splitext(f); mime='video/mp4' if ext=='.mp4' else 'image/jpeg'
    h=h.replace(f'"videos/{f}"',f'"data:{mime};base64,'+base64.b64encode(open(f'{D}/videos/{f}','rb').read()).decode()+'"')
title='<title>Glossário de Marketing</title>\n'; h=h.replace(title,'',1)
h='<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n'+title+'<meta name="description" content="Os termos e as siglas do marketing explicados de um jeito simples, por Camila Pavani. Conceito, exemplo e como aplicar.">\n</head>\n<body>\n'+h+'\n</body>\n</html>\n'
open(os.path.join(D,'..','site','index.html'),'w').write(h); print('ok')
