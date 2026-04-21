# Kryptografie – Náhled (pohled přednášejícího)

> Důraz není na to, jak algoritmy fungují uvnitř, ale na **bezpečnostní problémy, použití v praxi a moderní výzvy**.

---

## Obsah

1. Certifikáty a certifikační autority
2. Integrita a důvěryhodnost – digitální podpis
3. Hashe – k čemu slouží
4. Charakteristika moderních algoritmů
5. Symetrická vs. asymetrická kryptografie
6. RSA vs. eliptické křivky
7. Post-kvantová kryptografie

---

## Certifikáty a certifikační autority (CA)

### Co je certifikát

- Digitální dokument, který váže **veřejný klíč** na **identitu** (osoba, server, organizace)
- Podepsán certifikační autoritou → důvěryhodnost přenesena z CA na držitele
- Formát: **X.509**
- Obsah: veřejný klíč, jméno subjektu, jméno CA, platnost (od–do), sériové číslo, podpis CA

### Certifikační autorita (CA)

- Třetí strana, které všichni důvěřují
- **Hierarchie CA**: Root CA → Intermediate CA → koncový certifikát
- Root CA jsou předinstalované v OS / prohlížeči (trust store)
- Pokud CA kompromitována → celý řetězec nedůvěryhodný

### Životnost certifikátů

- Certifikáty mají **omezenou platnost** (dnes typicky 90 dní – Let's Encrypt, nebo 1–2 roky)
- Po vypršení je nutná obnova
- Odvolání před expirací: **CRL** (Certificate Revocation List) nebo **OCSP**
- Kratší životnost = menší okno pro zneužití kompromitovaného certifikátu

---

## Integrita a důvěryhodnost – digitální podpis

Jak udržet integritu a důvěryhodnost podepsaného dokumentu:

1. Vypočítá se **hash** dokumentu
2. Hash se zašifruje **soukromým klíčem** podepisujícího → digitální podpis
3. Příjemce dešifruje podpis **veřejným klíčem** → získá hash
4. Nezávisle vypočítá hash dokumentu → porovná

```
dokument → hash() → H
H + soukromý klíč → podpis

příjemce:
podpis + veřejný klíč → H'
dokument → hash() → H
H == H' ? OK : CHYBA
```

- Garantuje **integritu** (dokument nebyl změněn) i **autenticitu** (podepsal držitel soukromého klíče)
- Nezajišťuje důvěrnost (dokument není šifrován)

---

## Hashe

### Co je hash

- Jednosměrná funkce: libovolně dlouhý vstup → **pevná délka výstupu**
- Není možné (prakticky) zpětně získat vstup
- Malá změna vstupu → zcela jiný výstup (avalanche effect)

### Vlastnosti kryptografického hashe

- **Jednosměrnost** – z výstupu nelze rekonstruovat vstup
- **Odolnost vůči kolizím** – těžké najít dva různé vstupy se stejným hashem
- **Odolnost vůči druhé vzorce** – těžké najít jiný vstup se stejným hashem jako daný vstup

### Použití

- Digitální podpisy
- Ukládání hesel (bcrypt, Argon2 – ne čistý SHA!)
- Kontrolní součty souborů
- Hashovací řetězce (blockchain, Merkle tree)
- HMAC – autentizace zpráv

### Aktuální standardy

| Algoritmus | Délka výstupu | Stav         |
|------------|---------------|--------------|
| MD5        | 128 bit       | **broken**   |
| SHA-1      | 160 bit       | **deprecated**|
| SHA-256    | 256 bit       | bezpečný     |
| SHA-3      | variabilní    | bezpečný     |

---

## Symetrická vs. asymetrická kryptografie

### Symetrická

- Jeden klíč pro šifrování i dešifrování
- Rychlá (AES, ChaCha20)
- Vhodná pro šifrování dat
- **Největší problém: distribuce klíče** -- jak bezpečně dostat klíč k protistraně, aniž by ho někdo odposlouchal? Pokud máme bezpečný kanál pro přenos klíče, proč ho nepoužít rovnou pro data?

### Asymetrická

- Dvojice klíčů: veřejný (šifrování) + soukromý (dešifrování)
- Řeší problém distribuce klíče -- veřejný klíč lze sdílet volně
- Pomalá – nehodí se pro šifrování velkých dat
- Vhodná pro **výměnu klíčů** a **digitální podpisy**
- **Základní problém: podvržení veřejného klíče (MitM)**
  - Útočník se postaví mezi dva komunikující, každému podstrčí svůj veřejný klíč
  - Každá strana si myslí, že komunikuje s tou druhou, ale šifruje pro útočníka
  - Řešení: **certifikáty** -- veřejný klíč podepsán důvěryhodnou třetí stranou (CA), která potvrzuje identitu
  - Bez CA (nebo jiného mechanismu důvěry) asymetrická kryptografie MitM neřeší

### V praxi: hybridní přístup

```
asymetrická kryptografie → bezpečně přenese symetrický klíč
symetrický klíč → šifruje samotná data
```

Příklad: TLS (HTTPS)

---

## RSA vs. eliptické křivky (ECC)

### RSA

- Bezpečnost: faktorizace velkých čísel
- Doporučená velikost klíče: **minimálně 2048 bit**, ideálně 3072–4096 bit
- Větší klíče → exponenciálně náročnější výpočty

### Eliptické křivky (ECC)

- Bezpečnost: problém diskrétního logaritmu na eliptické křivce
- **Kratší klíče, stejná bezpečnost**:

| Bezpečnost | RSA        | ECC     |
|------------|------------|---------|
| 80 bit     | 1024 bit   | 160 bit |
| 128 bit    | 3072 bit   | 256 bit |
| 256 bit    | 15360 bit  | 512 bit |

- ECC preferováno pro mobilní zařízení, IoT, TLS
- Standardy: P-256, P-384 (NIST), Curve25519

---

## Post-kvantová kryptografie

### Problém

Kvantové počítače (Shorův algoritmus) dokáží:
- Faktorizovat velká čísla → **RSA broken**
- Řešit diskrétní logaritmus → **ECC broken**
- Symetrická kryptografie: Groverův algoritmus zdvojnásobí efektivní délku klíče (AES-256 → ekvivalent 128 bit bezpečnosti)

### Řešení – post-kvantové algoritmy

NIST standardizoval (2024):
- **CRYSTALS-Kyber** → výměna klíčů (KEM)
- **CRYSTALS-Dilithium** → digitální podpisy
- **FALCON** → digitální podpisy
- **SPHINCS+** → digitální podpisy (hash-based)

### Migrace

- Stávající certifikáty a podpisy jsou **ohroženy** do budoucna (harvest now, decrypt later)
- Nutná migrace infrastruktury – CA, PKI, protokoly
- Hybridní přístup: klasický + post-kvantový algoritmus zároveň

---

## Doplnit z hodiny

> Doplnit po přednášce.
