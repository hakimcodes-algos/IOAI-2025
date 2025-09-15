# International Olympiad in Artificial Intelligence (IOAI 2025, Beijing, China)

## About IOAI 2025

The [**2nd International Olympiad in Artificial Intelligence (IOAI 2025)**](https://ioai-official.org/china-2025/) took place in **Beijing, China**, from **August 2 to 9, 2025**, hosted by **Beijing National Day School (BNDS)** under the patronage of **UNESCO**.

- **Contest Rules**: Full rules encompassing the Individual, Team, and GAITE contests are available [here](https://ioai-official.org/china-2025/2025-contest-rules/).  
- **Syllabus**: The official syllabus outlining the AI topics contestants should master is available [here](https://ioai-official.org/china-2025/syllabus-2025/).  
- **Team Challenge**: Details of the “Future Factory” robotics challenge are described [here](https://ioai-official.org/team-challenge/).  
- **Results**: Official medal tables and country results are published [here](https://ioai-official.org/china-2025/results-2025/).  

## Highlights

- **Individual Contest**: A two-day on-site competition preceded by an at-home (practice) round, focused on machine learning, NLP, computer vision, etc.  
- **Team Challenge**: The “Future Factory” robotics-oriented challenge, with a simulated stage and real-robot final using Galbot robots.  
- **GAITE Contest**: A simplified, hint-enabled variant of the Individual Contest, designed for broader accessibility.  

## Individual Contest Tasks

| Task Folder | Statement | Training Data | Reference Solution | Validation Data | Test Data |
|-------------|-----------|---------------|------------------|----------------|-----------|
| [Task 1](Individual-Contest/Radar) | [Radar](Individual-Contest/Radar/Radar.ipynb) | [Training Set](Individual-Contest/Radar/training_set) | [Solution](Individual-Contest/Radar/Solution/Radar_Solution.ipynb) | [Validation Set](Individual-Contest/Radar/Solution/validation_set) | [Test Set](Individual-Contest/Radar/Solution/test_set) |
| [Task 2](Individual-Contest/Chicken_Counting) | [Chicken Counting](Individual-Contest/Chicken_Counting/Chicken_Counting.ipynb) | [Training Set](Individual-Contest/Chicken_Counting/training_set) | [Solution](Individual-Contest/Chicken_Counting/Chicken_Counting_Solution.ipynb) | [Validation Set](Individual-Contest/Chicken_Counting/Solution/validation_set) | [Test Set](Individual-Contest/Chicken_Counting/Solution/test_set) |
| [Task 3](Individual-Contest/Concepts) | [Concepts](Individual-Contest/Concepts/Concepts.ipynb) | [Training Set](https://huggingface.co/datasets/IOAI-official/ioai2025-onsite-concepts-train) | [Solution](Individual-Contest/Concepts/Concepts_Solution.ipynb) | [Validation Set](https://huggingface.co/datasets/IOAI-official/ioai2025-onsite-concepts-validation) | [Test Set](https://huggingface.co/datasets/IOAI-official/ioai2025-onsite-concepts-test) |
| [Task 4](Individual-Contest/Restroom) | [Restroom Icon Matching](Individual-Contest/Restroom/Restroom.ipynb) | [Training Set](Individual-Contest/Restroom/training_set) | [Solution](Individual-Contest/Restroom/Solution/Restroom_Solution.ipynb) | [Validation Set](Individual-Contest/Restroom/Solution/validation_set) | [Test Set](Individual-Contest/Restroom/Solution/test_set) |
| [Task 5](Individual-Contest/Antique) | [Antique Painting Authentication](Individual-Contest/Antique/Antique.ipynb) | [Training Set](Individual-Contest/Antique/training_set) | [Solution](Individual-Contest/Antique/Solution/Antique_Solution.ipynb) | [Validation Set](Individual-Contest/Antique/Solution/validation_set) | [Test Set](Individual-Contest/Antique/Solution/test_set) |
| [Task 6](Individual-Contest/Pixel) | [Pixel Efficiency](Individual-Contest/Pixel/Pixel.ipynb) | [Training Set](https://huggingface.co/datasets/IOAI-official/IOAI-2025-Pixel-train) | [Solution](Individual-Contest/Pixel/Pixel_Solution.ipynb) | [Validation Set](https://huggingface.co/datasets/IOAI-official/IOAI-2025-Pixel-ref) | [Test Set](https://huggingface.co/datasets/IOAI-official/IOAI-2025-Pixel-test) |


## Environment Setup

The competition environment uses Python 3.12.7 and includes a comprehensive set of dependencies listed in [requirements.txt](requirements.txt). The contestants were not allowed to install other external libraries, so these were the only packages they could use. Below are instructions for setting up the environment using different package managers.

### Using Conda (Recommended)

```bash
# Create and activate a new conda environment
conda create -n ioai-2025 python=3.12.7
conda activate ioai-2025

# Update pip and install dependencies
pip install --upgrade pip
pip install --no-deps -r requirements.txt
```

### Using venv

```bash
# Linux/macOS
python3.12 -m venv ioai-2025
source ioai-2025/bin/activate

# Windows
python -m venv ioai-2025
.\ioai-2025\Scripts\activate

# Install dependencies (all platforms)
pip install --upgrade pip
pip install --no-deps -r requirements.txt
```

### Using pyenv

```bash
# Install Python 3.12.7
pyenv install 3.12.7
pyenv local 3.12.7

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.\.venv\Scripts\activate   # Windows

# Install dependencies
pip install --upgrade pip
pip install --no-deps -r requirements.txt
```

> **Note**: The `--no-deps` flag is required to ensure exact package versions match the competition environment.

## Translations of Individual Contest Tasks

Translated versions of the Individual Contest task statements are available for [Day 1](Translations/Individual-Contest-Day1) and [Day 2](Translations/Individual-Contest-Day2).  

These translations were optionally prepared by Team Leaders and provided to their contestants during the contest, alongside the official English version.

## License

This work is released under the **Creative Commons Attribution 4.0 International (CC-BY-4.0)** License.  
You may share and adapt this content as long as proper credit is given and changes are clearly indicated.
