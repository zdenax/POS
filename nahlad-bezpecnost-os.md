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

## Common Criteria (ISO 15408)

Nástupce Orange Book -- mezinárodní standard.

- **EAL** (Evaluation Assurance Level) -- úrovně 1–7
- Umožňuje srovnávat produkty od různých výrobců
- Certifikace prováděna nezávislými laboratořemi

---

## Doplnit z hodiny

> Doplnit po přednášce.
