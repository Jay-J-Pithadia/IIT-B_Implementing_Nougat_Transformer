import sys
import os

if len(sys.argv) > 1:
    pdf_path = sys.argv[1]
    output_dir = sys.argv[2]
    nougat_cmd = f"nougat --markdown --out '{output_dir}'"
    
    for pdf in os.listdir(pdf_path):
      if pdf.endswith(".pdf"):
        os.system(f"{nougat_cmd} pdf {pdf_path}/{pdf}")
      else:
        print("No pdf files found.")

    for mmd in os.listdir(output_dir):
      if mmd.endswith(".mmd"):
        print(f"\n\n\n\nOutput for file: {mmd}\n")
        with open(f"{output_dir}/{mmd}", "r", encoding="utf-8") as markdown_file:
              markdown_content = markdown_file.read()
              print(markdown_content)
        print("\n\n\n\n\n")
      else:
        print("No markdown(.mmd) files found.")
