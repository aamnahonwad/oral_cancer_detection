import os
from PIL import Image, ImageOps
from rembg import remove

# Paths mapped based on the media files found in the current brain directory
# Regions 1-5 (Batch 2)
# Regions 6, 9, 7, 10, 7 (Batch 1)
# Region 8 (Batch 3)

paths = {
    1: r"C:\Users\Aamna\.gemini\antigravity\brain\01e87bf2-e60e-4202-b861-694e24d8ea0b\media__1776784292918.jpg",
    2: r"C:\Users\Aamna\.gemini\antigravity\brain\01e87bf2-e60e-4202-b861-694e24d8ea0b\media__1776784303824.jpg",
    3: r"C:\Users\Aamna\.gemini\antigravity\brain\01e87bf2-e60e-4202-b861-694e24d8ea0b\media__1776784318177.jpg",
    4: r"C:\Users\Aamna\.gemini\antigravity\brain\01e87bf2-e60e-4202-b861-694e24d8ea0b\media__1776784325353.jpg",
    5: r"C:\Users\Aamna\.gemini\antigravity\brain\01e87bf2-e60e-4202-b861-694e24d8ea0b\media__1776784334520.jpg",
    6: r"C:\Users\Aamna\.gemini\antigravity\brain\01e87bf2-e60e-4202-b861-694e24d8ea0b\media__1776783926455.jpg",
    7: r"C:\Users\Aamna\.gemini\antigravity\brain\01e87bf2-e60e-4202-b861-694e24d8ea0b\media__1776784067516.jpg",
    8: r"C:\Users\Aamna\.gemini\antigravity\brain\01e87bf2-e60e-4202-b861-694e24d8ea0b\media__1776784622758.jpg",
    9: r"C:\Users\Aamna\.gemini\antigravity\brain\01e87bf2-e60e-4202-b861-694e24d8ea0b\media__1776783944648.jpg",
    10: r"C:\Users\Aamna\.gemini\antigravity\brain\01e87bf2-e60e-4202-b861-694e24d8ea0b\media__1776784077278.jpg"
}

output_dir = r"c:\Users\Aamna\Downloads\oral_ai\static\images"
os.makedirs(output_dir, exist_ok=True)

print("Starting extraction of the instructed images only...")

for region_num, path in paths.items():
    print(f"Processing Region {region_num}...")
    try:
        if not os.path.exists(path):
            print(f"File not found: {path}")
            continue
            
        with open(path, "rb") as i:
            input_data = i.read()
            output_data = remove(input_data)
            
        out_path = os.path.join(output_dir, f"region{region_num}.png")
        with open(out_path, "wb") as o:
            o.write(output_data)
            
        print(f"Saved: {out_path}")
    except Exception as e:
        print(f"Error on Region {region_num}: {e}")

print("All 10 images processed and placed in static/images!")
