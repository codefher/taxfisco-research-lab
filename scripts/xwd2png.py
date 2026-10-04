#!/usr/bin/env python3
"""
Convierte una captura de X (formato XWD, la salida de `xwd`) a PNG.

Por que hace falta
------------------
Para la evidencia del Prototipo II hay que capturar UNA ventana concreta, no la
pantalla completa: el escritorio del usuario tiene otras ventanas apiladas (el
navegador, el editor) que tapan al terminal. `xwd -id <id>` captura los pixeles
de esa ventana por mucho que este oculta detras de otra, pero Grafana no lo lee y
no hay ImageMagick ni ffmpeg en la maquina, asi que se parsea el formato XWD a
mano y se escribe el PNG con PIL.

XWD (X Window Dump, version 7) es un header de enteros de 32 bits big-endian,
despues el nombre de la ventana, la paleta de color y los pixeles. Para un
visual TrueColor de 32 bits por pixel el dato es BGRX por pixel.

Uso:
    xwd -id <win_id> -silent | python3 scripts/xwd2png.py salida.png
    python3 scripts/xwd2png.py salida.png < fichero.xwd
"""

import struct
import sys


def parse(path, out):
    with open(path, "rb") as fh:
        buf = fh.read()

    if len(buf) < 100:
        raise SystemExit("XWD demasiado corto")

    fields = struct.unpack(">25I", buf[:100])
    (header_size, file_version, pixmap_format, pixmap_depth, pixmap_width,
     pixmap_height, xoffset, byte_order, bitmap_unit, bitmap_bit_order,
     bitmap_pad, bits_per_pixel, bytes_per_line, visual_class, red_mask,
     green_mask, blue_mask, bits_per_rgb, colormap_entries, ncolors,
     window_width, window_height, window_x, window_y,
     window_bdrwidth) = fields

    if file_version != 7:
        raise SystemExit(f"version XWD no soportada: {file_version}")

    offset = header_size + ncolors * 12
    data = buf[offset:]
    if len(data) < bytes_per_line * pixmap_height:
        raise SystemExit(
            f"datos de pixeles incompletos: {len(data)} bytes para "
            f"{bytes_per_line * pixmap_height} esperados"
        )

    from PIL import Image
    img = Image.new("RGB", (pixmap_width, pixmap_height))
    px = img.load()

    swap = (byte_order == 1)  # MSBFirst
    fmt = ">" if swap else "<"
    step = bits_per_pixel // 8
    padding = bytes_per_line - pixmap_width * step

    for y in range(pixmap_height):
        row_start = y * bytes_per_line
        for x in range(pixmap_width):
            off = row_start + x * step
            b, g, r = struct.unpack_from(fmt + "BBB", data, off)
            px[x, y] = (r, g, b)

    img.save(out)
    print(f"  {out} ({pixmap_width}x{pixmap_height}, "
          f"depth={pixmap_depth}, bpp={bits_per_pixel})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit(2)
    if len(sys.argv) == 2:
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False, suffix=".xwd") as tmp:
            tmp.write(sys.stdin.buffer.read())
            src = tmp.name
    else:
        src = sys.argv[2]
    parse(src, sys.argv[1])
