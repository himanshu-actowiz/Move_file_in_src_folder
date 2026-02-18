
import os

source_path = "C:/Users/hemanshu.marwadi/Desktop/OS_MAKE_DIR"
destination_path = "C:/Users/hemanshu.marwadi/Desktop/2027_year_folder"

def move_file(src_path,dst_path):

    for folder in os.listdir(src_path):# folder
        # if folder == '2026-02-22':
        src_folder_path = os.path.join(src_path,folder)
        year_change = folder.replace("2026", "2027")
        print(year_change)
        print(src_path)
        print(folder)
        print(src_folder_path)
        dest_folder=os.path.join(dst_path,year_change)

        for src_folder_file in os.listdir(src_folder_path):# files
            print(src_folder_file,src_folder_path)
            src_file_path = os.path.join(src_folder_path,src_folder_file)
            dest_file_path=os.path.join(dest_folder,src_folder_file)

            os.rename(src_file_path,dest_file_path)
            
def remove_file(destination_path):
    for i in os.listdir(destination_path):
        remove_file_path = os.path.join(destination_path,i)
        for j in os.listdir(remove_file_path):
            remove_path = os.path.join(remove_file_path,j)
            
            if remove_path.endswith(".js") or remove_path.endswith(".java"):
                os.remove(remove_path)
    
            
move_folder_file = move_file(source_path,destination_path)
remove_file(destination_path)


