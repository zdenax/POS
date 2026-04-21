# KI/POS – Shrnutí
**Datum:** 16. 5. 2025  
**Týden:** 13.

---

## Klíčové pojmy

- **Kernel** = privilegovaný režim / instrukce (nastavení tabulky stránek, přístup k paměti, HALT)
- **Realokační problém** – `.so` / `.dll`, position independent code
- **Bázový registr** < instruction pointer
- **User-space** = přístup k CPU, neprivilegované instrukce, US paměť
- **Hypervisor** = virtualizace prostředků
- **Scheduler** = plánovač (zjišťuje PID nového procesu)
  - statická priorita (nice) … −40 … 100
  - dynamická priorita: zvýhodňuje dlouho čekající
  - real-time priorita: nedají se předbíhat, kooperace
- **Komunikace** = stream, queue
- **Pipe (roura)** = vyrovnávací buffer mezi procesy
- `$`: `ulimit -a`
- `#`: FIFO, Eurocity, futex

---

## Souborový systém (FS)

### Řez souborovým systémem (vrstvový model)

Diagram ukazuje cestu od otevřeného souboru až po fyzické HW zařízení -- každá vrstva abstrahuje tu pod ní.

```
[otevřený soubor]   [mount]
         ↓
     [adresáře]          ← překlad jméno → i-číslo
         ↓
      [i-uzel]           ← metadata souboru (oprávnění, velikost, ukazatele na bloky)
         ↓
      [buffer]           ← vyrovnávací paměť bloků v RAM (cache)
         ↓
[ovladač]  [logický svazek]   ← ovladač zařízení; svazek = logická jednotka (volume)
         ↓
  [obraz/image] (oddíl)  ← konkrétní oddíl na fyzickém médiu
         ↓
[HW]   [vnější paměť]   ← fyzické zařízení (disk, SSD, ...)
```

### Řez formátem souboru (logický)

Ukazuje jak je soubor vnitřně strukturován na disku -- dvě dimenze: boot/hlavička/metadata vs. samotná data.

```
┌─────────┐     ┌──────────┐
│  boot   │     │   data   │
├─────────┤     ├──────────┤
│ header  │     │ metadata │
├─────────┤     └──────────┘
│  meta   │
│  data   │
└─────────┘
```

- **boot** – zaváděcí blok (přítomen pouze u bootovatelných oddílů)
- **header** – hlavička souborového systému (typ, velikost, parametry)
- **metadata** – informace o souborech (i-uzly, adresářové záznamy)
- **data** – samotná uživatelská data souborů



# (nejde mi opt key) 21-04-2026

namei (cela cesta k sobouru) treba /boot/efi/EFI/ubuntu/grub.cfg

zacne a zacne oteviraat postupně ... a omylem v tom efi se podiva do jineho souboroveho systému .. 





# JAK TO VYPADÁ KDYŽ OTEVŘEME SOUBOR
-----------------------------------------

fd <- open ("/bin/ls")


1) zavolá si namei
2) podiva se do souboroveho systemu a hleda 

	
   
 	------
	|blok|	 i uzly 
	------

	on si ty i uzly "kešuje"

	vznikne dynamický uzel -> obsahuje kopii fyzického & ještě k tomu to druhý...

	150 -> fyzický uzel 


# SYSTÉMOVÁ TABULKA SYSTÉMOVÝCH SOUBORŮ –> SYSFILETABLE -> je to v kernelu btw

2 částí -> odkaz na dyn. uzel a file pointer (na začátku 0 "na read a write .. ale na append muze byt an konci")

a kazda sluzaba ma: TASK FILETABLE a obsahuje odkaz na tu systemovou tabulku souborů 

file table ja tabulka a má indexy -- treba 0 1 2 a to co nam vrati byla zrovna ta 3jak třeba

**DOPLNIT OBRÁZEK Z TABULE PAK**
------------------------------------
# Tabulky otevřených souborů (Unix/Linux)

---

## SysFileTable

- je v **kernelu**
- každý záznam má 2 části:
  - **odkaz na dynamický i-uzel**
  - **file pointer** -- na začátku = 0; při read/write se posouvá, při `append` začíná na konci

---

## Task File Table (per-proces)

- každý proces má vlastní
- je to tabulka s **indexy = file descriptory (fd)** -- celá čísla 0, 1, 2, 3, ...
- každý fd odkazuje na záznam v SysFileTable
- fd 0 = stdin, fd 1 = stdout, fd 2 = stderr
- `open()` vrátí první volný index -- např. 3

---

## Schéma

```
PROCES                     KERNEL                        DISK

Task File Table            Sys File Table
┌──────────────┐          ┌───────────────┐
│ 0  (stdin)   │          │  file pointer │
│ 1  (stdout)  │          │  → dyn. i-uzel│
│ 2  (stderr)  │          ├───────────────┤
│ 3            │────────▶ │  file pointer │          fyzický i-uzel
│  ...         │          │  → dyn. i-uzel│──┐       ┌──────────┐
└──────────────┘          ├───────────────┤  │  ┌───▶│ metadata │
                           │  ...          │  │  │    ├──────────┤
                           └───────────────┘  │  │    │  data    │
                                              │  │    └──────────┘
                           dynamický i-uzel   │  │
                           ┌───────────────┐  │  │
                           │  i-číslo      │──┘──┘
                           │  ref. count   │
                           └───────────────┘
```

> **DOPLNIT OBRÁZEK Z TABULE**

---

## dup vs. přímý zápis

- **`dup(fd)`** -- zkopíruje ukazatel v Task File Table; oba fd sdílejí tentýž záznam v SysFileTable (= stejný file pointer, stejný soubor)
- **přímý zápis `fd = 3`** -- jen přepsání čísla v paměti procesu, OS o tom neví, nic se reálně nezmění


# stat obr.png 

vypise zakladni infromace jmeno velikost pčet obsazených  bloku atd -> dodat nejakej priklad ze systemu potom

zmeny obsahu atd 

mame treba parametr -f a ukazuje souborove id 























# TROŠKU MIMO TÉMA : 

# FAT – File Allocation Table

## Co to je

FAT je datová struktura používaná souborovým systémem (původně MS-DOS, dnes např. USB flash disky, SD karty) pro sledování toho, **které bloky (clustery) na disku patří kterému souboru**.

Je to v podstatě **pole indexů** -- každá položka odpovídá jednomu clusteru na disku a říká, co v něm je.

---

## Jak funguje

Disk je rozdělen na stejně velké bloky = **clustery**. FAT tabulka má pro každý cluster jeden záznam:

```
index │ hodnota
──────┼──────────────────────────────
  0   │ rezervováno
  1   │ rezervováno
  2   │ → 3          (soubor A pokračuje v clusteru 3)
  3   │ → 5          (soubor A pokračuje v clusteru 5)
  4   │ → EOF        (konec souboru B)
  5   │ → EOF        (konec souboru A)
  6   │ FREE         (volný cluster)
  7   │ BAD          (vadný sektor)
```

Soubor A tedy zabírá clustery: 2 → 3 → 5 → EOF (řetěz).

---

## Struktura disku s FAT

```
┌──────────────┐
│  Boot sector │  ← informace o FS (velikost clusteru, počet FAT kopií, ...)
├──────────────┤
│   FAT #1     │  ← hlavní tabulka
├──────────────┤
│   FAT #2     │  ← záložní kopie (redundance)
├──────────────┤
│ Root adresář │  ← jen u FAT12/FAT16; u FAT32 je běžný adresář
├──────────────┤
│    Data      │  ← samotné clustery se soubory
└──────────────┘
```

---

## Varianty

| Verze  | Max. velikost svazku | Typické použití         |
|--------|----------------------|-------------------------|
| FAT12  | ~32 MiB              | staré diskety           |
| FAT16  | ~2 GiB               | starší HDD, DOS/Win 9x  |
| FAT32  | ~2 TiB               | USB flash, SD karty      |
| exFAT  | ~128 PiB             | moderní flash média     |

---

ssssss# Nevýhody FAT vs. moderní FS (ext4, NTFS)

- **fragmentace** -- soubory jsou roztroušeny v řetězech po celém disku
- **žádná žurnalizace** -- při výpadku proudu hrozí poškození dat
- **žádná přístupová práva** -- není vlastník, nejsou oprávnění (Unix práva)
- **žádné i-uzly** -- metadata jsou jen v adresářových záznamech, ne v samostatné struktuře
- FAT tabulka musí být celá v paměti pro rychlý přístup → u velkých disků je obrovská

---

## Srovnání s i-uzlovým přístupem (Unix/Linux)

| Vlastnost            | FAT                        | Unix (ext4)              |
|----------------------|----------------------------|--------------------------|
| Metadata souboru     | v adresářovém záznamu      | v i-uzlu                 |
| Alokace bloků        | řetěz v FAT tabulce        | přímé/nepřímé ukazatele v i-uzlu |
| Přístupová práva     | ne                         | ano (rwx, ACL)           |
| Žurnalizace          | ne (exFAT částečně)        | ano                      |
| Pevné odkazy         | ne                         | ano                      |





# KONEC MIMO TÉMA





