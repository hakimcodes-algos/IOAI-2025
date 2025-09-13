import os
from huggingface_hub import hf_hub_download

HF_REPO = "IOAI-official/IOAI2025"

FILES = [
    "Individual-Contest/Chicken_Counting/Solution/test_set/data-00000-of-00001.arrow",
    "Individual-Contest/Chicken_Counting/Solution/test_set/labels/data-00000-of-00001.arrow",
    "Individual-Contest/Chicken_Counting/Solution/validation_set/data-00000-of-00001.arrow",
    "Individual-Contest/Chicken_Counting/Solution/validation_set/labels/data-00000-of-00001.arrow",
    "Individual-Contest/Chicken_Counting/training_set/train/data-00000-of-00001.arrow",
    "Individual-Contest/Concepts/Solution/test_set/test/data-00000-of-00001.arrow",
    "Individual-Contest/Concepts/Solution/validation_set/test/data-00000-of-00001.arrow",
    "Individual-Contest/Concepts/training_set/hint_descriptions/train/data-00000-of-00001.arrow",
    "Individual-Contest/Concepts/training_set/train/train/data-00000-of-00001.arrow",
    "Individual-Contest/Pixel/Solution/Scoring/reference_dataset/test/data-00000-of-00001.arrow",
    "Individual-Contest/Pixel/Solution/test_set/test/data-00000-of-00001.arrow",
    "Individual-Contest/Pixel/clip-vit-large-patch14/model.safetensors",
    "Individual-Contest/Pixel/training_set/train/data-00000-of-00001.arrow",
    "Individual-Contest/Restroom/CLIP/ViT-B-32.pt",
]

def fetch_file(repo_id, filename, local_path):
    if os.path.exists(local_path):
        print(f"Already exists, skipping: {local_path}")
        return
    
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    print(f"Downloading {filename} → {local_path}")
    cached_path = hf_hub_download(
        repo_id=repo_id,
        filename=filename,
        repo_type="dataset"   # 👈 force dataset repo
    )
    
    try:
        os.link(cached_path, local_path)  # hardlink, no extra disk use
    except OSError:
        os.replace(cached_path, local_path)  # fallback: move file

def main():
    for f in FILES:
        fetch_file(HF_REPO, f, f)

if __name__ == "__main__":
    main()

