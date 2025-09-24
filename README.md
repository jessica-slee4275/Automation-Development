
# PlayStation SDET Automation Template (PyTest + Selenium)

Production-ready template for **Agile QE** style UI automation:
- **PyTest** test runner with **fixtures**, **HTML report**, **parallel runs**
- **Selenium WebDriver** + **webdriver-manager** (no manual driver setup)
- **Page Object Model (POM)** with reusable waits & logger
- **ENV-based config** (BASE_URL, BROWSER, HEADLESS)
- **CI examples**: GitHub Actions & Jenkins Pipeline
- **Artifacts**: HTML report (`pytest-html`) archived in CI

> Default demo site: https://www.saucedemo.com  (public test app)
> You can switch to any site via `BASE_URL` env var.

---

## 🚀 Quick Start

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -n auto --html=report.html --self-contained-html
```

### Run headless / switch browser
```bash
export HEADLESS=1
export BROWSER=chrome   # chrome | firefox
export BASE_URL=https://www.saucedemo.com
pytest -n auto --html=report.html --self-contained-html -q
```

### Select tests
```bash
pytest tests/test_login.py -q
pytest -k "cart or checkout" -q
```

### Common env vars
- `BASE_URL` (default: `https://www.saucedemo.com`)
- `BROWSER`  (default: `chrome`)
- `HEADLESS` (`1` to enable, default off)
- `CI`       (set automatically in CI to force headless)

---

## 🧱 Project Structure

```
ps-sdet-automation-template/
├─ .github/workflows/ci.yml        # GitHub Actions: install → run → upload report
├─ Jenkinsfile                     # Jenkins Pipeline: same flow
├─ pytest.ini                      # PyTest defaults
├─ requirements.txt
├─ src/
│  ├─ pages/                       # Page Object Model
│  │  ├─ base_page.py
│  │  ├─ login_page.py
│  │  ├─ inventory_page.py
│  │  ├─ cart_page.py
│  │  └─ checkout_page.py
│  └─ utils/
│     ├─ config.py
│     ├─ wait.py
│     └─ logger.py
├─ tests/
│  ├─ test_login.py
│  ├─ test_add_to_cart.py
│  └─ test_checkout.py
└─ conftest.py                     # drivers, fixtures, screenshots on failure
```

---

## 🧪 What the demo tests do (SauceDemo)

- **Login**: standard credentials (`standard_user` / `secret_sauce`)
- **Add to Cart**: add/remove items, verify cart badge & content
- **Checkout**: fill forms, finish order, assert completion page

---

## 🧰 Useful Commands

- Run with debug logs:
  ```bash
  pytest -o log_cli=true -o log_cli_level=INFO
  ```
- Re-run failed tests only:
  ```bash
  pytest --last-failed
  ```

---

## 🏗 CI Examples

### GitHub Actions
See [.github/workflows/ci.yml](.github/workflows/ci.yml)

### Jenkins
See [Jenkinsfile](Jenkinsfile)

Both:
- Install deps
- Run tests headless
- Upload/Archive `report.html`

---

## 🧭 Extending to Your App

- Add new page objects in `src/pages`
- Create/selectors & small, stable methods
- Compose business flows in tests with fixtures
- Use `wait.until_visible()` instead of raw sleeps

---

## 📋 License
MIT — use freely for interviews & production kickstarts.
