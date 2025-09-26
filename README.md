# Applied Machine Learning

A collection of machine learning assignments and projects covering various topics and techniques.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd applied-machine-learning
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

### Running the Assignments

1. Navigate to the specific module folder you want to work on
2. Open the corresponding `.ipynb` file in Jupyter Notebook
3. Run the cells in order to execute the code

### Key Dependencies

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Plotting and visualization
- **seaborn**: Statistical data visualization
- **scikit-learn**: Machine learning algorithms
- **jupyter**: Interactive notebook environment

### Dataset Access

Most datasets are included in the `Datasets/` folder. For the Titanic project (Module 5), the dataset files are located in `Module-5/titanic/`.

### Notes

- All notebooks include data preprocessing and analysis steps
- Some assignments may require additional data downloads (check individual notebook instructions)
- Make sure to run cells in order as later cells may depend on variables defined in earlier cells
