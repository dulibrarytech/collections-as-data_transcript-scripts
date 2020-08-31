import os
import os.path


def clean_folder(path):
    for transcript in os.scandir(path):
        if transcript.is_file():
            transcript_name = transcript.name[:-4]
            if transcript_name not in page_set:
                remove_path = os.path.join(path, transcript_name + '.xml')
                os.remove(remove_path)
    

image_path = r"C:\Users\alice.tarrant\Downloads\export_job_880492\137454\temp"
page_path = os.path.join(image_path, "page")
alto_path = os.path.join(image_path, "alto")

page_set = set()

for image in os.scandir(image_path):
    if image.is_file():
        page_set.add(image.name[:-4])
        
        
print(len(page_set))

clean_folder(page_path)
clean_folder(alto_path)