# Playwright Python Web UI 自动化测试框架

这是一个基于 Python 和 Playwright 构建的可扩展、易维护的 Web UI 自动化测试框架。它采用了页面对象模型 (POM) 设计模式，并通过数据库集成支持数据驱动测试 (DDT)。

## 🚀 特性

*   **页面对象模型 (POM)**：将测试逻辑与页面细节分离，提高可维护性。
*   **数据驱动测试 (DDT)**：从数据库（支持 MySQL）动态获取测试数据。
*   **平台化思维**：架构设计旨在未来轻松集成其他类型的测试（API、移动端/Appium）。
*   **自动等待与高可靠性**：利用 Playwright 内置的自动等待机制。
*   **智能断言**：`BasePage` 内置断言辅助函数（如 `assert_text_contains`），提供更稳健的验证。
*   **测试报告**：集成 Allure 生成全面的测试报告。
*   **CI/CD**：提供现成的 `Jenkinsfile`。
*   **代码生成**：提供辅助脚本以轻松录制测试。

## 📂 项目结构

```
.
├── config/                 # 配置（环境变量、设置）
├── core/                   # 核心框架逻辑（可复用组件）
│   ├── base_page.py        # 基础页面对象，包含通用封装
│   ├── database/           # 数据库连接器（MySQL 和 Mock）
│   └── utils/              # 工具类（日志、辅助函数）
├── tests/                  # 测试实现
│   ├── web/                # Web UI 测试
│   │   ├── pages/          # 页面对象
│   │   └── common/         # 通用 Web 测试
│   │       └── test_login.py # 示例测试
│   └── api/                # 未来的 API 测试
├── scripts/                # 辅助脚本（例如：代码生成封装）
├── requirements.txt        # Python 依赖
├── pytest.ini              # Pytest 配置
└── Jenkinsfile             # CI 流水线定义
```

## 🛠️ 安装与设置

1.  **安装 Python 3.8+**
2.  **安装依赖**：
    ```bash
    pip install -r requirements.txt
    playwright install chromium
    ```
3.  **配置**：
    - 将 `.env.example` 复制为 `.env`（如果需要，请创建一个），或者直接设置环境变量。
    - 默认设置位于 `config/settings.py`。

## 🏃 运行测试

### 1. 基础运行
```bash
pytest
```

### 2. 指定浏览器运行（有头模式）
```bash
pytest --headed --browser chromium
```

### 3. 生成报告
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

## 🗄️ 数据库集成

本框架支持从 MySQL 获取测试数据。
- **真实数据库**：在 `.env` 中更新 `DB_HOST`、`DB_USER` 等，并设置 `USE_MOCK_DB=false`。
- **Mock 数据库**：本地开发且无数据库时的默认设置。设置 `USE_MOCK_DB=true`。

## 🎥 录制测试

要快速为新页面生成代码，请运行：
```bash
python3 scripts/generate_test.py --url https://example.com
```

## 🏗️ 扩展平台

`core/` 目录包含与具体测试实现无关的逻辑。
- **添加 API 测试**：创建 `tests/api/` 并使用 `requests` 或 Playwright 的 `APIRequestContext`，复用 `core/utils/logger.py` 和 `config/settings.py`。
- **添加移动端测试**：在新的 `tests/mobile/` 目录中集成 `Appium-Python-Client`。

## 🤝 贡献指南

1.  在 `tests/web/pages/` 中创建一个新的页面对象。
2.  在 `tests/web/` 中编写测试。
3.  确保测试在本地通过。
