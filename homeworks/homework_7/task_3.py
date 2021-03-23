from os import listdir, path, walk, makedirs
from shutil import copy2, rmtree


def search_template(_root_dir, _template_dir):
    template_path = ''
    _dirs = []
    for root, dirs, files in walk(_root_dir):
        if _template_dir in dirs:
            template_path = path.join(root, _template_dir)
        if template_path == root:
            _dirs = [path.join(root, _dirs) for _dirs in dirs]
        for _dir in _dirs:
            if _dir in root:
                yield _dir, [path.join(root, files_) for files_ in files]


def split_path(path_):
    return path.split(path_)[-1]


if __name__ == '__main__':
    root_dir = './my_project'
    template_dir = 'templates'
    result_template_dir = path.join(root_dir, template_dir)
    try:
        makedirs(result_template_dir)
    except FileExistsError as e:
        rmtree(result_template_dir)

    result = search_template(root_dir, template_dir)
    for item in result:
        dir_result = path.join(result_template_dir, split_path(item[0]))
        files_result = item[1]
        if not path.exists(dir_result):
            makedirs(dir_result)
        for file in files_result:
            copy2(file, path.join(dir_result, split_path(file)))
