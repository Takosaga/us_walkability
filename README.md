
# DC Walkability Analysis

Open mvp/prototype
<a target="_blank" href="https://colab.research.google.com/github/Takosaga/us_walkability/blob/main/notebooks/mvp.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## Overview
This data science project analyzes walkability metrics across Washington D.C. using Walk Score data. The analysis combines transportation accessibility metrics including walk scores, transit scores, and bike scores to provide insights into urban mobility patterns.

## Features
- Geospatial visualization of walkability metrics using interactive maps
- Statistical analysis of correlations between different mobility scores
- Regression modeling to understand factors influencing Walk Scores
- Analysis of neighborhood amenities (dining, shopping, parks) impact on walkability

## Technical Stack
- Python
- Key Libraries:
 - pandas: Data manipulation and analysis
 - plotly: Interactive geospatial visualizations 
 - seaborn/matplotlib: Statistical visualizations
 - scikit-learn: Machine learning model preparation
 - statsmodels: Statistical modeling

## Key Findings
- Strong correlation between different mobility scores (walk, transit, bike)
- Significant impact of amenities (grocery, shopping, dining) on overall Walk Scores
- Spatial patterns in walkability across DC neighborhoods
- Statistical relationships between infrastructure metrics and walkability

## Future Development
- API integration for real-time data collection:
 - Walk Score API
 - Google Places API for location data
 - Geocoding services
- Cloud database implementation for scalable data storage
- Expanded analysis across multiple cities

## Data Source
Sample data provided by [Walk Score](https://www.walkscore.com/professional/research.php) for Washington D.C.

## Business Applications
- Urban planning and infrastructure development
- Real estate investment analysis
- Comparative city analysis
- Public transportation planning

## Getting Started
1. Clone the repository
2. Install required dependencies: pandas, plotly, seaborn, sklearn, statsmodels
3. Set up necessary API keys for map visualizations
4. Run the Jupyter notebook to reproduce the analysis

## Contact
[Your contact information]

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
