import os

DIRS = {
    'my_project':
        [
            {'settings': None},
            {'mainapp':
                [
                    {'templates':
                        [
                            {'mainapp': None}
                        ]}
                ]},
            {'adminapp': None},
            {'authapp':
                [
                    {'templates':
                        [
                            {'authapp': None}
                        ]}
                ]}
        ],
    'test_project':
        [
            {'settings': [
                {'test_dir_1': [
                    {'test_dir_1': None},
                    {'test_dir_2': None}
                ]},
                {'test_dir_2': None}
            ]},
            {'mainapp': None},
            {'adminapp': None},
            {'authapp': None}
        ]
}


def generate_paths(dirs, _result, _path='./', is_recursive=False):
    for key, values in dirs.items():
        if not is_recursive:
            _path = key
        for value in values:
            for _key, _value in value.items():
                dir_path = os.path.join(_path, _key)
                if _value:
                    generate_paths(value, _result, dir_path, True)
                    break
                _result.append(dir_path)


if __name__ == '__main__':
    paths = []
    generate_paths(DIRS, paths)
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
