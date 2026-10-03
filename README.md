# PDF Password Remover

A small command-line utility that saves a password-protected PDF as an unencrypted PDF. You must know the PDF's password to use it.

## Requirements

- Python 3.9 or newer
- [`pikepdf`](https://pikepdf.readthedocs.io/)

## Setup

Create and activate a virtual environment, then install the dependency:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pikepdf
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

Set the password in a local `.env` file to avoid entering it on every run. Copy `.env.example` to `.env` and set `PDF_PASSWORD`:

```dotenv
PDF_PASSWORD=your_pdf_password
```

The `.env` file is ignored by Git. You can also provide the password through the `PDF_PASSWORD` environment variable.

## Usage

The input PDF path is required. If you omit the output path, the program writes a sibling file with `-unlocked` added to its name:

```bash
python3 main.py protected.pdf
```

For example, that command creates `protected-unlocked.pdf` in the same directory as `protected.pdf`.

Choose an output path explicitly:

```bash
python3 main.py protected.pdf unlocked-copy.pdf
```

Override the password from `.env` for a single run:

```bash
python3 main.py protected.pdf --password 'the pdf password'
```

You can combine an explicit output path and password:

```bash
python3 main.py protected.pdf unlocked-copy.pdf --password 'the pdf password'
```

Show all command options:

```bash
python3 main.py --help
```

## Run without activating the virtual environment

From the project directory, use the included launcher. It calls the Python interpreter inside `.venv` directly, so there is no need to activate the environment:

```bash
./unlock-pdf protected.pdf
./unlock-pdf protected.pdf unlocked-copy.pdf --password 'the pdf password'
```

On first use, make the launcher executable if needed:

```bash
chmod +x unlock-pdf
```

The launcher still expects the one-time setup above to have created `.venv` and installed `pikepdf`.

## Notes

- The input file is kept as-is; the unlocked copy is saved to the output path.
- If a file already exists at the output path, `pikepdf` may replace it.
- Keep the output file secure if it contains sensitive information, since it is no longer protected by the PDF password.
