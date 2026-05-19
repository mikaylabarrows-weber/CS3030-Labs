from pathlib import Path

folder = Path("task2_data")
files = sorted(folder.iterdir())

for index, file in enumerate(files, start=1):
    new_name = f"Hawaii_Trip_{index:02}.jpg"
    new_file = folder / new_name
    file.rename(new_file)
    print(f"Renamed: {file.name} -> {new_name}")

print("Finished.")