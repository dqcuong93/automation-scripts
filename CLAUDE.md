# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Small collection of standalone Python CLI scripts (Click-based) meant to be symlinked into `~/.bin` and run directly from the shell. There is no package build, no test suite, and no CI config in this repo — each script in `tools/` is self-contained and independently runnable.

## Commands

Install dependencies:
```bash
pip install -r requirements.txt
```

Run a script directly during development (no need to symlink):
```bash
python tools/create_web_link.py --help
python tools/ssh_switcher.py --help
```

Lint/format a script (the project's own formatting stack, per `pyproject.toml` and `.flake8`); run these directly rather than via `tools/format_checker.py` (deprecated, see below):
```bash
black tools/
isort tools/
flake8 tools/
mypy tools/
bandit -r tools/
```

There is no test suite (`pytest`, etc.) in this repo — do not assume one exists.

## Architecture

Each file in `tools/` is a standalone `click`-based CLI entry point with no shared internal modules between them; they are wired to shell commands only via symlinks created during installation (see README's "Installation and Usage" section), not via `setup.py`/`pyproject.toml` entry points. When adding a new tool, follow the existing pattern: a single `tools/<name>.py` file with a module docstring documenting Usage/Options/Examples/Dependencies/Environment (used as the tool's `--help`-adjacent reference), a `click.command` with `context_settings={"help_option_names": ["-h", "--help"]}`, and `logging`-based output (not `print`).

Formatting/lint configuration (`.flake8`, `pyproject.toml`) targets Python 3.8, 100-char line length, black-compatible isort, and Google-style docstrings — match this style in new code.

Notable existing behavior to be aware of:
- `tools/format_checker.py` is **deprecated** (marked as such in its own docstring/warning) and not symlinked during install. It duplicates what a `pre-commit` setup does better, and as shipped its `run_all_formatters` invokes `black`/`isort` without `--check`, so running it reformats files in place rather than only reporting issues. Do not build on it; use `pre-commit` or the formatter CLIs directly instead.
- `mypy`, `bandit`, and `safety` are listed in `requirements.txt` but have no wrapper script invoking them — run them directly if needed.
- `ssh_switcher.py`'s `SSH_IDENTITIES` mapping is hardcoded per-user (aliases like `cuong`, `gk`, `finsc_bitbucket`); adding an identity means editing this dict directly, there is no config file.
