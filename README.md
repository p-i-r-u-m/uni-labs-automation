# uni-labs-automation

**University Labs Automation** is a CLI-driven system to automate the generation of programming lab reports according to faculty requirements. It sets up a C++/GoogleTest build environment, pulls lab tasks from an SQLite database, auto‑generates UML class diagrams, and produces a fully‑formatted `.docx` report— all via simple shell scripts.

---

## ⚙️ Features

- **C++ & GoogleTest via CMake**  
  Preconfigured build environment for compiling and testing lab solutions.

- **Automated UML Diagram Generation**  
  Generates class diagrams (PNG) on each successful build.

- **SQLite‑Backed Task Management**  
  Pulls current lab task descriptions & screenshots from `labs.db` and `tasks_img/`.

- **.docx Report Generation**  
  Fills a lab report template with title, objective, task screenshot, UML, code listing, unit‑test results, and conclusions.

- **Shell‑Script Interface**  
  Quick commands for testing, building, running, and exporting reports.

---

## 🔧 Project Structure

```bash
.
├── lab_templ
│   ├── 0test.sh
│   ├── 1build.sh
│   ├── 2run.sh
│   ├── 3docx.sh
│   ├── clang-uml.yml
│   ├── CMakeLists.txt
│   ├── report
│   │   ├── diagram
│   │   └── lab-number.txt
│   ├── src
│   │   └── main.cpp
│   └── tests
│       └── unit_tests.cpp
├── organize.sh
├── packy
│   ├── database
│   │   ├── labs.db
│   │   └── tasks_img
│   ├── functions_packy
│   │   ├── auto_report.py
│   │   ├── file_manage.py
│   │   ├── packy_functions.py
│   │   ├── __pycache__
│   │   │   ├── auto_report.cpython-313.pyc
│   │   │   ├── file_manage.cpython-313.pyc
│   │   │   ├── header.cpython-313.pyc
│   │   │   ├── packy_functions.cpython-313.pyc
│   │   │   └── tests_generation.cpython-313.pyc
│   │   └── tests_generation.py
│   └── packy.py
└── README.md
```


---

## 🚀 Quick Workflow

1. **Configure paths & data**  
   Before anything, update script paths and database location in:
   - `lab_templ/0test.sh`  
   - `lab_templ/1build.sh`  
   - `lab_templ/2run.sh`  
   - `lab_templ/3docx.sh`  
   - `organize.sh`  
   - `packy/functions_packy/auto_report.py`  
   - `packy/database/labs.db`  
   - the `packy/database/tasks_img/` folder

2. **Populate the database**  
   Insert your lab tasks (IDs, objectives, screenshots) into `labs.db` and place task images under `tasks_img/`.

3. **Generate a new lab template**  
   From the project root:
   ```bash
   ./organize.sh
   
> This creates a new lab_templ/report/lab-<number>/ folder with placeholders.

4. **Enter the lab folder**

```bash
cd lab_templ/report/lab-<number>
```

5. **Build & test your solution**

```bash
./0test.sh      # create template for unit test (alpha, don't stable)
./1build.sh     # compiles C++ code and auto-generates UML
./2run.sh       # builds & runs code + tests in one step
```

6. **Generate the .docx report**

```bash
./3docx.sh
```

> outputs lab-<number>.docx with embedded screenshots, UML diagram, code listing, test result, and conclusions.

---

## 📋 Configuration

Shell scripts (`0test.sh`, `1build.sh`, `2run.sh`, `3docx.sh`, `organize.sh`) rely on environment variables or hard‑coded paths—edit the top of each script to point at your local compiler, CMake, and Python interpreter.

`auto_report.py`: adjust template paths and placeholders to match your .docx template.

`labs.db`: update with your lab numbers, titles, objectives, and screenshot filenames.

`tasks_img/`: store the corresponding PNG/JPG screenshots of the lab tasks here.

---

## 📦 Dependencies

- C++17 compiler (e.g., g++)

- CMake (v3.10+)

- GoogleTest (installed or vendored via CMake)

- Python 3.8+ (for auto_report.py)

- Pandoc & LibreOffice CLI (optional, if extending to other document formats)
