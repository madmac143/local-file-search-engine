import os

# walks through a directory tree and returns a list of file metadata dictionaries
def scan_directory(directory):
    
    # create empty list to store file information
    file_index = []

    # walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            
            # extract path
            file_path = os.path.join(root, file)
            
            # extract file name and extension
            file_name, extension = os.path.splitext(file)
            
            # strip the "." from beginning of filename
            file_extension = extension.lstrip(".")
            
            # extract file size
            file_size = os.path.getsize(file_path)

            # build dictionary for each directory
            record = {
                "path": file_path,
                "name": file_name,
                "extension": file_extension,
                "size": file_size 
            }

            # create a list of dictionaries 
            file_index.append(record)
    
    # return the list
    return file_index