# 🚀 SCHNEIDER ELECTRIC AI CODE REVIEWER v8.0 - COMPLETE DEPLOYMENT GUIDE

## 📦 WHAT'S NEW IN THIS UPDATE

### ✅ CRITICAL FIX: Language-Specific Code Generation
**Problem Solved**: AI was generating Python code for all languages (C, Java, JS, etc.)

**Solution Implemented**:
1. Created **6 comprehensive rule files** (17-20 rules each per language)
2. Integrated rules into **both** `/analyze` and `/fix` endpoints
3. Added **filename parameter** to fix endpoint (was missing!)
4. Fixed **Unicode character errors** in extension.ts

### 📊 Language Rule Files Created:
- `c_rules.json` - 17 C-specific rules (memory safety, buffer overflow prevention)
- `cpp_rules.json` - 18 C++ rules (smart pointers, Rule of Five, modern C++)
- `java_rules.json` - 16 Java rules (generics, exception handling, resource management)
- `js_rules.json` - 18 JavaScript rules (modern ES6+, async/await, security)
- `ts_rules.json` - 20 TypeScript rules (strict typing, type safety, null checks)
- `python_rules.json` - 18 Python rules (PEP8, type hints, pythonic code)
- `st_rules.json` - 15 Structured Text rules (IEC 61131-3, Schneider prefixes)

---

## 📂 STEP 1: FILE DEPLOYMENT

### Backend Files (Copy to `E:\Schneider_Hackathon\server\`):

```powershell
# 1. Copy app.py (updated with language-specific rules)
Copy-Item app.py E:\Schneider_Hackathon\server\app.py -Force

# 2. Copy all 7 language rule JSON files
Copy-Item c_rules.json E:\Schneider_Hackathon\server\ -Force
Copy-Item cpp_rules.json E:\Schneider_Hackathon\server\ -Force
Copy-Item java_rules.json E:\Schneider_Hackathon\server\ -Force
Copy-Item js_rules.json E:\Schneider_Hackathon\server\ -Force
Copy-Item ts_rules.json E:\Schneider_Hackathon\server\ -Force
Copy-Item python_rules.json E:\Schneider_Hackathon\server\ -Force
Copy-Item st_rules.json E:\Schneider_Hackathon\server\ -Force

# 3. Update requirements.txt if needed
Copy-Item requirements.txt E:\Schneider_Hackathon\server\ -Force
```

### Frontend Files (Copy to `E:\Schneider_Hackathon\extension\src\`):

```powershell
# 1. Copy TypeScript files
Copy-Item extension.ts E:\Schneider_Hackathon\extension\src\extension.ts -Force
Copy-Item llmClient.ts E:\Schneider_Hackathon\extension\src\llmClient.ts -Force
Copy-Item chatbotView.ts E:\Schneider_Hackathon\extension\src\chatbotView.ts -Force

# 2. Update package.json if needed
Copy-Item package.json E:\Schneider_Hackathon\extension\package.json -Force
```

---

## 🔧 STEP 2: RECOMPILE EXTENSION

```powershell
cd E:\Schneider_Hackathon\extension
npm run compile
```

**Expected Output**:
```
> schneider-ai-code-reviewer@8.0.0 compile
> tsc -p ./
✔ Compilation successful
```

**If you see errors**:
- Check that extension.ts header has NO Unicode characters (╔ ║ ╚)
- Should only have plain ASCII comments
- Run `npm install` first if dependencies are missing

---

## 🐍 STEP 3: RESTART BACKEND

```powershell
cd E:\Schneider_Hackathon\server
.\venv\Scripts\activate
python app.py
```

**Expected Startup Logs**:
```
INFO:__main__:✅ Gemini initialized: gemini-2.0-flash
INFO:__main__:✅ Loaded 436 Schneider rules
INFO:__main__:   📋 Naming: 89
INFO:__main__:   📋 Structure: 127
INFO:__main__:   📋 Security: 43
INFO:__main__:   📋 Energy: 31
INFO:__main__:   📋 General: 146
INFO:__main__:✅ Loaded 17 C language-specific rules
INFO:__main__:✅ Loaded 18 CPP language-specific rules
INFO:__main__:✅ Loaded 16 JAVA language-specific rules
INFO:__main__:✅ Loaded 18 JS language-specific rules
INFO:__main__:✅ Loaded 20 TS language-specific rules
INFO:__main__:✅ Loaded 18 PY language-specific rules
INFO:__main__:✅ Loaded 15 ST language-specific rules
 * Running on http://127.0.0.1:5000
```

**CRITICAL**: You MUST see "Loaded X language-specific rules" for each language!

---

## 🔄 STEP 4: RELOAD VSCODE

1. Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)
2. Type: `Developer: Reload Window`
3. Press Enter

This reloads the extension with new compiled code.

---

## 🧪 STEP 5: TESTING GUIDE

### Test 1: C File Language Detection

Create `test_buggy.c`:
```c
#include <stdio.h>

#define HIGH_POWER_THRESHOLD 1000
#define DATA_ARRAY_SIZE 100

int calculate_energy(int voltage, int current) {
    int power = voltage * current;
    return power;
}

void process_motor(int speed, int torque) {
    int result = speed * torque;
    if (result > HIGH_POWER_THRESHOLD) {
        printf("High power\n");
    }
}

int get_data(int arr[]) {
    int i;
    for (i = 0; i < DATA_ARRAY_SIZE; i++) {
        arr[i] = i * 2;
    }
    return i;
}

int main() {
    int voltage = 220;
    int current = 5;
    int power = calculate_energy(voltage, current);
    printf("%d\n", power);
    int data_array[DATA_ARRAY_SIZE] = {0};
    get_data(data_array);
    return 0;
}
```

**Expected Analysis**:
- Score: 30-50/100 (should find many issues)
- Issues should include:
  - [C-DOC-001] Missing function header comments
  - [C-NAMING-001] camelCase instead of snake_case
  - [C-HEADER-001] Missing necessary headers
  - [C-SECURITY-002] Array bounds not validated

**Click Auto-Fix**:
- ✅ **MUST return C code**, NOT Python
- ✅ Should have `#include` statements
- ✅ Should have function comments
- ✅ Should use snake_case names
- ✅ Should include bounds checking

### Test 2: JavaScript File

Create `test_buggy.js`:
```javascript
var HIGH_POWER_THRESHOLD = 1000
var DATA_ARRAY_SIZE = 100

function calculateEnergy(voltage, current) {
    var power = voltage * current
    return power
}

function processMotor(speed, torque) {
    var result = speed * torque
    if (result > HIGH_POWER_THRESHOLD) {
        console.log("High power")
    }
}

function getData(arr) {
    for (var i = 0; i < DATA_ARRAY_SIZE; i++) {
        arr[i] = i * 2
    }
    return i
}

var voltage = 220
var current = 5
var power = calculateEnergy(voltage, current)
console.log(power)
var dataArray = new Array(DATA_ARRAY_SIZE).fill(0)
getData(dataArray)
```

**Expected Issues**:
- [JS-CONST-001] Use const/let instead of var
- [JS-SEMICOLON-001] Missing semicolons
- [JS-DOC-001] Missing JSDoc comments
- [JS-CONSOLE-001] console.log in production

**Click Auto-Fix**:
- ✅ **MUST return JavaScript code**, NOT Python
- ✅ Should use `const` and `let`
- ✅ Should have semicolons
- ✅ Should have JSDoc comments

### Test 3: TypeScript File

Create `test_buggy.ts`:
```typescript
var HIGH_POWER_THRESHOLD = 1000
var DATA_ARRAY_SIZE = 100

function calculateEnergy(voltage, current) {
    var power = voltage * current
    return power
}

function processMotor(speed, torque) {
    var result = speed * torque
    if (result > HIGH_POWER_THRESHOLD) {
        console.log("High power")
    }
}

function getData(arr) {
    for (var i = 0; i < DATA_ARRAY_SIZE; i++) {
        arr[i] = i * 2
    }
    return i
}

var voltage = 220
var current = 5
var power = calculateEnergy(voltage, current)
console.log(power)
var dataArray: number[] = new Array(DATA_ARRAY_SIZE).fill(0)
getData(dataArray)
```

**Expected Issues**:
- [TS-TYPE-001] Missing type annotations on parameters/returns
- [TS-CONST-001] Use const instead of var
- [TS-TYPE-002] Avoid implicit 'any' types
- [TS-DOC-001] Missing TSDoc comments

**Click Auto-Fix**:
- ✅ **MUST return TypeScript code** with type annotations
- ✅ Should have explicit types everywhere
- ✅ Should use `const` and `let`
- ✅ Should have TSDoc comments

---

## 🎯 SUCCESS CRITERIA

### ✅ Backend Started Successfully
- [ ] Backend shows "Loaded X language-specific rules" for all 7 languages
- [ ] Flask server running on port 5000
- [ ] No errors in terminal

### ✅ Extension Compiled Successfully
- [ ] `npm run compile` runs without errors
- [ ] No TypeScript compilation errors
- [ ] VSCode extension loads without errors

### ✅ Language Detection Works
- [ ] C files analyzed as C (not Python)
- [ ] JavaScript files analyzed as JavaScript
- [ ] TypeScript files analyzed as TypeScript
- [ ] Each language shows language-specific issues

### ✅ Auto-Fix Returns Correct Language
- [ ] C file Auto-Fix returns C code (with #include, snake_case)
- [ ] JS file Auto-Fix returns JS code (with const/let, semicolons)
- [ ] TS file Auto-Fix returns TS code (with type annotations)
- [ ] NO language returns Python when it shouldn't

---

## 🐛 TROUBLESHOOTING

### Problem: Backend doesn't show "Loaded X language-specific rules"

**Solution**:
```powershell
# Verify rule files exist
cd E:\Schneider_Hackathon\server
ls *.json
```

Should show:
```
c_rules.json
cpp_rules.json
Extracted_Rules_From_Pdf.json
java_rules.json
js_rules.json
python_rules.json
st_rules.json
ts_rules.json
```

### Problem: Auto-Fix still returns Python for C files

**Checklist**:
1. ✅ Did backend show "Loaded 17 C language-specific rules"?
2. ✅ Did you restart the backend after copying app.py?
3. ✅ Is the file actually named with .c extension?
4. ✅ Check backend logs - does it say "Analyzing test.c"?

**Debug**: Add print statement in app.py line 600:
```python
logger.info(f"🔍 DEBUG: filename={filename}, file_ext={file_ext}, lang_name={lang_name}")
```

### Problem: Extension compilation errors with Unicode characters

**Solution**: Check extension.ts lines 1-8. Should be:
```typescript
/**
 * SCHNEIDER ELECTRIC AI CODE REVIEWER - PRODUCTION v8.0
 * - ENHANCED FEATURES: History tracking, statistics, better UX
```

NOT:
```typescript
/**
 * ╔══════════════════════════════════════════════════════════════════════════════╗
 * ║  SCHNEIDER ELECTRIC AI CODE REVIEWER - PRODUCTION v8.0                      ║
```

---

## 📝 WHAT CHANGED IN EACH FILE

### `app.py` Changes:
1. **Lines 136-158**: Added LANGUAGE_RULES dictionary loading
2. **Lines 361-370**: Added lang_rules_text formatting in `/analyze`
3. **Lines 549-605**: Fixed `/fix` endpoint to accept filename parameter
4. **Lines 565-575**: Added ALL language-specific rules to fix prompt

### `llmClient.ts` Changes:
1. **Line 140**: Added `filename` parameter to `fixCode()` method
2. **Line 148**: Pass filename to backend in `/fix` request

### `chatbotView.ts` Changes:
1. **Line where fixCode is called**: Pass `this.currentFileName` to fixCode

### `extension.ts` Changes:
1. **Lines 1-6**: Removed Unicode box-drawing characters

---

## 📊 EXPECTED RULE COUNTS

| Language | Rules | Key Focus Areas |
|----------|-------|-----------------|
| C | 17 | Memory safety, buffer overflows, header guards |
| C++ | 18 | Smart pointers, Rule of Five, modern C++11/14 |
| Java | 16 | Generics, exceptions, resource management |
| JavaScript | 18 | Modern ES6+, async/await, const/let |
| TypeScript | 20 | Strict typing, null safety, interfaces |
| Python | 18 | PEP8, type hints, docstrings |
| ST (PLC) | 15 | IEC 61131-3, variable prefixes, Schneider standards |

---

## ✅ FINAL VERIFICATION COMMAND

Run this to verify everything is in place:

```powershell
# Check backend files
cd E:\Schneider_Hackathon\server
echo "=== Backend Files ==="
ls *.json | Select-Object Name
ls app.py | Select-Object Name

# Check frontend files
cd E:\Schneider_Hackathon\extension\src
echo "=== Frontend Files ==="
ls *.ts | Select-Object Name

# Check compilation
cd ..
npm run compile
```

---

## 🎉 SUCCESS MESSAGE

When everything works, you'll see:

**Backend Terminal**:
```
✅ Loaded 436 Schneider rules
✅ Loaded 17 C language-specific rules
✅ Loaded 18 CPP language-specific rules
✅ Loaded 16 JAVA language-specific rules
✅ Loaded 18 JS language-specific rules
✅ Loaded 20 TS language-specific rules
✅ Loaded 18 PY language-specific rules
✅ Loaded 15 ST language-specific rules
```

**VSCode Extension**:
- Analyzes C files → Gets C-specific issues
- Auto-Fix C files → Returns proper C code
- Same for all 7 supported languages

---

## 📞 SUPPORT

If issues persist:
1. Check backend logs in terminal
2. Check VSCode Output panel (View → Output → Schneider AI)
3. Verify all rule JSON files are valid JSON (no syntax errors)
4. Ensure `.env` file has valid API keys

Good luck with the hackathon! 🚀

---

## 🐙 GIT PUSH COMMANDS — Complete Reference

Use these any time you update a file. Always run from `D:\Schneider_Hackathon`.

---

### ⚡ Push Everything at Once (Most Common)
```bash
cd D:\Schneider_Hackathon
git add .
git status          # double-check .env is NOT listed
git commit -m "Describe what you changed"
git push origin main
```

---

### File-by-File Commands

#### 🐍 Backend — app.py
```bash
git add server/app.py
git commit -m "Update backend app.py"
git push origin main
```

#### 📦 Backend — requirements.txt
```bash
git add server/requirements.txt
git commit -m "Update Python dependencies"
git push origin main
```

#### 📋 Backend — Schneider Rules JSON
```bash
git add server/Extracted_Rules_From_Pdf.json
git commit -m "Add new extracted rules from Rules_Guide_Used"
git push origin main
```

#### 📁 Backend — Language Rule Files
```bash
git add server/c_rules.json server/cpp_rules.json server/java_rules.json server/js_rules.json server/ts_rules.json server/python_rules.json server/st_rules.json
git commit -m "Update language-specific rule files"
git push origin main
```

#### 🤖 Rule Extractor — Streamlit App (v3.3)
```bash
git add rule_extractor.py
git commit -m "Update rule extractor to v3.3 - raw HTTP, triple-LLM fallback, download button"
git push origin main
```

#### 🔧 Rule Extractor + requirements.txt (together)
```bash
git add rule_extractor.py server/requirements.txt
git commit -m "Add rule extractor with dependencies"
git push origin main
```

#### 🗂️ Rules Guide Folder (new source documents)
```bash
git add Rules_Guide_Used/
git commit -m "Add new rule source documents to Rules_Guide_Used"
git push origin main
```

#### 🔷 Frontend — All TypeScript Files
```bash
git add extension/src/extension.ts extension/src/llmClient.ts extension/src/chatbotView.ts
git commit -m "Update extension TypeScript files"
git push origin main
```

#### 📦 Frontend — package.json
```bash
git add extension/package.json
git commit -m "Update extension package.json"
git push origin main
```

#### 📄 Docs — All at Once
```bash
git add docs/INSTALLATION.md docs/DEPLOYMENT_GUIDE.md docs/PROJECT_COMPLETE_SUMMARY.md docs/RULES_SUMMARY.md docs/VIDEO_DEMO_SCRIPT.md
git commit -m "Update documentation"
git push origin main
```

#### 📄 Docs — Individual Files
```bash
# Installation guide only
git add docs/INSTALLATION.md
git commit -m "Update installation guide"
git push origin main

# Project summary only
git add docs/PROJECT_COMPLETE_SUMMARY.md
git commit -m "Update project summary"
git push origin main

# Rules summary only
git add docs/RULES_SUMMARY.md
git commit -m "Update rules summary"
git push origin main

# Video demo script only
git add docs/VIDEO_DEMO_SCRIPT.md
git commit -m "Update video demo script"
git push origin main
```

#### 🏠 README
```bash
git add README.md
git commit -m "Update README"
git push origin main
```

#### ⚙️ GitHub Actions Workflow
```bash
git add .github/workflows/schneider-gate.yml
git commit -m "Update CI/CD workflow"
git push origin main
```

#### 🔒 Gitleaks Config
```bash
git add .gitleaks.toml
git commit -m "Update gitleaks allowlist"
git push origin main
```

#### 🔑 .env.example (NEVER push .env itself!)
```bash
git add server/.env.example
git commit -m "Update environment variable template"
git push origin main
```

---

### 🔄 Full Project Push After Big Update
```bash
cd D:\Schneider_Hackathon

# Stage all changes
git add .

# ✅ Safety check — .env must NOT appear in this list
git status

# Commit
git commit -m "v8.0 - [describe your changes here]"

# Push
git push origin main

# Watch GitHub Actions go green ✅
```

---

### ⚠️ NEVER Push These — Should be in .gitignore
```
server/.env                  ← real API keys
server/venv/                 ← Python virtual environment  
extension/node_modules/      ← npm packages
server/reports/              ← generated PDF reports
__pycache__/                 ← Python cache files
*.pyc                        ← compiled Python
```

### Safety Check Before Every Push (PowerShell)
```powershell
git ls-files | Select-String ".env"
# Must return NOTHING — if it shows .env, stop and fix .gitignore first
```

---

### 📋 Quick Cheat Sheet

| What changed | Command |
|---|---|
| app.py | `git add server/app.py` |
| requirements.txt | `git add server/requirements.txt` |
| rule_extractor.py | `git add rule_extractor.py` |
| Rules JSON | `git add server/Extracted_Rules_From_Pdf.json` |
| All rule JSONs | `git add server/*_rules.json` |
| All TS files | `git add extension/src/*.ts` |
| All docs | `git add docs/` |
| Everything | `git add .` |

Then always finish with:
```bash
git commit -m "your message"
git push origin main
```