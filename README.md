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
| [Task 2](Individual-Contest/Chicken_Counting) | [Chicken Counting](Individual-Contest/Chicken_Counting/Chicken_Counting.ipynb) | [Training Set](Individual-Contest/Chicken_Counting/training_set) | [Solution](Individual-Contest/Chicken_Counting/Solution/Chicken_Counting_Solution.ipynb) | [Validation Set](Individual-Contest/Chicken_Counting/Solution/validation_set) | [Test Set](Individual-Contest/Chicken_Counting/Solution/test_set) |
| [Task 3](Individual-Contest/Concepts) | [Concepts](Individual-Contest/Concepts/Concepts.ipynb) | [Training Set](Individual-Contest/Concepts/training_set) | [Solution](Individual-Contest/Concepts/Solution/Concepts_Solution.ipynb) | [Validation Set](Individual-Contest/Concepts/Solution/validation_set) | [Test Set](Individual-Contest/Concepts/Solution/test_set) |
| [Task 4](Individual-Contest/Restroom) | [Restroom Icon Matching](Individual-Contest/Restroom/Restroom.ipynb) | [Training Set](Individual-Contest/Restroom/training_set) | [Solution](Individual-Contest/Restroom/Solution/Restroom_Solution.ipynb) | [Validation Set](Individual-Contest/Restroom/Solution/validation_set) | [Test Set](Individual-Contest/Restroom/Solution/test_set) |
| [Task 5](Individual-Contest/Antique) | [Antique Painting Authentication](Individual-Contest/Antique/Antique.ipynb) | [Training Set](Individual-Contest/Antique/training_set) | [Solution](Individual-Contest/Antique/Solution/Antique_Solution.ipynb) | [Validation Set](Individual-Contest/Antique/Solution/validation_set) | [Test Set](Individual-Contest/Antique/Solution/test_set) |
| [Task 6](Individual-Contest/Pixel) | [Pixel Efficiency](Individual-Contest/Pixel/Pixel.ipynb) | [Training Set](Individual-Contest/Pixel/training_set) | [Solution](Individual-Contest/Pixel/Solution/Pixel_Solution.ipynb) | - | [Test Set](Individual-Contest/Pixel/Solution/test_set) |

## Downloading Large Data Files

Large datasets and model files have been removed from GitHub due to size limits, but are hosted on [Hugging Face Datasets](https://huggingface.co/datasets/IOAI-official/IOAI2025).

After cloning this repository, run:

```bash
pip install huggingface_hub
python utils/DownloadLargeData.py
```

## Translations of Individual Contest Tasks

Translated versions of the Individual Contest task statements are available for [Day 1](Translations/Individual-Contest-Day1) and [Day 2](Translations/Individual-Contest-Day2).  

These translations were optionally prepared by Team Leaders and provided to their contestants during the contest, alongside the official English version.

## License

This work is released under the **Creative Commons Attribution 4.0 International (CC-BY-4.0)** License.  
You may share and adapt this content as long as proper credit is given and changes are clearly indicated.
