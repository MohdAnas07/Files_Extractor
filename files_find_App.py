import os,shutil

def files_finder(file_extension,folder_path):
     files = []
     for file in os.listdir(folder_path):
          for extension in file_extension:
               if file.endswith(extension):
                    files.append(file)
     return files


folder_path = input("Enter the folder path : ")

extension = {
               'Audio_extension':('.mp3','.m4a','.wav','.flac'),
               'Vedios_extension':('.mp4','.mkv','.MKV','.flv','.mpeg'),
               'Documents_extension':('.doc','.pdf','.txt'),
     }

for extension_type,tuple_file in extension.items():
     folder_name = extension_type.split('_')[0]+'files'
     new_folder_path = os.path.join(folder_path,folder_name)
     os.mkdir(new_folder_path)
     
     for item in files_finder(tuple_file ,folder_path):
          item_path = os.path.join(folder_path,item)
          new_item_path = os.path.join(new_folder_path,item)
          shutil.move(item_path,new_item_path)
          
                    
     
