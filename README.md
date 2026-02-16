# NLP Information Extraction System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> An intelligent chatbot system for automated information extraction from text messages using regular expressions and genetic algorithms.

This project was developed as part of the Natural Language Processing course (Spring 2024) at Sharif University of Technology. It implements a sophisticated information extraction system that automatically categorizes and extracts structured data from chat messages in Persian and English.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Contributors](#contributors)
- [License](#license)

## 🎯 Overview

This system combines multiple NLP techniques to extract meaningful information from unstructured text:

- **Regex-based Information Extraction**: Identifies emails, phone numbers, addresses, and other structured data
- **Genetic Algorithm for Regex Generation**: Automatically generates optimized regex patterns from example text
- **Custom Pattern Management**: User-defined regex patterns stored in SQLite database
- **Matrix Chatbot Integration**: Interactive bot interface using the Opsdroid framework

## ✨ Features

### Core Capabilities

- **📧 Email Extraction**: Detects and extracts email addresses from text
- **📱 Phone Number Recognition**: Identifies mobile and landline numbers (supports Persian/Arabic numerals)
- **🏠 Address Extraction**: Recognizes Persian addresses using entity-based pattern matching
- **🤖 Automated Regex Generation**: Creates optimal regex patterns using genetic algorithms
- **💾 Custom Pattern Storage**: Manages user-defined patterns in a SQLite database
- **🌐 Multi-language Support**: Handles both Persian and English text
- **💬 Interactive Chatbot**: Matrix protocol integration for real-time interaction

### Genetic Algorithm Features

- Population-based evolution (configurable generations and population size)
- 21 distinct gene types representing regex building blocks
- Fitness-based selection and optimization
- Returns top-3 best-performing patterns

## 🏗️ Architecture

### System Components

```
┌─────────────────────────────────────────────┐
│           Opsdroid Chatbot Layer            │
│  (Matrix Protocol, Command Handlers)        │
└────────────┬────────────────────────────────┘
             │
    ┌────────┴────────┐
    │                 │
┌───▼────┐    ┌──────▼─────┐    ┌──────────┐
│  Info  │    │   Regex    │    │   New    │
│ Module │    │ Generator  │    │  Regex   │
│        │    │            │    │  Module  │
│ Extract│    │ Genetic    │    │ Database │
│ Contact│    │ Algorithm  │    │ Patterns │
│  Info  │    │            │    │          │
└────────┘    └────────────┘    └──────────┘
```

### Module Descriptions

#### 1. **regex_generator** - Genetic Algorithm Engine
Generates optimized regex patterns through evolutionary algorithms:
- **Genes**: 21 types (digits, letters, spaces, character ranges, etc.)
- **Evolution**: Population-based selection over multiple generations
- **Output**: Top-3 regex patterns ranked by fitness score

#### 2. **info** - Information Extraction
Specialized extractors for structured data:
- `number.py`: Mobile/landline phone number extraction
- `address.py`: Persian address recognition using entity keywords
- `extractor.py`: Email extraction and message classification

#### 3. **new_regex** - Pattern Database
SQLite-based management of custom regex patterns:
- Store user-defined patterns with unique names
- Test messages against all stored patterns
- Validate custom regex on text

#### 4. **skills** - Chatbot Commands
Opsdroid bot command handlers:
- `/generate` - Generate regex from examples
- `/info` - Extract contact information
- `/add` - Store custom pattern
- `/checkall` - Test against stored patterns
- `/checkone` - Validate custom regex
- `/help` - Display available commands

## 🛠️ Technologies

- **Python 3.8+** - Core programming language
- **Opsdroid** - Chatbot framework with Matrix protocol support
- **SQLAlchemy 2.0.30** - ORM for database management
- **Regular Expressions** - Pattern matching and text extraction
- **Genetic Algorithms** - Automated regex optimization
- **Matrix Protocol** - Decentralized communication
- **SQLite** - Lightweight pattern database

## 📥 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Matrix account (for chatbot functionality)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/NLP-1403/HW2.git
   cd HW2
   ```

2. **Install dependencies**
   ```bash
   pip install -r new_regex/requirements.txt
   pip install opsdroid
   ```

3. **Configure the bot**
   
   Edit `configuration.yaml` and update the Matrix credentials:
   ```yaml
   connectors:
     matrix:
       mxid: '@your_bot:matrix.server'
       password: 'your_password'
       homeserver: 'https://matrix.server'
   ```

4. **Initialize the database**
   ```bash
   python new_regex/main.py
   ```

5. **Run the chatbot**
   ```bash
   opsdroid start
   ```

## 🚀 Usage

### Command-Line Usage

#### Extract Information from Text
```python
from info.extractor import Extractor

text = ["ایمیل من test@example.com است و شماره تلفن من 09123456789 است"]
results = Extractor(text, char_threshold=100)
print(results)
```

#### Generate Regex Pattern
```python
from regex_generator.generator import generator

examples = ["test123", "demo456", "sample789"]
patterns = generator(examples, population=100, generation=10)
print(patterns)  # Returns top-3 regex patterns
```

#### Add Custom Pattern
```python
from new_regex.main import add_regex, check_message_patterns

add_regex("postal_code", r"\d{10}")
matches = check_message_patterns("کد پستی: 1234567890")
```

### Chatbot Commands

Once the bot is running, interact via Matrix chat:

```
/generate 100 10 test@email.com test2@email.com
→ Generates regex patterns from examples

/info 50 My email is test@example.com
→ Extracts emails, phone numbers, addresses

/add postal_code \d{10}
→ Stores custom regex pattern

/checkall Test message 1234567890
→ Tests against all stored patterns

/help
→ Shows all available commands
```

## 📁 Project Structure

```
HW2/
├── configuration.yaml          # Opsdroid bot configuration
├── NLP_Spring1403_HW2.pdf     # Assignment specification
├── LICENSE                     # MIT License
├── README.md                   # This file
│
├── info/                       # Information extraction module
│   ├── AddressEntities.txt    # Persian address entity keywords
│   ├── AreaCodes.txt          # Iranian area codes
│   ├── address.py             # Address extraction
│   ├── number.py              # Phone number extraction
│   └── extractor.py           # Main extraction orchestrator
│
├── regex_generator/            # Genetic algorithm engine
│   ├── const.py               # Gene type definitions
│   ├── genetic.py             # Genetic algorithm core (21 gene types)
│   ├── generator.py           # Main regex generator
│   ├── parser.py              # Gene-to-regex conversion
│   ├── decoder.py             # Pattern decoder
│   ├── formatter.py           # Output formatter
│   ├── evalute.py             # Fitness evaluation
│   └── utils.py               # Utility functions
│
├── new_regex/                  # Custom pattern database
│   ├── main.py                # Database operations
│   ├── requirements.txt       # SQLAlchemy dependencies
│   └── message_patterns.db    # SQLite database
│
├── skills/                     # Opsdroid bot commands
│   ├── accept_invite.py       # Auto-accept invites
│   ├── join_room.py           # Join Matrix rooms
│   ├── help.py                # Help command
│   ├── regex_generator.py     # /generate command
│   ├── info.py                # /info command
│   ├── add_regex.py           # /add command
│   ├── check_with_new_regexes.py  # /checkall command
│   └── check_message_with_regex.py  # /checkone command
│
└── document/                   # LaTeX report
    ├── Report.tex             # Technical documentation
    ├── solutionclass.cls      # LaTeX template
    └── img/                   # Report images
```

## 📚 Documentation

- **Detailed Report**: See the [PDF assignment specification](NLP_Spring1403_HW2.pdf) for project requirements
- **Technical Documentation**: See `document/Report.tex` for implementation details
- **Code Comments**: Inline documentation in Python modules

### Key Concepts

**Genetic Algorithm Genes (21 types):**
- `0x00`: `\d` (digits)
- `0x01`: `[A-Z]` (uppercase)
- `0x02`: `[a-z]` (lowercase)
- `0x03`: `[A-Za-z]` (letters)
- `0x06`: `\w` (word characters)
- `0x07`: `\s` (whitespace)
- `0x09`: `.` (any character)
- `0x0c-0x14`: Character ranges and column-based patterns

## 👥 Contributors

This project was developed by:

- **Ilia Hashemi Rad** - Student ID: 99102456
- **AmirMohammad Fakhimi** - Student ID: 99170531
- **AmirMahdi Namjoo** - Student ID: 97107212

**Course**: Natural Language Processing (Spring 2024)  
**Institution**: Sharif University of Technology  
**Department**: Computer Engineering

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Sharif University of Technology NLP Course Staff
- Opsdroid Framework Community
- Matrix Protocol Contributors

---

**Note**: This is an educational project developed for academic purposes. The genetic algorithm implementation demonstrates automated regex pattern generation, while the information extraction showcases practical NLP applications for Persian and English text.
