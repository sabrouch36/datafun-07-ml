# 📈 datafun-07-ml: Machine Learning Project

## 🎯 Project Purpose

This project introduces basic machine learning (ML) concepts using Python.  
We explore **supervised learning** with a focus on **simple linear regression** to build a predictive model using real-world data.  

We:
- Import and clean data
- Train a model (fit a best-fit line)
- Make predictions
- Visualize the results
- Draw insights

---

## 🛠️ Environment Setup

We use a **virtual environment** named `.venv` for package management.

### ✅ Create and Activate Virtual Environment (Windows)

```bash
py -3.12 -m venv .venv
.venv\Scripts\activate

🔄 Git Commands Used

git init
git add .
git commit -m "Initial setup for ML project"
git remote add origin https://github.com/YOUR_USERNAME/datafun-07-ml.git
git push -u origin main

🧠 How to Run the Project
Activate your environment:

.venv\Scripts\activate

datafun-07-ml/
│
├── sabri_ml.ipynb #  Main notebook: All parts (1–5)
├── nyc.csv #  Dataset: NYC January temperatures
├── README.md #  Project overview and instructions
├── requirements.txt #  Python package dependencies
│
├── 15_02_knn_digits.ipynb #  Sample k-NN project from Chapter 15
├── 15_04_linear_regression.ipynb # Sample Linear Regression from textbook
│
├── account.py # 🧾OOP class example (Chapter 10)
├── commissionemployee.py #  OOP class example: Employee commission
├── salariedcommissionemployee.py #  OOP class: Inheritance example
├── deck2.py #  Card simulation from OOP chapters
│
├── .gitignore #  Files excluded from Git tracking
└── .venv/ #  Virtual environment folder



---

## 📚 Project Parts

### ✅ Part 1 – Chart a Straight Line
- Created a simple Celsius → Fahrenheit conversion model
- Visualized the relationship using `matplotlib`

### ✅ Part 2 – Prediction with `scipy.stats.linregress`
- Loaded NYC temperature data from CSV
- Built and visualized a regression model using `scipy`
- Predicted future value for the year **2024**

### ✅ Part 3 – Prediction with `scikit-learn`
- Reused NYC dataset
- Split data into training and testing sets
- Built a linear regression model using `LinearRegression`
- Predicted for 2024 and compared with Part 2

### ✅ Part 4 – Insights and Comparison
- Compared `scipy` vs `sklearn` in terms of:
  - Accuracy
  - Use cases
  - Flexibility
- Summarized findings in markdown

### ✅ Part 5 – Bonus: California Housing
- Loaded California Housing dataset
- Built a multivariate linear regression model
- Evaluated using **Mean Squared Error** and **R² Score**
- Visualized actual vs predicted values

---

## 🧪 Technologies Used

- Python
- Jupyter Notebook
- pandas, numpy, matplotlib, seaborn
- scikit-learn
- scipy

---

## 📈 Sample Visualization

> _(Optional: You can add an image here if you saved any plots)_

```markdown
![Regression Plot](images/part5_actual_vs_predicted.png)


📝 Notes
All work follows the structure and objectives of Chapter 10.16 and Chapter 15.4 of the course textbook.

This notebook is structured for readability, reproducibility, and clear evaluation of each modeling approach.

📬 Contact
For questions or collaboration opportunities, feel free to reach out via GitHub.



