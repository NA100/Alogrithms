import os

project_name = "your_project"
package_name = "your_package"

structure = {
    f"{project_name}/src/{package_name}": ["__init__.py", "module1.py"],
    f"{project_name}/tests": ["__init__.py", "test_module1.py"],
    f"{project_name}/scripts": ["run.py"],
    f"{project_name}": [
        ".gitignore",
        "README.md",
        "requirements.txt",
        "pyproject.toml",
        "setup.cfg",
        "setup.py"
    ]
}

boilerplate = {
    "README.md": f"# {project_name}\n\nProject description.\n",
    ".gitignore": "__pycache__/\n*.pyc\n.env\n.venv/\n",
    "requirements.txt": "# Add dependencies here\n",
    "pyproject.toml": """\
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "your_project"
version = "0.1.0"
description = "Your project description"
authors = [{name = "Your Name", email = "your@email.com"}]
""",
    "setup.cfg": """\
[metadata]
name = your_project
version = 0.1.0
description = Your project description
author = Your Name

[options]
packages = find:
install_requires =
""",
    "setup.py": """\
from setuptools import setup

setup()
""",
    "src/{}/__init__.py".format(package_name): "",
    "src/{}/module1.py".format(package_name): "# Module 1 code here\n",
    "tests/__init__.py": "",
    "tests/test_module1.py": """\
from src.{} import module1

def test_sample():
    assert True
""".format(package_name),
    "scripts/run.py": "# Entry point script\n"
}


def create_structure():
    for path, files in structure.items():
        os.makedirs(path, exist_ok=True)
        for file in files:
            full_path = os.path.join(path, file)
            content_key = file if file in boilerplate else os.path.relpath(full_path, project_name)
            with open(full_path, "w") as f:
                f.write(boilerplate.get(content_key, ""))


if __name__ == "__main__":
    create_structure()
    print(f"✅ Project structure for '{project_name}' created.")

