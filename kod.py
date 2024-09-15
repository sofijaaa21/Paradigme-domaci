import os
import fnmatch

# Spisak ekstenzija za uklanjanje
extensions = ['*.bak', '*.log', '*.tmp']

# Pretrazuje se tekuci direktorijum i poddirektorijum
for root, dirs, files in os.walk('.'):
    for ext in extensions:
        for filename in fnmatch.filter(files, ext):
            file_path = os.path.join(root, filename)
            try:
                os.remove(file_path)
                print(f"Uklonjena datoteka: {file_path}")
            except OSError as e:
                print(f"Greska pri uklanjanju {file_path}: {e}")
                
print("Sve pomocne datoteke su uklonjene. :)")
