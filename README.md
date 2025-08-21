# GitHub Actions Repository

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)

A comprehensive collection of GitHub Actions workflows demonstrating CI/CD best practices, custom actions, reusable workflows, and code quality automation.

## 📋 Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Available Workflows](#available-workflows)
- [Custom Actions](#custom-actions)

- [Reusable Workflows](#reusable-workflows)
- [Code Quality & Linting](#code-quality--linting)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Overview

This repository serves as a comprehensive example and template collection for GitHub Actions workflows. It includes complete CI/CD pipelines, custom actions, reusable workflows, and various code quality automation examples.

### Key Features

- **Complete CI/CD Pipeline**: Full implementation from code to deployment
- **Custom Actions**: Reusable custom actions with `action.yml`
- **Reusable Workflows**: Shareable workflows across repositories
- **Code Quality**: Automated linting and quality checks
- **Multi-Language Support**: Examples for Python, SQL, dbt, and more
- **Best Practices**: Industry-standard workflow patterns

## 📁 Repository Structure

```
.
├── action.yml                    # Custom action definition
├── hello-world.py               # Sample Python script
├── LICENSE                      # Apache 2.0 License
├── linting-messy-scripts        # Scripts for linting demos
├── sample-CD.py                 # Sample continuous deployment script
├── .github/workflows/           # GitHub Actions workflows
│   ├── Complete-CICD.yml                        # Full CI/CD pipeline
│   ├── Custom-Action-Workflow.yml               # Custom action usage
│   ├── Python-Linting-Check.yml                # Python code quality
│   ├── Reusable-Linter-Caller-DifferentRepo.yml # Cross-repo linter
│   ├── Reusable-Linter-Caller-SameRepo.yml     # Same-repo linter
│   ├── Reusable-Linter.yml                     # Base reusable linter
│   ├── sample-CD.yaml                           # CD workflow example
│   └── Super-Linter.yml                        # Multi-language linting
└── linting/                     # Sample files for linting
    ├── dbt_model.sql           # dbt model example
    ├── python_script.py        # Python script example
    └── sql_script.sql          # SQL script example
```

## 🔄 Available Workflows

### Complete CI/CD Pipeline (`Complete-CICD.yml`)
A comprehensive continuous integration and continuous deployment workflow that includes:
- Code checkout and setup
- Build and test stages
- Security scanning
- Quality checks
- Deployment automation

### Python Linting Check (`Python-Linting-Check.yml`)
Automated Python code quality enforcement including:
- PEP 8 compliance checking
- Code formatting validation
- Import sorting verification
- Security vulnerability scanning

### Super Linter (`Super-Linter.yml`)
Multi-language linting workflow supporting:
- Python
- SQL
- YAML
- JSON
- Markdown
- Shell scripts

## 🛠️ Custom Actions

### Main Custom Action (`action.yml`)
The repository includes a custom action defined in `action.yml` that can be used across workflows. This action demonstrates:
- Input parameter handling
- Custom logic execution
- Output generation
- Reusability patterns



## 🔄 Reusable Workflows

### Reusable Linter (`Reusable-Linter.yml`)
A base linting workflow that can be called from other workflows or repositories.

**Features:**
- Configurable linting rules
- Multiple language support
- Customizable failure conditions

### Cross-Repository Linter (`Reusable-Linter-Caller-DifferentRepo.yml`)
Demonstrates how to use reusable workflows from different repositories.

### Same-Repository Linter (`Reusable-Linter-Caller-SameRepo.yml`)
Example of calling reusable workflows within the same repository.

## 🎯 Code Quality & Linting

### Sample Files for Testing
The `linting/` directory contains sample files for testing linting workflows:

- **`python_script.py`**: Python code for testing Python linters
- **`sql_script.sql`**: SQL queries for SQL linting
- **`dbt_model.sql`**: dbt model for dbt-specific linting

### Supported Linting Tools
- **Python**: flake8, black, isort, pylint
- **SQL**: sqlfluff, SQL formatting
- **dbt**: dbt-checkpoint, dbt linting
- **YAML**: yamllint
- **General**: Super-Linter for multi-language support

## 🚀 Getting Started

Reference workflows from this repository in your projects or use the custom action and reusable workflows as needed.

## 🔧 Customization

### Workflow Inputs
Most workflows support customization through inputs. Check individual workflow files for available options:

- Language versions
- Linting strictness
- Deployment targets
- Security scan configurations

### Environment Variables
Configure workflows using environment variables:
- `PYTHON_VERSION`: Python version for Python workflows
- `NODE_VERSION`: Node.js version for Node workflows
- `DEPLOYMENT_ENV`: Target deployment environment

## 📦 Dependencies

The workflows in this repository use various GitHub Actions:
- `actions/checkout@v4`: Repository checkout
- `actions/setup-python@v4`: Python environment setup
- `actions/setup-node@v4`: Node.js environment setup
- `github/super-linter@v4`: Multi-language linting

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Reusable Workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
- [Custom Actions](https://docs.github.com/en/actions/creating-actions)

---

⭐ **Star this repository if it helps you with your GitHub Actions journey!**
