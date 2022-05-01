from file_parsing import *

# ожидается ввод типа <name of the file> <path_to_parameters> <path_to_nodes>
# вязанные файлы, указанные в импортах сверху, должны лежать в той же папке

parser = Parser()
state = parser.parse('parameters.txt', 'positions.txt')
state.start()