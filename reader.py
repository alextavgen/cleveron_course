import urllib.request
from enum import Enum


class Reader():
    def __init__(self):
        pass

    def get_data(self, resource):
        pass


class FileReader(Reader):
    def __init__(self):
        pass

    def get_data(self, resource):
        with open(resource, 'r') as file:
            return file.readlines()


class URLReader(Reader):
    def __init__(self):
        pass

    def get_data(self, resource):
        data = urllib.request.urlopen(resource)
        return data.readlines()


class ResourceType(Enum):
    FILE = 'FILE'
    URL = 'URL'


class Resource:
    def __init__(self, resource, resource_type):
        self.resource = resource
        self.resource_type = resource_type

    def is_file(self):
        if self.resource_type == ResourceType.FILE:
            return True
        else:
            return False

    def is_url(self):
        return True if self.resource_type == ResourceType.URL else False

class Logic():
    def __init__(self):
        pass

    def process_line(self, line):
        pass

    def get_results(self):
        pass


class WordCountLogic(Logic):
    def __init__(self):
        self.word_count = dict()

    def process_line(self, line):
        lines_splitted = line.split(',')
        words = lines_splitted[1].split(' ')
        for word in words:
            word = word.replace(',', '').replace('.','')
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1

    def get_results(self):
        return sorted(self.word_count.items(), key=lambda element: element[1], reverse=True)

class SentinentalAnalysisLogic(Logic):
    def __init__(self, negative_resource, positive_resource):
        self.negative_resource = negative_resource
        self.positive_resource = positive_resource
        self.positive_set = None
        self.negative_set = None
        self.comments_dictionary = dict()


    def process_line(self, line):
        if not self.positive_set or not self.negative_set:
            self.__initialisation__()

        lines_splitted = line.split(',')
        comments = lines_splitted[1]
        words = comments.split(' ')

        self.comments_dictionary[comments] = 0

        for word in words:
            if word in self.negative_set:
                self.comments_dictionary[comments] -= 1
            elif word in self.positive_set:
                self.comments_dictionary[comments] += 1

    def get_results(self):
        return sorted(self.comments_dictionary.items(), key=lambda element: element[1])


    def __initialisation__(self):
        self.negative_set = self.__get_resource__(self.negative_resource)
        self.positive_set = self.__get_resource__(self.positive_resource)

    @staticmethod
    def __get_resource__(resource):
        if resource.resource_type == ResourceType.FILE:
            file_reader = FileReader()
            filename = resource.resource

            result = list()
            for word in file_reader.get_data(filename):
                result.append(word.strip('\n'))

            return set(result)
        elif resource.resource_type == ResourceType.URL:
            url_reader = URLReader()
            url_name = resource.resource
            result = list()

            for word in url_reader.get_data(url_name):
                result.append(word.strip('\n'))
            return set(result)

class Processor():
    def __init__(self, resource_list, logic_list):
        self.file_reader = FileReader()
        self.url_reader = URLReader()
        self.resource_list = resource_list
        self.logic_list = logic_list


    def process_data(self):
        for resource in resource_list:
            lines = list()
            if resource.resource_type == ResourceType.URL:
                lines = self.url_reader.get_data(resource.resource)
            elif resource.resource_type == ResourceType.FILE:
                lines = self.file_reader.get_data(resource.resource)

            for line in lines:
                for logic in self.logic_list:
                    logic.process_line(line)

            for logic in self.logic_list:
                for result in logic.get_results():
                    print(result)


negatiivsed = 'https://raw.githubusercontent.com/alextavgen/facebook-scraper/master/final/negatiivne.txt'
positiivsed = 'https://raw.githubusercontent.com/alextavgen/facebook-scraper/master/final/positiivne.txt'

neg_file = '/Users/aleksandr.tavgen/Downloads/negatiivne.txt'
pos_file = '/Users/aleksandr.tavgen/Downloads/positiivne.txt'

neg_resource = Resource(neg_file, ResourceType.FILE)
pos_resource = Resource(pos_file, ResourceType.FILE)

URL = 'https://raw.githubusercontent.com/alextavgen/facebook-scraper/master/final/hinnavaatlus.csv'
file_name = '/Users/aleksandr.tavgen/Downloads/hinnavaatlus.csv'

resource_list = list()
#resource_list.append(Resource(URL, ResourceType.URL))
resource_list.append(Resource(file_name, ResourceType.FILE))

logic_list = list()
#logic_list.append(WordCountLogic())
logic_list.append(SentinentalAnalysisLogic(neg_resource, pos_resource))

processor = Processor(resource_list, logic_list=logic_list)

processor.process_data()

link = 'https://drive.google.com/file/d/1rDPIJfg5ENmNq4Ihx3MPmy6YrKefH-sx/'




