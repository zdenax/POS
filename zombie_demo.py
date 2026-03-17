#!/usr/bin/env python3
"""
POS - Zombie procesy - demonstrace
Zombie = proces který skončil, ale rodič ještě nezavolal wait()
"""

import os
import time
import sys

def vytvor_zombie(pocet: int, doba_zombie_sekund: int = 15):
    print(f"\n=== Vytváříme {pocet} zombie procesů ===")
    print(f"Rodič PID: {os.getpid()}\n")

    pidy_deti = []

    for i in range(pocet):
        pid = os.fork()

        if pid == 0:
            # --- DÍTĚ ---
            # Okamžitě skončí → stane se zombiem protože rodič nevolá wait()
            print(f"  Dítě {i+1}: PID={os.getpid()} končím → stávám se zombie...")
            os._exit(0)
        else:
            # --- RODIČ ---
            pidy_deti.append(pid)

    print(f"\nRodič nevolá wait() → děti jsou nyní ZOMBIE")
    print(f"PIDs zombie dětí: {pidy_deti}")
    print(f"\nZkontroluj stav: ps -o pid,ppid,stat,cmd -p {' '.join(map(str, pidy_deti))}")
    print(f"Nebo:            ps aux | grep -E 'Z|zombie'")
    print(f"\nZombie zůstanou {doba_zombie_sekund} sekund, pak rodič zavolá wait()...\n")

    # Rodič čeká - zombie mezitím existují v tabulce procesů
    time.sleep(doba_zombie_sekund)

    # Úklid - rodič zavolá wait() pro každé dítě
    print("=== Rodič volá wait() - uklízíme zombie ===")
    for pid in pidy_deti:
        ziskany_pid, status = os.waitpid(pid, 0)
        print(f"  Zombie PID={ziskany_pid} odstraněn (exit status={status >> 8})")

    print("\nVšechny zombie odstraněny. Tabulka procesů je čistá.")


if __name__ == "__main__":
    pocet = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    doba  = int(sys.argv[2]) if len(sys.argv) > 2 else 15

    if pocet > 20:
        print("Max 20 zombie pro bezpečnost.")
        sys.exit(1)

    vytvor_zombie(pocet, doba)
