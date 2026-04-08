# POS
  Jak spustit:
  python3 /home/posuser/zombieprocesy/zombie_demo.py        # 3  
  zombie, 15 sekund
  python3 /home/posuser/zombieprocesy/zombie_demo.py 5 30   # 5  
  zombie, 30 sekund

  Během čekání v druhém terminálu zkontroluj:
  ps aux | grep Z          # zombie mají stav Z
  ps -o pid,ppid,stat,cmd  # detail stavu

  Co skript demonstruje:
  1. Rodič forkuje děti → děti okamžitě os._exit(0)
  2. Rodič nevolá wait() → děti jsou zombie (stav Z v tabulce
  procesů)
  3. Po uplynutí doby rodič zavolá wait() → zombie zmizí
