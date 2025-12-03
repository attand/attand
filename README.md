# Playwright Python Web UI Automation Framework

This is a scalable, maintainable Web UI automation framework built with Python and Playwright. It uses the Page Object Model (POM) design pattern and supports Data-Driven Testing (DDT) via Database integration.

## 🚀 Features

*   **Page Object Model (POM)**: Separates test logic from page details for better maintainability.
*   **Data-Driven Testing (DDT)**: Fetches test data dynamically from a Database (MySQL support included).
*   **Platform Ready**: Architecture is designed to easily plug in other types of testing (API, Mobile/Appium) in the future.
*   **Auto-Wait & Reliability**: Leverages Playwright's built-in auto-waiting mechanisms.
*   **Reporting**: Integrated with Allure for comprehensive test reports.
*   **CI/CD**: Ready-to-use `Jenkinsfile`.
*   **Code Generation**: Helper scripts to record tests easily.

## 📂 Project Structure

```
.
├── config/                 # Configuration (Environment variables, settings)
├── core/                   # Core Framework Logic (Reusable components)
│   ├── base_page.py        # Base Page Object with common wrappers
│   ├── database/           # Database connectors (MySQL & Mock)
│   └── utils/              # Utilities (Logger, Helpers)
├── tests/                  # Test Implementations
│   ├── web/                # Web UI Tests
│   │   ├── pages/          # Page Objects
│   │   └── test_login.py   # Example Test
│   └── api/                # Future API Tests
├── scripts/                # Helper scripts (e.g., codegen wrapper)
├── requirements.txt        # Python dependencies
├── pytest.ini              # Pytest configuration
└── Jenkinsfile             # CI Pipeline definition
```

## 🛠️ Setup

1.  **Install Python 3.8+**
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    playwright install chromium
    ```
3.  **Configuration**:
    - Copy `.env.example` to `.env` (create one if needed) or set environment variables directly.
    - Default settings are in `config/settings.py`.

## 🏃 Running Tests

### 1. Basic Run
```bash
pytest
```

### 2. Run with specific browser (headed)
```bash
pytest --headed --browser chromium
```

### 3. Generate Report
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

## 🗄️ Database Integration

The framework supports fetching test data from MySQL.
- **Real DB**: Update `DB_HOST`, `DB_USER`, etc., in `.env` and set `USE_MOCK_DB=false`.
- **Mock DB**: Default for local dev without a DB. Set `USE_MOCK_DB=true`.

## 🎥 Recording Tests

To quickly generate code for a new page:
```bash
python3 scripts/generate_test.py --url https://example.com
```

## 🏗️ Expanding the Platform

The `core/` directory contains logic that is agnostic of the specific test implementation.
- To add **API Testing**: Create `tests/api/` and use `requests` or Playwright's `APIRequestContext`, reusing `core/utils/logger.py` and `config/settings.py`.
- To add **Mobile Testing**: Integrate `Appium-Python-Client` in a new `tests/mobile/` directory.

## 🤝 Contributing

1.  Create a new Page Object in `tests/web/pages/`.
2.  Write a test in `tests/web/`.
3.  Ensure it passes locally.
