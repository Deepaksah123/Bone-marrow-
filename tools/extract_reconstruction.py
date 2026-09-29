#!/usr/bin/env python3
import pathlib, sys, zipfile

if len(sys.argv) < 3:
    raise SystemExit("Usage: extract_reconstruction.py base.apk output_dir")

apk = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
exclude_file = pathlib.Path(__file__).parent.parent / "reconstruction" / "EXCLUDED_INTERFACES.txt"
exclude = {
    line.strip()
    for line in exclude_file.read_text().splitlines()
    if line.strip() and not line.startswith("#")
}

with zipfile.ZipFile(apk) as z:
    for info in z.infolist():
        if info.filename in exclude:
            continue
        target = out / info.filename
        target.parent.mkdir(parents=True, exist_ok=True)
        if not info.is_dir():
            target.write_bytes(z.read(info))

print("Exact APK hierarchy extracted to:", out)
