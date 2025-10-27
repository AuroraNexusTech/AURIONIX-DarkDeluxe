#!/usr/bin/env python3
import os, hashlib, zipfile
from pathlib import Path

APP   = "AURIONIX_DarkDeluxe"
BRAND = "AURIONIX DarkDeluxe"
CLAIM = "Transform. Evolve. Conquer."
ENC   = "utf-8"

# PayPal/Preis (per ENV überschreibbar)
PAYPAL_ME = os.environ.get("PAYPAL_ME", "https://www.paypal.me/Keffo").rstrip("/")
PRICE     = os.environ.get("PRICE", "59").strip()
PP_LINK   = f"{PAYPAL_ME}/{PRICE}" if PRICE else PAYPAL_ME

root = Path(APP)

def w(p: Path, s: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s.strip() + "\n", encoding=ENC)

def page(lang="de"):
    if lang == "de":
        fname, langattr = "index.html", "de"
        cta  = f"Jetzt für {PRICE}€ sichern" if PRICE else "Jetzt sichern"
        lead = "Das ultimative Dark Luxury Life Upgrade System — sofort downloadbar."
        pay  = "Sofortiger Download nach Zahlung. Sicher via PayPal."
        dl   = "Direktdownload"
    else:
        fname, langattr = "en.html", "en"
        cta  = f"Get Instant Access — {PRICE}" if PRICE else "Get Instant Access"
        lead = "The ultimate Dark Luxury Life Upgrade System — instant download."
        pay  = "Instant download after payment. Secure via PayPal."
        dl   = "Direct Download"
    html = f"""<!doctype html>
<html lang="{langattr}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{BRAND} — {CLAIM}</title>
<style>
body{{background:#000;color:#ddd;font-family:Montserrat,Arial,sans-serif;margin:0}}
.wrap{{max-width:1080px;margin:0 auto;padding:40px 20px}}
.hero{{text-align:center;padding:40px 0}}
h1{{color:#C9A54B;font-family:Orbitron,Arial,sans-serif;font-weight:900;margin:0 0 6px;font-size:38px;letter-spacing:.5px}}
.sub{{color:#eee;opacity:.95;margin:0 0 18px;font-size:18px}}
.box{{background:linear-gradient(180deg,#0b0b0b 0,#121212 100%);border:1px solid #1b1b1b;border-radius:16px;padding:28px;box-shadow:0 0 40px #000 inset,0 0 40px rgba(201,165,75,.12)}}
.cta{{background:#C9A54B;color:#000;text-decoration:none;padding:14px 26px;border-radius:10px;font-weight:800;display:inline-block;margin:10px 0}}
.grid{{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));margin-top:16px}}
.card{{background:#0c0c0c;border:1px solid #1a1a1a;border-radius:12px;padding:12px}}
footer{{text-align:center;color:#777;padding:30px 0}}
.badge{{display:inline-block;margin-top:6px;color:#C9A54B;font-weight:700;letter-spacing:.6px}}
.dl{{margin-top:14px}}
</style></head>
<body><div class="wrap">
  <div class="hero box">
    <h1>{BRAND}</h1>
    <div class="badge">{CLAIM}</div>
    <p class="sub">{lead}</p>
    <a class="cta" href="{PP_LINK}" rel="nofollow noopener">{cta}</a>
    <div class="grid">
      <div class="card"><b>Influence Ascension</b><br>200 Social Templates + Captions</div>
      <div class="card"><b>Aegis Shield Protocol</b><br>Security & Recovery</div>
      <div class="card"><b>Wealth Override</b><br>30 Income Systems</div>
      <div class="card"><b>PulseForge Audio Lab</b><br>50 DarkTech Samples (spec)</div>
      <div class="card"><b>Prime Physique Ritual</b><br>10-Day Body Plan</div>
    </div>
    <p class="dl"><a class="cta" href="./AURIONIX_DarkDeluxe.zip">{dl}</a></p>
    <p style="margin-top:8px;color:#cfcfcf">{pay}</p>
  </div>
</div><footer>© {BRAND}</footer></body></html>"""
    return fname, html

# Inhalte (kompakt – erweiterbar)
README_DE = f"""{BRAND}
{CLAIM}

Verwendung
1) ZIP entpacken
2) Module öffnen (DE/EN)
3) Salespage (HTML) hochladen
Zahlung: {PAYPAL_ME}{'/' + PRICE if PRICE else ''}
Support: Instagram @MrViperkilla100
"""
README_EN = f"""{BRAND}
{CLAIM}

Use
1) Unzip
2) Open modules (EN/DE)
3) Upload sales page (HTML)
Payment: {PAYPAL_ME}{'/' + PRICE if PRICE else ''}
Support: Instagram @MrViperkilla100
"""
LICENSE_DE = "Privatnutzung. Keine Weitergabe. Kein Re-Upload.\nAudio: Nutzung in eigenen Werken erlaubt, kein Weiterverkauf.\n© AURIONIX DarkDeluxe\n"
LICENSE_EN = "Personal use only. No redistribution.\nAudio: allowed in your works, resale prohibited.\n© AURIONIX DarkDeluxe\n"

IA_DE = "INFLUENCE ASCENSION — DE\n30-Tage Social Growth System…\n"
IA_EN = "INFLUENCE ASCENSION — EN\n30-Day Social Growth System…\n"
CAPTIONS_DE = "\n".join(["Elite wird gemacht — nicht geboren. #DarkDeluxe"]+[f"DarkDeluxe #{i:02d} — Fokus. Wert. Momentum." for i in range(2,121)])
CAPTIONS_EN = "\n".join(["Elite is made — not born. #DarkDeluxe"]+[f"DarkDeluxe #{i:02d} — Focus. Value. Momentum." for i in range(2,121)])
AEGIS_DE = "AEGIS SHIELD PROTOCOL — DE\nCheckliste: Berechtigungen, 2FA, Sperrbildschirm, Phishing, Backup, Verlust.\n"
AEGIS_EN = "AEGIS SHIELD PROTOCOL — EN\nChecklist: permissions, 2FA, lock screen, anti-phishing, backup, lost.\n"
WEALTH_DE = "WEALTH OVERRIDE — DE\n30 Online-Einnahmequellen + Starter.\n"
WEALTH_EN = "WEALTH OVERRIDE — EN\n30 online revenue streams + starters.\n"
PULSEFORGE_README = "PULSEFORGE AUDIO LAB\n50 DarkTechno Samples (Spec & Struktur). Lizenz: Nutzung erlaubt; kein Weiterverkauf.\n"
SAMPLE_LIST = "Kicks: 01–14\nSnares/Claps: 15–22\nFX: 23–40\nStabs: 41–50\n"
PHYSIQUE_DE = "PRIME PHYSIQUE RITUAL — DE\n10-Tage Body-Upgrade.\n"
PHYSIQUE_EN = "PRIME PHYSIQUE RITUAL — EN\n10-Day Body Upgrade.\n"
BADGE_DESC = "DARKCORE MEMBER BADGE — Rund, Black × Gold, High-Glow.\n"
LAUNCH_DE = "\n".join([f"Tag {i}: Aktion/Asset — CTA" for i in range(1,31)])
LAUNCH_EN = "\n".join([f"Day {i}: Action/Asset — CTA" for i in range(1,31)])

def write_bundle():
    # Root
    w(root/"README_DE.txt", README_DE)
    w(root/"README_EN.txt", README_EN)
    w(root/"LICENSE_DE.txt", LICENSE_DE)
    w(root/"LICENSE_EN.txt", LICENSE_EN)
    # Module
    w(root/"Influence_Ascension/DE/Influence_Ascension_DE.pdf.txt", IA_DE)
    w(root/"Influence_Ascension/DE/Captions_DE.txt", CAPTIONS_DE)
    w(root/"Influence_Ascension/EN/Influence_Ascension_EN.pdf.txt", IA_EN)
    w(root/"Influence_Ascension/EN/Captions_EN.txt", CAPTIONS_EN)
    w(root/"Aegis_Shield_Protocol/DE/Aegis_Protocol_DE.pdf.txt", AEGIS_DE)
    w(root/"Aegis_Shield_Protocol/EN/Aegis_Protocol_EN.pdf.txt", AEGIS_EN)
    w(root/"Wealth_Override/DE/Wealth_Override_DE.pdf.txt", WEALTH_DE)
    w(root/"Wealth_Override/EN/Wealth_Override_EN.pdf.txt", WEALTH_EN)
    w(root/"PulseForge_Audio_Lab/PulseForge_README.txt", PULSEFORGE_README)
    w(root/"PulseForge_Audio_Lab/Sample_List.txt", SAMPLE_LIST)
    w(root/"Prime_Physique_Ritual/DE/Prime_Physique_DE.pdf.txt", PHYSIQUE_DE)
    w(root/"Prime_Physique_Ritual/EN/Prime_Physique_EN.pdf.txt", PHYSIQUE_EN)
    w(root/"Bonus/DarkCore_Badge_Description.txt", BADGE_DESC)
    w(root/"Bonus/Social_Launch_30Day_DE.txt", LAUNCH_DE)
    w(root/"Bonus/Social_Launch_30Day_EN.txt", LAUNCH_EN)

def zip_tree(src: Path, out_zip: Path):
    with zipfile.ZipFile(out_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in src.rglob("*"):
            z.write(p, p.relative_to(src.parent))

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1<<20), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    # Clean
    if root.exists():
        for p in sorted(root.rglob("*"), reverse=True):
            if p.is_file(): p.unlink()
        for p in sorted(root.rglob("*"), reverse=True):
            if p.is_dir():
                try: p.rmdir()
                except OSError: pass
        try: root.rmdir()
        except OSError: pass

    # Write bundle
    write_bundle()

    # Build Pages site (site/)
    site = Path("site"); site.mkdir(exist_ok=True)
    for fname, content in (page("de"), page("en")):
        w(site/fname, content)

    # Build ZIP and copy to site/
    out_zip = Path("AURIONIX_DarkDeluxe.zip")
    if out_zip.exists(): out_zip.unlink()
    zip_tree(root, out_zip)
    (site/"AURIONIX_DarkDeluxe.zip").write_bytes(out_zip.read_bytes())
    digest = sha256(out_zip)
    (Path("AURIONIX_DarkDeluxe.zip.sha256")).write_text(f"{digest}  {out_zip.name}\n", encoding="ascii")
    (site/"AURIONIX_DarkDeluxe.zip.sha256").write_text(f"{digest}  {out_zip.name}\n", encoding="ascii")

    print("[✓] Built:", out_zip, "— SHA256:", digest)
    print("[i] Pages prepared in ./site (index.html, en.html, ZIP). PayPal:", PP_LINK)

if __name__ == "__main__":
    main()
