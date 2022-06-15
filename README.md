# admin-panel

## Install dependencies

### One-time action

```bash
pip install poetry
poetry config virtualenvs.in-project true
```

### For each projet

Prepare virtual environment:
```bash
poetry init
poetry install
```
Activate virtual environment:
```bash
source .venv/bin/activate
```
Prepare .env file as specified in .env.default<br/>
Export environment variables:
```bash
export $(grep -v '^#' .env | xargs)
```

## Usage

Run:
```bash
python -m frontend
```
Or use make utility:
```bash
make run
```
