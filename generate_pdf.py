from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Heart Disease Detection Project Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, text):
        self.set_font('Arial', '', 11)
        # Replacing unicode dashes/apostrophes just in case
        text = text.replace('—', '-').replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
        self.multi_cell(0, 8, text)
        self.ln()

workflow_text = """The project follows a linear data science pipeline. This means we process raw data step-by-step to the final application:
1. Data Loading & EDA: The raw CSV file is loaded, and exploratory graphs/plots are created.
2. Preprocessing (Data Cleaning): Missing values are imputed, numerical features like age are scaled, and categorical classes are encoded. The SMOTE technique is applied to balance the target classes (Disease/No-Disease).
3. Model Training: Five different algorithms are trained: Logistic Regression, Random Forest, XGBoost, Decision Tree, and SVM.
4. Evaluation & Tuning: The best performing model is selected based on key metrics like F1-Score, fine-tuned using GridSearchCV, and exported as 'best_model.pkl'.
5. Prediction UI (Streamlit): A frontend web interface is developed where users can input testing attributes to predict the likelihood of heart disease."""

models_text = """Five different Machine Learning models were utilized in this project:
- Logistic Regression: A simple and fast baseline model that provides the probability of the disease.
- Random Forest: An ensemble model consisting of multiple decision trees, naturally robust against outliers.
- XGBoost: An extreme gradient boosting algorithm. It generally provides the highest accuracy when identifying complex patterns.
- SVM (Support Vector Machine): Useful as a high-dimensional data separator.
- Decision Tree: A fundamental rule-based machine learning algorithm.

Why were these chosen? -> We compared all these models using Cross Validation so that the one with the best generalization on unseen tabular data could be selected as the core engine for the final Streamlit deployment!"""

dataset_text = """Dataset: UCI Cleveland Heart Disease (Kaggle)
It contains medical data for 303 patients across 14 attributes:
1. age: Age in years
2. sex: 1 = Male, 0 = Female
3. cp (Chest Pain Type): 0 = Typical angina, 1 = Atypical angina, 2 = Non-anginal pain, 3 = Asymptomatic
4. trestbps: Resting blood pressure (in mm Hg)
5. chol: Serum cholesterol level in mg/dl (levels over 200 may pose a risk)
6. fbs: Fasting blood sugar > 120 mg/dl indicates presence of diabetes (1 = Yes, 0 = No)
7. restecg: Resting electrocardiographic results (0 = Normal, 1 = Abnormal, 2 = High Risk/Hypertrophy)
8. thalach: Maximum heart rate achieved during exercise
9. exang: Exercise-induced angina present (1 = Yes, 0 = No)
10. oldpeak: ST depression induced by exercise relative to rest
11. slope: The structural slope of the peak exercise ST segment
12. ca: Number of major blood vessels (0-3) colored by fluoroscopy
13. thal: Thalassemia blood disorder (1 = Normal, 2 = Fixed defect, 3 = Reversible defect)
14. target (Diagnosis): 1 = Heart Disease Detected (Positive), 0 = No Disease (Negative/Healthy)"""

pdf = PDF()
pdf.add_page()
pdf.chapter_title('1. Project Step-by-Step Workflow')
pdf.chapter_body(workflow_text)
pdf.chapter_title('2. Models Explained (Why Which Model?)')
pdf.chapter_body(models_text)
pdf.add_page()
pdf.chapter_title('3. Detailed Dataset Information (14 Features)')
pdf.chapter_body(dataset_text)
pdf.output('Heart_Disease_Project_Report.pdf')
print("PDF Generated successfully as Heart_Disease_Project_Report.pdf")
