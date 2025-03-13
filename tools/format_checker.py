#!/usr/bin/env python3
"""Python code formatting checker.

This script checks and verifies Python code against coding conventions
using multiple formatting tools: black, isort, flake8, and eradicate.

Dependencies:
    Required packages (install with pip):
        black>=24.2.0
        isort>=5.13.2
        flake8>=7.0.0
        eradicate>=2.3.0

Usage:
    format-check [OPTIONS] PATH...

Arguments:
    PATH  One or more Python files or directories to check.
          For directories, all .py files will be checked recursively.

Options:
    -v, --verbose  Show detailed output from formatters
    --help        Show this help message

Examples:
    # Check a single file
    format-check script.py

    # Check multiple files
    format-check file1.py file2.py file3.py

    # Check all Python files in a directory recursively
    format-check project_directory/

    # Check with verbose output
    format-check -v script.py

Tools Used:
    - black: Code formatter that formats code in a consistent style
    - isort: Sorts and formats imports
    - flake8: Style guide enforcement
    - eradicate: Removes commented-out code

Exit Status:
    0 - All checks passed
    1 - Some formatters reported issues
    2 - Error occurred during execution (missing dependencies, invalid paths, etc.)
"""

import logging
import shutil
import subprocess
from pathlib import Path
from typing import List, Tuple

import click

FORMATTER_COMMANDS = {
    "black": ["black"],
    "isort": ["isort"],
    "flake8": ["flake8"],
    "eradicate": ["eradicate"],
}

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def check_dependencies() -> None:
    """Verify all required formatting tools are installed."""
    missing_tools = []
    for tool in FORMATTER_COMMANDS:
        if not shutil.which(tool):
            missing_tools.append(tool)

    if missing_tools:
        tools_str = ", ".join(missing_tools)
        raise click.ClickException(
            f"Missing required tools: {tools_str}. "
            f"Please install with: pip install {' '.join(missing_tools)}"
        )


def run_formatter(formatter: str, files: List[Path]) -> Tuple[bool, str]:
    """Run a specific code formatter on the given files.

    Args:
        formatter: Name of the formatter to run
        files: List of file paths to format

    Returns:
        Tuple of (success, output)
    """
    cmd = FORMATTER_COMMANDS[formatter] + [str(f) for f in files]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, f"{e.stdout}\n{e.stderr}"


def collect_python_files(paths: Tuple[Path, ...]) -> List[Path]:
    """Collect all Python files from the given paths.

    Args:
        paths: Tuple of paths to process

    Returns:
        List of Path objects pointing to Python files
    """
    files = []
    for path in paths:
        if path.is_dir():
            files.extend(path.glob("**/*.py"))
        else:
            files.append(path)
    return files


def run_all_formatters(files: List[Path], verbose: bool) -> bool:
    """Run all formatters on the given files.

    Args:
        files: List of files to check
        verbose: Whether to show detailed output

    Returns:
        True if all formatters passed, False otherwise
    """
    all_passed = True
    for formatter in FORMATTER_COMMANDS:
        logger.info(f"\nRunning {formatter}...")
        success, output = run_formatter(formatter, files)

        if not success:
            all_passed = False
            logger.error(f"{formatter} found issues:")
            if verbose or formatter in ["flake8", "eradicate"]:
                logger.error(output)
        elif verbose:
            logger.info(output if output else f"{formatter} passed")

    return all_passed


@click.command(context_settings={"help_option_names": ["-h", "--help"]}, no_args_is_help=True)
@click.argument(
    "paths",
    nargs=-1,
    type=click.Path(exists=True, path_type=Path),
    required=True,
)
@click.option("-v", "--verbose", is_flag=True, help="Show detailed output from formatters")
def check_code(paths: Tuple[Path, ...], verbose: bool) -> None:
    """Check Python code formatting using multiple tools.

    Runs black, isort, flake8, and eradicate on the specified Python files
    or directories to ensure consistent code formatting and style.

    Example:
        format-check file1.py file2.py
        format-check directory/
    """
    try:
        check_dependencies()

        files = collect_python_files(paths)
        if not files:
            logger.warning("No Python files found to check")
            return

        logger.info(f"Checking {len(files)} Python files...")

        if run_all_formatters(files, verbose):
            logger.info("\n✨ All formatters passed!")
        else:
            raise click.ClickException("Some formatters reported issues")

    except Exception as e:
        logger.error(f"Error during formatting: {e}")
        raise click.ClickException(str(e))


if __name__ == "__main__":
    check_code()
