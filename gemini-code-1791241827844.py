print("=" * 70)
print(PROJECT_NAME)
print("=" * 70)

print("\nUpload ONLY the internship task PDF files.\n")

uploaded_files = files.upload()

for filename in uploaded_files:
    if filename.lower().endswith(".pdf"):
        source = Path(filename)
        destination = DATA_DIR / source.name
        source.rename(destination)
        print(f"✓ Added: {filename}")
    else:
        print(f"⚠ Skipped non-PDF file: {filename}")