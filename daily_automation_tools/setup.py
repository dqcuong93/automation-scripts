"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

import pathlib

# Always prefer setuptools over distutils
from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="daily_automations_tools",
    version="2.0.0",
    description="Automation of some daily works you should have",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dqcuong93/automation-scripts",
    author="Chris Q. D.",
    author_email="dqcuong93@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
    package_dir={"": "src"},
    python_requires=">=3.10, <4",
    install_requires=["black", "click", "flake8", "isort", "eradicate", "prompt_toolkit"],
    entry_points={
        "console_scripts": [
            "daily_automation_tools=cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/dqcuong93/automation-scripts/issues",
        "Source": "https://github.com/dqcuong93/automation-scripts",
    },
)
