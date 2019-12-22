# Enter your code here. Read input from STDIN. Print output to STDOUT
import logging
import sys
from enum import Enum
from collections import deque


class FileType(Enum):
    file = 1
    directory = 2
    link = 3


class FileNode(object):
    def __init__(self):
        self.name = None
        self.fileType = None
        self.parent = None
        # array of FileNode objects
        self.children = []


class CommandProcessor(object):
    def __init__(self):
        self.root = FileNode()
        self.root.name = '/root'
        self.root.fileType = FileType.directory

    def pwd_cmd(self, cur_dir):
        if not cur_dir.parent:
            print(cur_dir.name)
            return
        print(self._get_full_path(cur_dir))

    def ls_cmd(self, cur_dir, args):
        if '-r' in args:
            self._print_children(cur_dir, True)
        else:
            self._print_children(cur_dir)

    def _print_children(self, node, recurse=False):
        if not node.children:
            return
        if recurse:
            stack = deque()
            stack.append(node)
            while stack:
                n = stack.pop()
                if n.fileType == FileType.directory and n != node:
                    print(self._get_full_path(n))
                for v in n.children:
                    if v.fileType == FileType.directory:
                        stack.append(v)
                    else:
                        print(v.name)
        else:
            for child in node.children:
                print(child.name)

    def _get_full_path(self, cur_dir):
        path = ''
        while cur_dir.parent:
            path = f'/{cur_dir.name}' + path
            cur_dir = cur_dir.parent
        return '/root' + path

    def mkdir_cmd(self, cur_dir, dir_name):
        if not dir_name:
            raise TypeError('Directory name cannot be empty')
        if len(dir_name) > 100:
            print('Invalid File or Folder Name')
            return
            # raise TypeError('Directory name must be less than 100 characters')

        # check if dir_name already exists in current directort
        for node in cur_dir.children:
            if node.fileType == FileType.directory:
                if node.name == dir_name.lower():
                    print('Directory already exists')
                    return
        tempNode = FileNode()
        tempNode.name = dir_name
        tempNode.parent = cur_dir
        tempNode.fileType = FileType.directory
        if not cur_dir.children:
            cur_dir.children = []
        cur_dir.children.append(tempNode)

    def cd_command(self, cur_dir, to_dir):
        if not to_dir:
            raise TypeError('Target directory name cannot be empty')
        if to_dir == '/':
            return self.root
        elif to_dir == '...':
            if cur_dir.parent is None:
                # print(f'{self._get_full_path(cur_dir)}')
                return cur_dir
            # print(f'{self._get_full_path(cur_dir)}')
            return cur_dir.parent
        else:
            for node in cur_dir.children:
                if node.fileType == FileType.directory:
                    if node.name == to_dir.lower():
                        # print(f'{self._get_full_path(node)}')
                        return node
            print('Directory not found')
            return cur_dir

    def touch_cmd(self, cur_dir, file_name):
        if not file_name:
            raise TypeError('File name must be provided')
        if len(file_name) > 100:
            # raise TypeError('File name must be within 100 characters')
            print('Invalid File or Folder Name')
            return
        node = FileNode()
        node.name = file_name
        node.parent = cur_dir
        node.fileType = FileType.file
        cur_dir.children.append(node)


if __name__ == '__main__':
    cli = CommandProcessor()
    current_directory = cli.root
    while True:
        try:
            cmd = input().strip().lower()
            splitted_cmd = cmd.split(' ')

            if splitted_cmd[0] == 'quit':
                logging.info('Quitting the application')
                sys.exit(0)
            elif splitted_cmd[0] == 'pwd':
                logging.debug('pwd command')
                cli.pwd_cmd(current_directory)
            elif splitted_cmd[0] == 'ls':
                logging.debug('ls command')
                cli.ls_cmd(current_directory, splitted_cmd)
            elif splitted_cmd[0] == 'cd':
                logging.debug('cd command: %s', splitted_cmd)
                if len(splitted_cmd) == 1:
                    print('Target directory name cannot be empty')
                else:
                    current_directory = cli.cd_command(
                        current_directory, splitted_cmd[1])
            elif splitted_cmd[0] == 'mkdir':
                logging.debug('mkdir command: %s', splitted_cmd)
                if len(splitted_cmd) == 1:
                    print('Directory name cannot be empty')
                else:
                    cli.mkdir_cmd(current_directory, splitted_cmd[1])
            elif splitted_cmd[0] == 'touch':
                logging.debug('touch command: %s', splitted_cmd)
                if len(splitted_cmd) == 1:
                    print('File name cannot be empty')
                else:
                    cli.touch_cmd(current_directory, splitted_cmd[1])
            else:
                print('Unknown command or command does not exist')
        except Exception as ex:
            logging.exception(ex)
