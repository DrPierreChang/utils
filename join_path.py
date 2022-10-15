import os


l = ["a", "b", "c"]
print("/".join(l))


print("some_path/".split("/"))


key = os.path.join('111. Данные полученные из подсистемы/РАГ', 'folder', 'json_example.json')
print(key)

nucl_folder = 'some_path/test777/19Mb.zip'
nucl_folder = nucl_folder.split('/')[:-1]
print(nucl_folder)

nucl_folder = '/'.join(nucl_folder)
print(nucl_folder == 'some_path/test777')
