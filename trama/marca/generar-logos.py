# Genera la geometría de la marca TRAMA (isotipo, logotipo, firmas, sello)
import os
def iso_paths():
    # placa de llana con dentado fino (12 dientes) + mango con punta redondeada
    x0, x1, top, h, n, dep = 14, 86, 18, 15, 12, 3.6
    pitch = (x1-x0)/n; pts = [(x0,top+h),(x0,top)]
    for k in range(n):
        a = x0 + k*pitch
        pts += [(a+pitch*.25,top),(a+pitch*.25,top+dep),(a+pitch*.75,top+dep),(a+pitch*.75,top)]
    pts += [(x1,top),(x1,top+h),(57,top+h)]
    d = "M" + " L".join(f"{x:.2f},{y:.2f}" for x,y in pts) + " L57,79 A7,7 0 0 1 43,79 L43,33 Z"
    return f'<path d="{d}"/>'
def wm_paths():
    # letras monolínea, trazo 9 sobre altura 100; la T repite el dentado
    T = "M0,0 H72 V9 H40.5 V100 H31.5 V9 H0 Z"
    strokes = []
    R = 106
    strokes.append(f"M{R+4.5},0 V100 M{R+4.5},4.5 H{R+38} A25,25 0 0 1 {R+38},54.5 H{R+4.5} M{R+36},54.5 L{R+66},100")
    for A in (206, 434):
        strokes.append(f"M{A},100 L{A+32},4.5 H{A+40} L{A+72},100 M{A+11.5},68 H{A+60.5}")
    Mx = 312
    strokes.append(f"M{Mx+4.5},100 V4.5 L{Mx+44},74 L{Mx+83.5},4.5 V100")
    return (f'<path d="{T}" stroke="none"/>'
            f'<path d="{" ".join(strokes)}" fill="none" stroke="currentColor" stroke-width="9" stroke-linejoin="miter" stroke-miterlimit="2.2"/>')
ISO = iso_paths(); WM = wm_paths()
symbols = f'''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<defs>
<clipPath id="wmclip"><rect x="-2" width="514" height="100"/></clipPath>
<path id="selloCirc" d="M50,50 m-38,0 a38,38 0 1,1 76,0 a38,38 0 1,1 -76,0"/>
</defs>
<symbol id="iso" viewBox="0 0 100 100"><g fill="currentColor">{ISO}</g></symbol>
<symbol id="wm" viewBox="0 0 512 100"><g fill="currentColor" clip-path="url(#wmclip)">{WM}</g></symbol>
<symbol id="firmaH" viewBox="0 0 330 100"><use href="#iso" width="100" height="100"/><use href="#wm" x="138" y="32" width="192" height="38"/></symbol>
<symbol id="firmaV" viewBox="0 0 260 200"><use href="#iso" x="80" y="0" width="100" height="100"/><use href="#wm" x="15" y="128" width="230" height="45.5"/><text x="130" y="196" text-anchor="middle" font-family="Hanken Grotesk, Helvetica, Arial, sans-serif" font-weight="500" font-size="10.5" letter-spacing="3.2" fill="currentColor">HERRAMIENTAS DE TERMINACIÓN</text></symbol>
<symbol id="sello" viewBox="0 0 100 100"><circle cx="50" cy="50" r="47" fill="none" stroke="currentColor" stroke-width="1.1"/><circle cx="50" cy="50" r="29" fill="none" stroke="currentColor" stroke-width=".6"/><text font-family="Hanken Grotesk, Helvetica, Arial, sans-serif" font-weight="500" font-size="6.4" letter-spacing="2.15" fill="currentColor"><textPath href="#selloCirc" textLength="235" lengthAdjust="spacing">TRAMA · HERRAMIENTAS DE TERMINACIÓN ·</textPath></text><use href="#iso" x="32" y="32" width="36" height="36"/></symbol>
</svg>'''
out = os.environ.get('OUT', '.')
open(os.path.join(out,'symbols.svg.html'),'w').write(symbols)
def standalone(name, vb, inner, color, bg=None, defs=''):
    b = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"><title>TRAMA</title>{defs}{b}<g fill="{color}" color="{color}">{inner}</g></svg>\n'
M = os.environ.get('MARCA', '.')
G, Y, BR = '#191A1B', '#EDECE8', '#8C6A44'
clip = '<defs><clipPath id="c"><rect x="-2" width="514" height="100"/></clipPath></defs>'
wmg = f'<g clip-path="url(#c)">{WM}</g>'
files = {
 'isotipo-grafito.svg': standalone('', '0 0 100 100', ISO, G),
 'isotipo-yeso-sobre-grafito.svg': standalone('', '0 0 100 100', ISO, Y, G),
 'logotipo-grafito.svg': standalone('', '0 0 512 100', wmg, G, defs=clip),
 'firma-horizontal-grafito.svg': standalone('', '0 0 330 100', ISO + f'<g transform="translate(138 32) scale({192/512})">{wmg}</g>', G, defs=clip),
 'firma-horizontal-yeso.svg': standalone('', '0 0 330 100', ISO + f'<g transform="translate(138 32) scale({192/512})">{wmg}</g>', Y, G, defs=clip),
 'firma-vertical-grafito.svg': standalone('', '0 0 260 200', f'<g transform="translate(80 0)">{ISO}</g><g transform="translate(15 128) scale({230/512})">{wmg}</g><text x="130" y="196" text-anchor="middle" font-family="Hanken Grotesk, Helvetica, Arial, sans-serif" font-weight="500" font-size="10.5" letter-spacing="3.2">HERRAMIENTAS DE TERMINACIÓN</text>', G, defs=clip),
}
for k,v in files.items(): open(os.path.join(M,k),'w').write(v)
print('ok', len(symbols))
