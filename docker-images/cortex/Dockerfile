# Cortex con el analizador MISP para el laboratorio SIN.
# La imagen oficial es Debian sin Python: se instala python3 y las
# dependencias que el analizador MISP necesita (cortexutils y pymisp).
FROM thehiveproject/cortex:4.1.0

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-pip python3-venv ca-certificates \
    && pip3 install --no-cache-dir --break-system-packages cortexutils pymisp \
    && python3 -c "import cortexutils, pymisp; print('deps ok')" \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
USER cortex
