# 🚀 xcli

### AI-Powered Linux Command Line Assistant

**Translate Natural Language into Safe Linux Commands**

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python)]()
[![Gemini](https://img.shields.io/badge/Gemini-AI-4285F4?style=for-the-badge&logo=google)]()
[![Typer](https://img.shields.io/badge/Typer-CLI-green?style=for-the-badge)]()
[![Rich](https://img.shields.io/badge/Rich-Terminal-blue?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)]()

---

### 🧠 Learn Linux. 🚀 Execute Safely. 🔒 Stay Protected.

</div>

---

# 📖 Table of Contents

- Overview
- Motivation
- Features
- Why xcli?
- Demo
- Current Capabilities
- Architecture
- Project Structure
- Design Principles
- Request Flow
- Future Roadmap
- Installation
- Usage

---

# 🌟 Overview

**xcli** is an AI-powered Linux command-line assistant that converts **natural language** into **safe Linux commands** while protecting users from dangerous or destructive operations.

Instead of memorizing hundreds of Linux commands, users can simply type what they want in plain English:

```bash
x list files
```

xcli translates the request into

```bash
ls
```

shows the generated command,

validates it against security policies,

asks for confirmation when necessary,

and safely executes it.

Unlike traditional AI wrappers, xcli is designed around a **Security First Architecture**, ensuring commands are validated before execution.

---

# 💡 Motivation

Learning Linux can be overwhelming because it requires remembering hundreds of commands, flags, and syntax.

Examples:

```bash
find . -name "*.py"
```

```bash
grep -rn "TODO" .
```

```bash
du -sh *
```

Most beginners end up searching Google or Stack Overflow repeatedly.

The goal of xcli is to provide an assistant that lets users think in **English**, while gradually teaching them Linux through everyday usage.

The project also serves as an exploration of AI-powered developer tooling, secure command execution, and modern CLI application architecture.

---

# ✨ Features

## Implemented

- ✅ Natural Language → Linux Command Translation
- ✅ Google Gemini Integration
- ✅ Rich Terminal UI
- ✅ Safe Command Execution
- ✅ Security Validator
- ✅ YAML-Based Security Policies
- ✅ Command Confirmation
- ✅ Modular Project Architecture
- ✅ Context Awareness (Current Directory, Files, Git, Python, System)
- ✅ Pydantic Structured Responses

---

## In Progress

- 🚧 Linux Teaching Mode
- 🚧 Conversation Memory
- 🚧 Git Assistant
- 🚧 Plugin System

---

## Planned

- 🔜 Voice Commands
- 🔜 Remote SSH Support
- 🔜 Docker Assistant
- 🔜 Kubernetes Assistant
- 🔜 Multi-Agent Workflow
- 🔜 AI Debugger
- 🔜 Shell History Intelligence
- 🔜 Interactive Linux Tutor

---

# 🎯 Why xcli?

Most AI command generators simply generate commands.

xcli goes much further.

It follows this pipeline:

```

English Request
↓

AI Translation
↓

Context Awareness
↓

Security Validation
↓

Confirmation
↓

Safe Execution

```

This ensures users never execute AI-generated commands blindly.

---

# 🖥 Demo

Example:

```bash
$ x list files
```

Output

```text
──────────────── Linux AI Assistant ────────────────

English

list files

Linux Command

ls

Meaning

List files in the current directory.

Risk

SAFE

────────────────────────────────────────────────────

Output

README.md

app

tests

pyproject.toml
```

---

Another example

```bash
$ x delete all files
```

Output

```text
BLOCKED

Reason:

'rm' is blocked by security policy.
```

---

# 🛡 Security First Philosophy

Unlike many AI assistants, xcli **never executes AI-generated commands directly**.

Every generated command passes through multiple security layers before execution.

Security layers include:

- Dangerous command detection
- YAML policy validation
- Prompt injection resistance
- Shell operator detection
- Safe subprocess execution
- User confirmation

Security is treated as a core feature rather than an afterthought.

---

# 🧠 Current Capabilities

| Feature | Status |
|----------|--------|
| English → Linux | ✅ |
| Gemini AI | ✅ |
| Rich CLI | ✅ |
| Context Collection | ✅ |
| YAML Policy Engine | ✅ |
| Secure Executor | ✅ |
| Confirmation | ✅ |
| Prompt Injection Protection | ✅ |
| Linux Tutor | 🚧 |
| Conversation Memory | 🚧 |
| Plugins | 🚧 |
| Voice Mode | 🔜 |

---

# 🏗 Architecture

xcli follows a modular layered architecture.

```

                User

                  │

                  ▼

          Command Line Interface

                  │

                  ▼

             CLI Controller

                  │

        ┌─────────┴─────────┐

        ▼                   ▼

 Context Service      AI Translator

        │                   │

        ▼                   ▼

 System Snapshot     Gemini Provider

        │                   │

        └─────────┬─────────┘

                  ▼

         Linux Command Model

                  ▼

       Security Validator

                  ▼

         YAML Policy Engine

                  ▼

      Confirmation Manager

                  ▼

       Secure Executor

                  ▼

            Terminal Output

```

---

# 🏛 Project Structure

```text
xcli/

├── app/
│
├── ai/
│   ├── provider.py
│   ├── translator.py
│   ├── prompt.py
│
├── context/
│   ├── models.py
│   ├── service.py
│
├── executor/
│   └── executor.py
│
├── models/
│   ├── command.py
│   ├── execution.py
│   └── validation_result.py
│
├── security/
│   ├── validator.py
│   ├── scanner.py
│   ├── rule_engine.py
│   ├── policy_loader.py
│   └── rules/
│       └── default.yaml
│
├── ui/
│   ├── printer.py
│   └── confirm.py
│
├── cli.py
├── config.py
├── main.py
│
├── tests/
│
├── pyproject.toml
├── README.md
└── .env
```

---

# 🎯 Design Principles

The architecture follows several software engineering principles.

## Single Responsibility Principle

Every module has one responsibility.

| Module | Responsibility |
|---------|---------------|
| CLI | User Interaction |
| Translator | AI Translation |
| Context Service | Machine Information |
| Validator | Security |
| Executor | Execute Commands |
| Printer | Terminal UI |

---

## Security by Default

Every generated command is considered **untrusted** until validated.

AI never executes commands directly.

---

## AI as a Component

AI is treated as one module within the system—not the system itself.

This allows replacing Gemini with another LLM in the future without changing the rest of the application.

---

## Extensibility

New command categories, validators, context providers, or AI models can be added without major architectural changes.

---

# 🔄 Request Flow

```

User

│

▼

CLI

│

▼

Collect System Context

│

▼

Build AI Prompt

│

▼

Gemini

│

▼

Structured Linux Command

│

▼

Security Validation

│

▼

Confirmation

│

▼

Execution

│

▼

Output

```

---

# 🧩 Core Components

| Component | Description |
|------------|-------------|
| CLI | Handles user input |
| Context Service | Collects system information |
| AI Provider | Communicates with Gemini |
| Translator | Converts English into Linux commands |
| Validator | Applies security rules |
| Policy Engine | Reads YAML security policies |
| Executor | Safely executes commands |
| Printer | Displays formatted terminal output |

---

# 🚀 Version

Current Version

```
v0.4.0-alpha
```

Current Milestone

```
Milestone 4 — Smart Context Engine
```

<div align="center">

# 🚀 xcli

### AI-Powered Linux Command Line Assistant

**Translate Natural Language into Safe Linux Commands**

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python)]()
[![Gemini](https://img.shields.io/badge/Gemini-AI-4285F4?style=for-the-badge&logo=google)]()
[![Typer](https://img.shields.io/badge/Typer-CLI-green?style=for-the-badge)]()
[![Rich](https://img.shields.io/badge/Rich-Terminal-blue?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)]()

---

### 🧠 Learn Linux. 🚀 Execute Safely. 🔒 Stay Protected.

</div>

---

# 📖 Table of Contents

- Overview
- Motivation
- Features
- Why xcli?
- Demo
- Current Capabilities
- Architecture
- Project Structure
- Design Principles
- Request Flow
- Future Roadmap
- Installation
- Usage

---

# 🌟 Overview

**xcli** is an AI-powered Linux command-line assistant that converts **natural language** into **safe Linux commands** while protecting users from dangerous or destructive operations.

Instead of memorizing hundreds of Linux commands, users can simply type what they want in plain English:

```bash
x list files
```

xcli translates the request into

```bash
ls
```

shows the generated command,

validates it against security policies,

asks for confirmation when necessary,

and safely executes it.

Unlike traditional AI wrappers, xcli is designed around a **Security First Architecture**, ensuring commands are validated before execution.

---

# 💡 Motivation

Learning Linux can be overwhelming because it requires remembering hundreds of commands, flags, and syntax.

Examples:

```bash
find . -name "*.py"
```

```bash
grep -rn "TODO" .
```

```bash
du -sh *
```

Most beginners end up searching Google or Stack Overflow repeatedly.

The goal of xcli is to provide an assistant that lets users think in **English**, while gradually teaching them Linux through everyday usage.

The project also serves as an exploration of AI-powered developer tooling, secure command execution, and modern CLI application architecture.

---

# ✨ Features

## Implemented

- ✅ Natural Language → Linux Command Translation
- ✅ Google Gemini Integration
- ✅ Rich Terminal UI
- ✅ Safe Command Execution
- ✅ Security Validator
- ✅ YAML-Based Security Policies
- ✅ Command Confirmation
- ✅ Modular Project Architecture
- ✅ Context Awareness (Current Directory, Files, Git, Python, System)
- ✅ Pydantic Structured Responses

---

## In Progress

- 🚧 Linux Teaching Mode
- 🚧 Conversation Memory
- 🚧 Git Assistant
- 🚧 Plugin System

---

## Planned

- 🔜 Voice Commands
- 🔜 Remote SSH Support
- 🔜 Docker Assistant
- 🔜 Kubernetes Assistant
- 🔜 Multi-Agent Workflow
- 🔜 AI Debugger
- 🔜 Shell History Intelligence
- 🔜 Interactive Linux Tutor

---

# 🎯 Why xcli?

Most AI command generators simply generate commands.

xcli goes much further.

It follows this pipeline:

```

English Request
↓

AI Translation
↓

Context Awareness
↓

Security Validation
↓

Confirmation
↓

Safe Execution

```

This ensures users never execute AI-generated commands blindly.

---

# 🖥 Demo

Example:

```bash
$ x list files
```

Output

```text
──────────────── Linux AI Assistant ────────────────

English

list files

Linux Command

ls

Meaning

List files in the current directory.

Risk

SAFE

────────────────────────────────────────────────────

Output

README.md

app

tests

pyproject.toml
```

---

Another example

```bash
$ x delete all files
```

Output

```text
BLOCKED

Reason:

'rm' is blocked by security policy.
```

---

# 🛡 Security First Philosophy

Unlike many AI assistants, xcli **never executes AI-generated commands directly**.

Every generated command passes through multiple security layers before execution.

Security layers include:

- Dangerous command detection
- YAML policy validation
- Prompt injection resistance
- Shell operator detection
- Safe subprocess execution
- User confirmation

Security is treated as a core feature rather than an afterthought.

---

# 🧠 Current Capabilities

| Feature | Status |
|----------|--------|
| English → Linux | ✅ |
| Gemini AI | ✅ |
| Rich CLI | ✅ |
| Context Collection | ✅ |
| YAML Policy Engine | ✅ |
| Secure Executor | ✅ |
| Confirmation | ✅ |
| Prompt Injection Protection | ✅ |
| Linux Tutor | 🚧 |
| Conversation Memory | 🚧 |
| Plugins | 🚧 |
| Voice Mode | 🔜 |

---

# 🏗 Architecture

xcli follows a modular layered architecture.

```

                User

                  │

                  ▼

          Command Line Interface

                  │

                  ▼

             CLI Controller

                  │

        ┌─────────┴─────────┐

        ▼                   ▼

 Context Service      AI Translator

        │                   │

        ▼                   ▼

 System Snapshot     Gemini Provider

        │                   │

        └─────────┬─────────┘

                  ▼

         Linux Command Model

                  ▼

       Security Validator

                  ▼

         YAML Policy Engine

                  ▼

      Confirmation Manager

                  ▼

       Secure Executor

                  ▼

            Terminal Output

```

---

# 🏛 Project Structure

```text
xcli/

├── app/
│
├── ai/
│   ├── provider.py
│   ├── translator.py
│   ├── prompt.py
│
├── context/
│   ├── models.py
│   ├── service.py
│
├── executor/
│   └── executor.py
│
├── models/
│   ├── command.py
│   ├── execution.py
│   └── validation_result.py
│
├── security/
│   ├── validator.py
│   ├── scanner.py
│   ├── rule_engine.py
│   ├── policy_loader.py
│   └── rules/
│       └── default.yaml
│
├── ui/
│   ├── printer.py
│   └── confirm.py
│
├── cli.py
├── config.py
├── main.py
│
├── tests/
│
├── pyproject.toml
├── README.md
└── .env
```

---

# 🎯 Design Principles

The architecture follows several software engineering principles.

## Single Responsibility Principle

Every module has one responsibility.

| Module | Responsibility |
|---------|---------------|
| CLI | User Interaction |
| Translator | AI Translation |
| Context Service | Machine Information |
| Validator | Security |
| Executor | Execute Commands |
| Printer | Terminal UI |

---

## Security by Default

Every generated command is considered **untrusted** until validated.

AI never executes commands directly.

---

## AI as a Component

AI is treated as one module within the system—not the system itself.

This allows replacing Gemini with another LLM in the future without changing the rest of the application.

---

## Extensibility

New command categories, validators, context providers, or AI models can be added without major architectural changes.

---

# 🔄 Request Flow

```

User

│

▼

CLI

│

▼

Collect System Context

│

▼

Build AI Prompt

│

▼

Gemini

│

▼

Structured Linux Command

│

▼

Security Validation

│

▼

Confirmation

│

▼

Execution

│

▼

Output

```

---

# 🧩 Core Components

| Component | Description |
|------------|-------------|
| CLI | Handles user input |
| Context Service | Collects system information |
| AI Provider | Communicates with Gemini |
| Translator | Converts English into Linux commands |
| Validator | Applies security rules |
| Policy Engine | Reads YAML security policies |
| Executor | Safely executes commands |
| Printer | Displays formatted terminal output |

---

# 🚀 Version

Current Version

```
v0.4.0-alpha
```

Current Milestone

```
Milestone 4 — Smart Context Engine


# ⚙️ Installation

## Prerequisites

Before installing xcli, ensure you have the following:

- Python **3.12+**
- Git
- Ubuntu Linux (recommended)
- Google Gemini API Key
- `uv` package manager

---

## Install uv

If you don't have **uv** installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify installation:

```bash
uv --version
```

---

## Clone Repository

```bash
git clone https://github.com/<your-username>/xcli.git

cd xcli
```

---

## Create Virtual Environment

```bash
uv venv
```

Activate it

Linux

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
uv sync
```

or

```bash
uv pip install -e .
```

---

## Configure Environment

Create

```
.env
```

Example

```env
GEMINI_API_KEY=your_api_key_here

MODEL=gemini-2.5-flash
```

---

## Run xcli

During development

```bash
uv run python -m app.main list files
```

or

```bash
uv run python -m app.main current directory
```

After installation

```bash
x list files
```

---

# Example Commands

```bash
x list files
```

↓

```bash
ls
```

---

```bash
x current directory
```

↓

```bash
pwd
```

---

```bash
x find python files
```

↓

```bash
find . -name "*.py"
```

---

```bash
x show disk usage
```

↓

```bash
du -sh
```

---

# Configuration

## Environment Variables

| Variable | Description |
|-----------|-------------|
| GEMINI_API_KEY | Gemini API Key |
| MODEL | Gemini model name |

---

## Security Policies

Security policies are stored as YAML files.

```
app/security/rules/
```

Example

```yaml
commands:

  ls:
    risk: safe
    confirm: false

  mkdir:
    risk: medium
    confirm: true

blocked_commands:

  - rm
  - shutdown
  - reboot
```

Changing YAML files allows modifying security behavior without changing Python code.

---

# 🛠 Development

## Running Tests

```bash
pytest
```

---

## Linting

```bash
ruff check .
```

---

## Formatting

```bash
ruff format .
```

---

# Project Dependencies

| Package | Purpose |
|----------|----------|
| Typer | CLI Framework |
| Rich | Beautiful Terminal UI |
| Pydantic | Structured Models |
| Google GenAI | Gemini API |
| PyYAML | Policy Engine |
| psutil | System Context |
| python-dotenv | Environment Variables |

---

# Directory Overview

```
app/

├── ai/
├── context/
├── executor/
├── models/
├── security/
├── ui/
└── main.py
```

Each directory has a single responsibility, following the Single Responsibility Principle (SRP).

---
# 🗺️ Project Roadmap

xcli is being developed incrementally using milestone-based development.

Each milestone introduces a major architectural improvement rather than just adding features.

---

# 📅 Milestone Timeline

| Milestone | Status | Description |
|-----------|--------|-------------|
| Milestone 1 | ✅ Completed | CLI Foundation |
| Milestone 2 | ✅ Completed | AI Translation & Secure Execution |
| Milestone 3 | 🚧 In Progress | Learning Experience |
| Milestone 4 | 🚧 In Progress | Smart Context Engine |
| Milestone 5 | 🔜 Planned | Conversation Memory |
| Milestone 6 | 🔜 Planned | Git Assistant |
| Milestone 7 | 🔜 Planned | Linux Tutor |
| Milestone 8 | 🔜 Planned | Plugin System |
| Milestone 9 | 🔜 Planned | Multi-Agent Architecture |
| Version 1.0 | 🎯 Goal | Production Ready AI Linux Assistant |

---

# ✅ Milestone 1 — CLI Foundation

Goal:

Build the basic command-line application.

### Features

- CLI using Typer
- Rich Terminal UI
- Project Architecture
- uv Package Management
- Configuration Management
- Modular Folder Structure

---

# ✅ Milestone 2 — AI Command Translation

Goal:

Convert natural language into Linux commands.

### Features

- Google Gemini Integration
- Structured JSON Responses
- Pydantic Models
- Secure Executor
- YAML Policy Engine
- Prompt Injection Detection
- Dangerous Command Blocking
- Confirmation System

Example

```
User

↓

"List files"

↓

Gemini

↓

ls

↓

Validator

↓

Executor
```

---

# 🚧 Milestone 3 — Learning Experience

Goal:

Transform xcli into a Linux learning assistant.

### Planned Features

- Command explanations
- Linux syntax guide
- Interactive tutorials
- Beginner mode
- Learning progress
- Command breakdown

Example

```
x find python files
```

Output

```
Command

find . -name "*.py"

Explanation

find

Search utility

.

Current directory

-name

Filter by filename

*.py

Matches Python files
```

---

# 🚧 Milestone 4 — Smart Context Engine

Goal:

Make xcli aware of the current machine state.

Instead of generating commands blindly,

Gemini receives

- Current directory
- Existing files
- Git repository
- Python version
- CPU usage
- Memory usage
- Disk usage
- Virtual environment
- Running processes
- Network interfaces

Example

```
x open main.py
```

Current directory

```
README.md

main.py

app.py
```

Gemini already knows

```
main.py exists
```

leading to much better command generation.

---

# 🔜 Milestone 5 — Conversation Memory

Goal:

Allow xcli to remember previous interactions.

Example

```
x find python files

↓

main.py

app.py

↓

x open the first one

↓

main.py

↓

x rename it to app_old.py
```

Future capabilities

- Session memory
- Reference previous commands
- Multi-step workflows
- Undo support

---

# 🔜 Milestone 6 — Git Assistant

Goal:

Provide AI-powered Git operations.

Examples

```
x commit my changes
```

↓

```
git add .

git commit -m "..."
```

Other features

- Resolve merge conflicts
- Explain Git errors
- Branch management
- Interactive commits
- Pull request preparation

---

# 🔜 Milestone 7 — Linux Tutor

Goal:

Teach Linux while users work.

Features

- Daily challenges
- Command quizzes
- Interactive lessons
- Difficulty levels
- Learning statistics
- Achievement badges

---

# 🔜 Milestone 8 — Plugin System

Goal:

Allow developers to extend xcli.

Future plugin examples

```
Docker

Kubernetes

AWS CLI

Azure CLI

Terraform

GitHub CLI
```

Plugin Architecture

```
Plugin

↓

Command Registration

↓

Security Validation

↓

Execution
```

---

# 🔜 Milestone 9 — Multi-Agent Architecture

Instead of one AI model,

multiple specialized agents will collaborate.

Example

```
User

↓

Task Planner

↓

Linux Agent

↓

Security Agent

↓

Git Agent

↓

Executor
```

Benefits

- Better reasoning
- More reliable execution
- Reduced hallucinations
- Complex task automation

---

# 🎯 Version 1.0 Vision

Version 1.0 aims to become a production-ready AI terminal assistant.

Core capabilities

- Natural language terminal
- Linux tutor
- Secure execution
- Context awareness
- Conversation memory
- Git assistant
- Plugin ecosystem
- Multiple AI providers

---

# 🚀 Long-Term Vision

The long-term goal is to build xcli into an intelligent developer assistant rather than a simple command generator.

Future capabilities include

- Docker Assistant
- Kubernetes Assistant
- AWS CLI Assistant
- SSH Remote Execution
- Local LLM Support
- Voice Commands
- File Editing
- AI Debugger
- Code Generation
- Task Automation
- Workflow Execution
- Developer Copilot for Linux

Ultimately, xcli aims to become an AI-powered operating system companion capable of understanding natural language, reasoning about the current environment, and safely assisting developers with everyday terminal tasks.
