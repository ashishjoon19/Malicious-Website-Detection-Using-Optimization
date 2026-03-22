# 🔐 Malicious Website Detection using Optimization Algorithms

A research-based machine learning project focused on detecting malicious URLs using advanced feature selection and optimization techniques.

---

## 🚀 Overview

With the rise of phishing, malware, and fraudulent websites, traditional detection systems fail to adapt to evolving threats. This project presents a **hybrid machine learning framework** that combines:

- Metaheuristic-based feature selection
- Optimized tree-based classification

The system performs **multi-class classification** of URLs into:
- Benign
- Phishing
- Malware
- Spam
- Defacement

---

## 📊 Dataset

- **CIC URL 2016 Dataset**
- ~36,000+ URLs with 79 features  
- 🔗 https://www.unb.ca/cic/datasets/url-2016.html

As mentioned in the project synopsis, the dataset supports both binary and multi-class classification tasks. :contentReference[oaicite:0]{index=0}

---

## 🧠 My Contribution

- Implemented **Whale Optimization Algorithm (WOA)** for feature selection  
- Reduced feature space from high-dimensional data to **42 optimal features**  
- Built baseline **CatBoost classifier**  
- Applied **Spider Monkey Optimization (SMO)** for hyperparameter tuning  
- Improved model performance significantly using optimization techniques  

---

## ⚙️ Methodology

### 1. Data Preprocessing
- Data cleaning and normalization  
- Train-test split (80:20)  

### 2. Feature Selection (WOA)
- Selected most relevant features  
- Reduced dimensionality and improved efficiency  

### 3. Model Training
- Used **CatBoost classifier** for multi-class classification  

### 4. Optimization (SMO)
- Tuned:
  - iterations
  - depth
  - learning rate
  - L2 regularization  

---

## 📈 Results

| Model                      | Accuracy |
|---------------------------|----------|
| CatBoost (Baseline)       | 95.11%   |
| CatBoost + SMO (Optimized)| 97.90%   |

### Key Outcomes:
- Feature reduction to **42 features**
- Improved classification performance
- Balanced precision, recall, and F1-score
- Reduced false positives

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

## 👥 Team Work

This was a group project where different optimization techniques were explored:

- Ashish Joon → CatBoost + SMO + WOA  
- Others → AdaBoost, BAT, Cuckoo Search, CSA, FHOA  

---

## 📅 Timeline

- Project Completion: Jan 2026  
- Research Paper: Jan 2026  

---

## 📎 How to Run

```bash
pip install -r requirements.txt
