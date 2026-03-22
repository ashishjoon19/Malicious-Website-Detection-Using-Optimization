# 🔐 Malicious Website Detection using Optimization Algorithms

A machine learning-based system for detecting malicious and phishing websites using advanced optimization techniques for feature selection and model tuning.

---

## 🚀 Overview

This project focuses on building a **multi-class classification system** to identify malicious URLs using the **CIC URL 2016 dataset**. The system leverages **metaheuristic optimization algorithms** to improve both feature selection and model performance.

---

## 🧠 Key Highlights

- 📊 Multi-class classification of URLs (benign, phishing, malware, etc.)
- ⚙️ Feature selection using **Whale Optimization Algorithm (WOA)**
- 🚀 Model optimization using **Spider Monkey Optimization (SMO)**
- 🌲 Final model: **CatBoost Classifier**
- 📉 Reduced feature space to **42 optimal features**
- 🎯 Achieved **97.9% accuracy** after optimization
- 📈 Baseline model accuracy: **95.1%**

---

## 📂 Dataset

- **CIC URL 2016 Dataset**
- 🔗 https://www.unb.ca/cic/datasets/url-2016.html

The dataset contains labeled URLs with multiple classes such as:
- Benign
- Phishing
- Malware
- Spam
- Defacement

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- CatBoost
- Metaheuristic Algorithms:
  - Whale Optimization Algorithm (WOA)
  - Spider Monkey Optimization (SMO)

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Removed irrelevant features
- Encoded categorical data
- Normalized feature values

### 2. Feature Selection (WOA)
- Applied Whale Optimization Algorithm
- Reduced features to **42 most relevant ones**
- Improved efficiency and reduced noise

### 3. Model Training (CatBoost)
- Trained baseline CatBoost model
- Evaluated using accuracy, precision, recall, F1-score

### 4. Optimization (SMO)
- Tuned hyperparameters:
  - iterations
  - depth
  - learning rate
  - L2 regularization
- Achieved improved performance over baseline

---

## 📊 Results

| Model                      | Accuracy |
|---------------------------|----------|
| CatBoost (Baseline)       | 95.1%    |
| CatBoost + SMO (Optimized)| 97.9%    |

- Strong performance across all classes
- Balanced precision and recall
- Reduced false positives

---

## 📌 Key Learnings

- Metaheuristic optimization significantly improves model performance
- Feature selection plays a critical role in classification accuracy
- CatBoost performs well on structured tabular data

---

## 👥 Contributors

- Ashish Joon (CatBoost + SMO + WOA)
- Team Members (Optimization Variants for Comparison)

---

## 📅 Timeline

- Project Completion: Jan 2026
- Research Paper Submission: Jan 2026

---

## 📎 How to Run

```bash
pip install -r requirements.txt
