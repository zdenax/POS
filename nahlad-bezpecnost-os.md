# KI/POS – Náhled do příště
**Téma:** Bezpečnost v rámci OS
**Datum příští hodiny:** 28. 4. 2026

---

## Co nás čeká

- Bezpečnost operačního systému
- Evaluace bezpečnosti systémů
- Orange Book (TCSEC)
- Možná: Bell-LaPadula model, Common Criteria

---

## Orange Book – TCSEC

**Trusted Computer System Evaluation Criteria** (1983, DoD USA)

Definuje úrovně důvěryhodnosti systémů:

| Třída | Název              | Popis                                                    |
|-------|--------------------|----------------------------------------------------------|
| D     | Minimal Protection | nesplňuje žádné požadavky                                |
| C1    | Discretionary      | základní oddělení uživatelů a dat                        |
| C2    | Controlled Access  | auditování, přesnější řízení přístupu (např. Unix, Win)  |
| B1    | Labeled Security   | povinné řízení přístupu (MAC), bezpečnostní štítky       |
| B2    | Structured         | formální bezpečnostní model, důvěryhodná komunikace      |
| B3    | Security Domains   | referencní monitor, minimální TCB                        |
| A1    | Verified Design    | formálně ověřený návrh TCB                               |

**TCB** = Trusted Computing Base -- část systému, která musí být správná, aby byl celý systém bezpečný (kernel, autentizace, ...).

---

## Bell-LaPadula model

Model pro **důvěrnost** (confidentiality) dat:

- **no read up** -- subjekt nesmí číst objekt s vyšší klasifikací
- **no write down** -- subjekt nesmí zapsat do objektu s nižší klasifikací

Používá se ve vojenských systémech (tajné, přísně tajné, ...).

---

## Common Criteria (CC) – ISO/IEC 15408

Nástupce Orange Book -- mezinárodní standard pro evaluaci bezpečnosti IT produktů.

- Umožňuje srovnávat produkty od různých výrobců
- Certifikace prováděna nezávislými laboratořemi (akreditované testovací centrum)
- Výsledek: certifikát uznaný ve více zemích (vzájemné uznávání přes CCRA dohodu)

### Klíčové pojmy CC

- **TOE** (Target of Evaluation) -- produkt nebo systém, který se hodnotí
- **ST** (Security Target) -- dokument popisující bezpečnostní vlastnosti TOE
- **PP** (Protection Profile) -- šablona požadavků pro danou kategorii produktů (např. firewall, OS)
- **SFR** (Security Functional Requirements) -- co systém musí dělat (funkce)
- **SAR** (Security Assurance Requirements) -- jak moc věříme, že to dělá správně (záruky)

### EAL – Evaluation Assurance Levels

| EAL | Název                        | Popis                                                      | Příklad              |
|-----|------------------------------|------------------------------------------------------------|----------------------|
| 1   | Functionally Tested          | základní testování funkčnosti                              | běžné komerční produkty |
| 2   | Structurally Tested          | + analýza návrhu, testování vývojářem                     |                      |
| 3   | Methodically Tested          | + vývojový proces, code review                            | mnoho OS, firewallů  |
| 4   | Methodically Designed        | + formální návrh, nezávislé testování                     | Windows, RHEL, iOS   |
| 5   | Semiformally Designed        | + semiformální modely, penetrační testy                   | čipové karty         |
| 6   | Semiformally Verified        | + strukturovaný vývoj, hloubková analýza                  | vojenské systémy     |
| 7   | Formally Verified            | formálně ověřený návrh i implementace                     | velmi vzácné         |

> Většina komerčních produktů cílí na **EAL 4** -- dobrý kompromis mezi zárukami a náklady na certifikaci.

---

## Doplnit z hodiny

> Doplnit po přednášce.
