import os
import json


class File:
    def file_read(filename):
        if os.stat('package/data/' + filename + '.json').st_size == 0:
            print(filename + ".json file is empty!")
            exit(0)
        elif os.stat('package/data/' + filename + '.json').st_size != 0:
            with open('package/data/' + filename + '.json', encoding=('UTF-8')) as f:
                file = json.load(f)
        return file


    def file_read_create_if_not_found(filename):
        if not os.path.isfile('package/data/' + filename + '.json'):
            print(filename, ".json file not found! Creating one now...")
            File.file_write(filename, {})
            with open('package/data/' + filename + '.json', encoding=('UTF-8')) as f:
                file = json.load(f)
        else:
            with open('package/data/' + filename + '.json', encoding=('UTF-8')) as f:
                file = json.load(f)
        return file

    def file_write(filename, item):  # Overwrites file!
        with open('package/data/' + filename + '.json', 'w', encoding=('UTF-8')) as outfile:
            json.dump(item, outfile, ensure_ascii=False)

    def file_delete(filename):
        os.remove('package/data/' + filename + '.json')
