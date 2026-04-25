import os, glob, re

MARKER = 'class="kk-cta"'
SKIP = {'index.html','index_backup.html','news.html','sitemap.xml','yandex_e1453ee8dd6aa370.html'}

CTA_DE = '<div class="kk-cta" style="background:linear-gradient(135deg,#1a2a4a,#0d1b35);border-left:4px solid #e8690a;border-radius:8px;padding:28px 32px;margin:48px auto 32px;max-width:760px;font-family:sans-serif;color:#fff;box-shadow:0 4px 24px rgba(0,0,0,.3)"><p style="margin:0 0 6px;font-size:13px;color:#e8690a;letter-spacing:1px;text-transform:uppercase">Haben Sie ein ähnliches Problem?</p><h3 style="margin:0 0 12px;font-size:22px;font-weight:700">Ihor Kryazhev — Technologie-Berater für Sekundärpolymer-Recycling</h3><p style="margin:0 0 20px;font-size:15px;color:#c8d8f0;line-height:1.6">25+ Jahre Erfahrung · LDPE, LLDPE, HDPE, PP · Online und vor Ort · Antwort in 24h</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a href="https://wa.me/4915258400610" style="background:#25d366;color:#fff;padding:11px 22px;border-radius:6px;text-decoration:none;font-weight:600;font-size:14px">&#128172; WhatsApp</a><a href="https://igoruspehov.github.io/polymer-consult/" style="background:#e8690a;color:#fff;padding:11px 22px;border-radius:6px;text-decoration:none;font-weight:600;font-size:14px">→ Zur Beratungsseite</a></div></div>'

CTA_EN = '<div class="kk-cta" style="background:linear-gradient(135deg,#1a2a4a,#0d1b35);border-left:4px solid #e8690a;border-radius:8px;padding:28px 32px;margin:48px auto 32px;max-width:760px;font-family:sans-serif;color:#fff;box-shadow:0 4px 24px rgba(0,0,0,.3)"><p style="margin:0 0 6px;font-size:13px;color:#e8690a;letter-spacing:1px;text-transform:uppercase">Facing a similar issue?</p><h3 style="margin:0 0 12px;font-size:22px;font-weight:700">Ihor Kryazhev — Polymer Recycling Consultant</h3><p style="margin:0 0 20px;font-size:15px;color:#c8d8f0;line-height:1.6">25+ years with extrusion equipment · LDPE, LLDPE, HDPE, PP · Remote & on-site · 24h response</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a href="https://wa.me/4915258400610" style="background:#25d366;color:#fff;padding:11px 22px;border-radius:6px;text-decoration:none;font-weight:600;font-size:14px">&#128172; WhatsApp</a><a href="https://igoruspehov.github.io/polymer-consult/" style="background:#e8690a;color:#fff;padding:11px 22px;border-radius:6px;text-decoration:none;font-weight:600;font-size:14px">→ Consulting page</a></div></div>'

CTA_RU = '<div class="kk-cta" style="background:linear-gradient(135deg,#1a2a4a,#0d1b35);border-left:4px solid #e8690a;border-radius:8px;padding:28px 32px;margin:48px auto 32px;max-width:760px;font-family:sans-serif;color:#fff;box-shadow:0 4px 24px rgba(0,0,0,.3)"><p style="margin:0 0 6px;font-size:13px;color:#e8690a;letter-spacing:1px;text-transform:uppercase">Похожая ситуация?</p><h3 style="margin:0 0 12px;font-size:22px;font-weight:700">Игорь Кряжев — консультант по переработке полимеров</h3><p style="margin:0 0 20px;font-size:15px;color:#c8d8f0;line-height:1.6">25+ лет с экструзионным оборудованием · LDPE, LLDPE, HDPE, PP · Онлайн и выезд · Ответ 24ч</p><div style="display:flex;gap:12px;flex-wrap:wrap"><a href="https://wa.me/4915258400610" style="background:#25d366;color:#fff;padding:11px 22px;border-radius:6px;text-decoration:none;font-weight:600;font-size:14px">&#128172; WhatsApp</a><a href="https://igoruspehov.github.io/polymer-consult/" style="background:#e8690a;color:#fff;padding:11px 22px;border-radius:6px;text-decoration:none;font-weight:600;font-size:14px">→ Страница консультанта</a></div></div>'

def lang(name, content):
    n = name.lower()
    if n.endswith('-de.html'): return 'de'
    if n.endswith('-en.html'): return 'en'
    if n.endswith('-ru.html'): return 'ru'
    if sum(1 for c in content if '\u0400'<=c<='\u04ff') > 100: return 'ru'
    return 'de'

modified = 0
for f in sorted(glob.glob('*.html')):
    if f in SKIP: continue
    txt = open(f, encoding='utf-8', errors='ignore').read()
    if MARKER in txt or '</body>' not in txt.lower(): continue
    l = lang(f, txt)
    cta = CTA_DE if l=='de' else CTA_EN if l=='en' else CTA_RU
    txt = re.sub(r'(</body>)', cta+r'\1', txt, count=1, flags=re.IGNORECASE)
    open(f,'w',encoding='utf-8').write(txt)
    print(f"OK [{l}] {f}")
    modified += 1

print(f"\nИзменено: {modified} файлов")
