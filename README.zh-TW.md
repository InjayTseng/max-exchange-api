# 透過 MAX 交易所 API 創建訂單

[English](README.md) | [繁體中文](README.zh-TW.md)

這個專案提供一個方便的工具，透過官方 MAX 交易所 API 在 MAX 交易平台上創建訂單。它旨在簡化訂單創建過程，允許快速有效地進行掛單操作。

## 特色

- 查詢賬戶餘額
- 根據目標價格和價差百分比計算訂單價格
- 計算多個訂單的遞增訂單大小
- 自動下達多個買賣訂單
- 簡單易懂的指令界面
- 下單前的詳細摘要和確認

## 先決條件

在開始之前，請確保您有以下要求：

- 已安裝 Python 3.x
- MAX 交易所賬戶
- MAX 交易所的 API 金鑰和密鑰

## 快速開始

1. 複製或下載 ZIP 並解壓縮。
2. 打開 `max-exchange-api` 資料夾。
3. 在資料夾內創建 `.env` 文件。
4. 將您的 MAX 交易所 API 金鑰和密鑰添加到 `.env` 文件中，如下所示：
    ```env
    MAX_API_KEY=your_api_key_here
    MAX_API_SECRET=your_api_secret_here
    ```
5. 安裝所需的依賴項（如果 `requirements.txt` 中列出了任何）：
    ```bash
    pip install -r requirements.txt
    ```
6. 用 Python 執行腳本：
    ```bash
    python3 main.py
    ```

## 使用教程

腳本將引導您完成以下提示：

1. **餘額查詢**：最初會顯示您的餘額，以確認 API 連接性。
2. **訂單配置**：系統將提示您輸入以下參數：
    - 目標價格
    - 價差百分比
    - 訂單總數
    - 基礎訂單大小
    - 訂單大小遞增百分比
    - 交易對（例如 'btcusd'）
3. **訂單審核**：將為您展示打算下的訂單摘要以供審核：
    - 交易對
    - 訂單總數
    - 總買入價值
    - 總賣出價值
4. **確認**：確認是否繼續下單。

確認後，腳本將自動開始按照配置下訂單。

## 參考
MAX 交易所 API 文檔：https://max.maicoin.com/documents/api_list/v2

## 貢獻

歡迎為此專案貢獻！如果您有建議或改進，請 fork 存儲庫並創建一個 pull request，或者開一個帶有 "enhancement" 標籤的問題。別忘了給這個專案一個星星！謝謝！

如果您想支持我的工作：

- **ETH**：`0x99141283469FF129EfC3139F963C511029aC5B66`
- **LOOT**：`0x99141283469FF129EfC3139F963C511029aC5B66`
- **ERC20**：`0x99141283469FF129EfC3139F963C511029aC5B66`
- **透過 MAX 交易所推薦代碼註冊**：[https://max.maicoin.com/signup?r=a4e9431a](https://max.maicoin.com/signup?r=a4e9431a)

## 感謝

這個專案得以實現，要感謝以下資源：

- 最初的 API 包裝器由 [kulisu](https://github.com/kulisu/max-exchange-api-python3) 提供。
- 從 [OpenAI 的 ChatGPT](https://openai.com/chatgpt) 獲得的指導和協助。

## 授權

此專案在 MIT 授權下提供 — 詳情請見 [LICENSE](LICENSE) 文件。
