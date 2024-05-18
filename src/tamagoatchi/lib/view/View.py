import json
import logging
import string
from typing import Any

from tamagoatchi.app.definitions import ROOT_DIR
from tamagoatchi.lib.handlers import ResourceHandler


class SuperFormatter(string.Formatter):
    """
    Class used to format strings
    """
    def __init__(self, default='') -> None:
        self.default = default

    def get_value(self, key, args, kwds) -> Any:
        if isinstance(key, str):
            return kwds.get(key, self.default.format(key))
        else:
            return string.Formatter.get_value(key, args, kwds)

    def format_field(self, value, spec: str) -> Any:
        """
        Function to format loops or callable when string is in brackets
        """
        if spec == 'call':
            return value()
        if spec.startswith('repeat'):
            split_arr = spec.partition(':')
            it = split_arr[0].split()[2]
            template = split_arr[-1]
            return '\n'.join(
                [self.format(template, **{it: val}, i=i + 1) for i, val in zip(range(0, len(value)), value)])
        else:
            return super(SuperFormatter, self).format_field(value, spec)

class View:
    def __init__(self, path: str) -> None:
        self.path = path

    def render(self):
        pass
class ConsoleView(View):
    """
    Class used to represent ConsoleView
    """
    def __init__(self, path: str, objects: dict, ext_dict: dict) -> None:
        """
        Function search the view and get all text
        """
        super().__init__(path)
        self.qualified_path_name = str(ROOT_DIR) + '\\cli\\views\\' + path + '.txt'
        self.inputs = {}
        self.objects = objects
        with open(self.qualified_path_name, 'r') as file:
            self.header = ext_dict
            self.__content = file.read()
            self.compile()
            self.parse(objects)

    def compile(self) -> None:
        """
        Function to compile the view and search if there's not error in view language
        """
        open_brackets = 0
        line_count = 1
        for line in self.__content.split('\n'):
            open_brackets += line.count('{') - line.count('}')
            if ';;Input' in line:
                res = line.partition(';;Input:')[2]
                if res == '':
                    logging.error("Error compiling view, Input name not given in line at " +
                                  self.qualified_path_name + ':' + str(line_count))
                    raise Exception("Error compiling view, Input name not given in line at " +
                                    self.qualified_path_name + ':' + str(line_count))
            line_count += 1
        if open_brackets != 0:
            logging.error("Error compiling view, Input name not given in line at " +
                          self.qualified_path_name + ':' + str(line_count))
            raise Exception("Error compiling view, Bracket mismatch at " +
                            self.qualified_path_name + ':' + str(line_count))

    def ObjectMappingLayer(self, objects: dict = None) -> None:
        """
        Function that format the strings
        """
        super_formater = SuperFormatter()
        self.__content = super_formater.format(self.__content, **objects)

    def langParser(self) -> int:
        """
        Function that create our own language in views
        """
        input_dict = {}
        skip_if = False
        for line in self.__content.split('\n'):
            if ';;if' in line:
                skip_if = True
                split_line = line.lstrip(';;if ').split('and')
                ans = True
                for ll in split_line:
                    tmp = ll.split()
                    if "'" not in tmp[0]:
                        first = input_dict[tmp[0]]
                    else:
                        first = tmp[0].strip("'")
                    if "'" not in tmp[2]:
                        second = input_dict[tmp[2]]
                    else:
                        second = tmp[2].strip("'")
                    if first != second:
                        ans = False
                        break
                if ans:
                    skip_if = False
            elif ';;default' in line:
                skip_if = False

            if skip_if:
                continue
            elif ';;inputL' in line:
                pre, trash, post = line.partition(';;inputL')
                print(pre, end='')
                post = post.strip()
                input_dict[post] = ''
                while True:
                    tmp = input()
                    if tmp == 'e':
                        break
                    input_dict[post] += '\n' + tmp
            elif ';;input' in line:
                pre, trash, post = line.partition(';;input')
                print(pre, end='')
                post = post.strip()
                if post[0] == '[' and post[-1] == ']':
                    post = post.strip('[')
                    post = post.strip(']')
                    if not post in input_dict.keys():
                        input_dict[post] = []
                    input_dict[post] += [input()]
                else:
                    input_dict[post] = input()
            elif ';;redirect' in line:
                tmp = line.lstrip(';;redirect ').strip()
                if "'" in tmp:
                    input_dict['form_redirect'] = tmp.strip("'")
                elif tmp in input_dict:
                    input_dict['form_redirect'] = input_dict[tmp]
            elif ';;push' in line:
                post = line.partition(';;push')[2].replace("\'", "\"").lstrip()
                if 'ext' not in input_dict:
                    input_dict['ext'] = []
                try:
                    input_dict['ext'].append(json.loads(post))
                except:
                    input_dict['ext'].append(post)
            elif ';;exit' == line or ';;exit' in line:
                return -1
            elif ';;refresh' == line or ';;refresh' in line:
                return 1
            else:
                if line != '' and ';;if' not in line and ';;default' not in line:
                    if line == '\\':
                        print()
                    else:
                        print(line)

        self.header['inputs'] = {}

        for key in input_dict:
            if key == 'form_redirect':
                self.header[key] = input_dict[key]
            elif key != 'choice':
                self.header['inputs'][key] = input_dict[key]

        return 0

    def render(self) -> int:
        """
        Rendering the view in function of langParser return
        """
        return_val = self.langParser()
        if return_val == 1:
            self.render()
        return return_val

    def parse(self, objects) -> str:
        """
        Used to parsing for objects
        """
        self.ObjectMappingLayer(objects)
        return self.__content

class GUIView:
    def __init__(self, ext_dict: dict) -> None:
        self.view_location = ResourceHandler.get_resources_location() + 2* f'\\{type(self).__name__.split('View')[0].lower()}' + '.tmx'
        self.header = ext_dict


    def redirect(self, location: str) -> int:
         self.header['form_redirect'] = location
         return 0

