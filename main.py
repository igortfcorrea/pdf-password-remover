import pikepdf
import os
import argparse
from pathlib import Path


def load_env_file(env_path: Path = Path(".env")) -> None:
    """Load KEY=VALUE entries without overriding variables already in the environment."""
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("\"'"))

def remove_pdf_password(
    input_pdf: str,
    output_pdf: str,
    password: str
):
    input_path = Path(input_pdf)
    output_path = Path(output_pdf)

    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_pdf}")

    with pikepdf.open(input_path, password=password) as pdf:
        pdf.save(output_path)

    print(f"Password removed successfully: {output_path}")

if __name__ == "__main__":
    load_env_file()

    parser = argparse.ArgumentParser(description="Remove the password from an encrypted PDF.")
    parser.add_argument("input_pdf", help="PDF file to unlock")
    parser.add_argument(
        "output_pdf",
        nargs="?",
        help="Output path (default: <input-name>-unlocked.pdf)",
    )
    parser.add_argument(
        "--password",
        help="PDF password (defaults to PDF_PASSWORD from .env or the environment)",
    )
    args = parser.parse_args()

    input_path = Path(args.input_pdf)
    output_path = Path(args.output_pdf) if args.output_pdf else input_path.with_name(
        f"{input_path.stem}-unlocked{input_path.suffix}"
    )

    pdf_password = args.password or os.getenv("PDF_PASSWORD")
    if not pdf_password:
        raise SystemExit("Set PDF_PASSWORD in .env or pass --password PASSWORD")

    remove_pdf_password(
        input_pdf=str(input_path),
        output_pdf=str(output_path),
        password=pdf_password,
    )
