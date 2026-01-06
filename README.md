# SofiAIPM – Accounts Receivable Risk Tool

A LangChain-based financial analysis tool for evaluating **Accounts Receivable / Trade Receivables**
to identify potential collection risk and aggressive revenue recognition.

---

## 📌 Overview

This tool analyzes a company’s accounts receivable health using simple but effective checks such as:
- Receivables growth over time
- Receivables-to-revenue ratio thresholds
- Long-duration receivables ageing risk

It is designed to be used as a **tool component** within the Sofi AI Portfolio Manager system.

---

## ✨ Features

- 📊 Detects receivable-related financial red flags  
- 🧠 Built using LangChain `StructuredTool`  
- ✅ Uses Pydantic for input validation  
- 📄 Returns human-readable string output for LLM reasoning  

---

## 🛠️ Inputs

- `receivables` – Receivables over multiple years  
- `revenue` – Revenue over the same period  
- `ageing_long_term_percentage` – % of receivables older than 90 days  

---

## 📤 Output

- A **string summary** highlighting warnings and healthy indicators  
- Compatible with LangChain / LangGraph agents  

---

## 📂 Project Structure

accounts-receivable-tool/
├── tool/
│ └── accounts_receivable_tool.py
├── .gitignore
├── requirements.txt
└── README.md

yaml
Copy code

---

## 🚀 Intended Use

Part of the **Sofi AI Portfolio Manager** workflow:

Tools → Agents → Orchestration → Frontend

nginx
Copy code

This repository focuses only on the **tool layer**.