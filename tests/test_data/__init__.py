import os


file_map = {
    "txt": "for_upload.txt",
    "csv": "test.csv"
}


path_to_dir = os.path.dirname(__file__)


choose_file = lambda file_type: os.path.join(path_to_dir, file_map[file_type])
