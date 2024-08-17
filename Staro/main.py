import csv
width = 150
height = 25
class node(object):
    all_nodes = []
    last_x = [0] # ovo je trebao biti obican broj, ali ga reseruje svakim ulaskom u klasu
    # last_x = 0
    def __init__(self, id, parent_id, name):
        # self.x = 0;
        # self.y = 0;
        self.name = name
        self.all_nodes.append(self)
        self.my_nodes = []
        self.id = id
        if(self.id > 0):
            for node in self.all_nodes:
                if(node.id == parent_id):
                    node.my_nodes.append(id)

    # def __str__(self, level = 0):
    #     ret = (1 * "\t") * level + self.name + "\n"
    #     for id in self.my_nodes:
    #         for node in self.all_nodes:
    #             if(id == node.id):
    #                 ret += node.__str__(level + 1)
    #     return ret

    # def __str__(self, level = 0):
    #     ret = ""
    #     for i in range(0, level - 1):
    #         ret += "|" + "\t"
    #     if(level > 0):
    #         ret += "o---"
    #     ret += self.name + "\n"
    #     for i, id in enumerate(self.my_nodes):
    #         for node in self.all_nodes:
    #             if(id == node.id):
    #                 if(i != len(self.my_nodes)):
    #                     for i in range(0, level + 1):
    #                         ret += "|"+ "\t"
    #                     ret += "\n"
    #                 ret += node.__str__(level + 1)
    #     return ret

    def __str__(self, space = "", level = 0, last = True):
        ret = space
        if (not last):
            space += "|" + "\t"
        else:
            space += "\t"
        if(level > 0):
            ret += "o---"
        ret += self.name + "\n"
        if(not last and len(self.my_nodes) > 0):
            ret += space + "|" + "\t"
            ret += "\n"
        for i, id in enumerate(self.my_nodes):
            for node in self.all_nodes:
                if(id == node.id):
                    ret += space + "|" + "\t"
                    ret += "\n"
                    if (i != len(self.my_nodes) - 1):
                        ret += node.__str__(space, level + 1, False)
                    else:
                        ret += node.__str__(space, level + 1, True)
        return ret

    def calc_coord(self, level = 0):
        height_mul = 6
        width_mul = 1.5
        self.y = int(height * (height_mul * level))

        if (len(self.my_nodes) == 0):
            self.x = int(self.last_x[0] + width * width_mul)
            self.last_x[0] = self.x
            # self.x = int(self.last_x + width * width_mul)
            # self.last_x = self.x
        else:
            sum = 0
            for id in self.my_nodes:
                for node in self.all_nodes:
                    if(id == node.id):
                        sum += node.calc_coord(level + 1)
            self.x = int(sum / len(self.my_nodes))

        return self.x

    def draw_lines(self, parent):
        text = ""
        for id in self.my_nodes:
            for node in self.all_nodes:
                if (id == node.id):
                    text += node.draw_lines(self)
        # print(str(parent.x) + " " + str(parent.y) + " " + str(self.x) + " " + str(self.y))
        text += self.add_line(parent.x, parent.y, self.x, self.y)
        return text

    def to_html(self):
        text = ""
        text += '<!DOCTYPE html>\n'
        text += '<html>\n'
        text += '    <head>\n'
        text += '        <meta charset="UTF-8">\n'
        text += '        <style>\n'
        text += '            #my\n'
        text += '            {\n'
        text += '               zoom: 30%;\n'
        text += '            }\n'
        text += '            .box\n'
        text += '            {\n'
        text += '                width: ' + str(width) + 'px;\n'
        text += '                height: ' + str(height) + 'px;\n'
        text += '                background: lightblue;\n'
        text += '                position:absolute;\n'
        text += '                color: black;\n'
        text += '                text-align: center;\n'
        text += '            }\n'
        text += '			.my-title\n'
        text += '            {\n'
        text += '                width: 800px;\n'
        text += '               height: 120px;\n'
        text += '                background: black;\n'
        text += '                position:absolute;\n'
        text += '                color: white;\n'
        text += '                text-align: center;\n'
        text += '            }\n'
        text += '            svg\n'
        text += '            {\n'
        text += '                overflow: visible;\n'
        text += '            }\n'
        text += '        </style>\n'
        text += '        <script>\n'
        text += '        </script>\n'
        text += '    </head>\n'
        text += '    <body>\n'
        text += '	<div id = "id--1" class = "my-title" style = "left: 0px; top: 0px;">\n'
        text += '		<h1>PORODIČNO STABLO KARPIĆ<h1>\n'
        text += '		<h2>Krećite se po radnoj površini da biste došli do stabla</h2>\n'
        text += '	</div>\n'

        self.calc_coord()

        for node in self.all_nodes:
            text += self.add_node(node.x, node.y, node.name, node.id)

        text += '        <svg style="stroke: black; stroke-width: 3px;">\n'
        text += self.draw_lines(self.all_nodes[0])
        text += '        </svg>\n'

        text += '    </body>\n'
        text += '</html>\n'
        return text

    def add_node(self, x, y, name, id):
        return '        <div id = "id-' + str(id) + '" class = "box" style = "left: ' + str(x) + 'px; top: ' + str(y) + 'px;">\n' + name + '</div>\n'
    def add_line(self, x1, y1, x2, y2):
        x1 = x1 + width / 2
        x2 = x2 + width / 2
        y1 = y1 + height / 2
        y2 = y2
        return '            <line x1="' + str(x1) + '" y1="' + str(y1) + '" x2="' + str(x2) + '" y2="' + str(y2) + '" marker-end="url(#arrowhead)"/>\n'
# Initial test to fill tree
# root = node(-1, 0, "root")
# x = node(1, -1, "A")
# x = node(2, -1, "B")
# x = node(11, 1, "C")
# x = node(12, 1, "D")
# x = node(21, 2, "E")
# x = node(22, 2, "F")
# print(root)

# Filling tree from test file
# filename = 'test.csv'
# root = node(-1, 0, "KORIJEN")
# with open(filename, newline='') as file:
#     reader = csv.reader(file, delimiter=',')
#     for i, row in enumerate(reader):
#         if(i != 0):
#             # print(str(int(row[0])) + str(int(row[1])) + row[2])
#             x = node(int(row[0]), int(row[1]), row[2])
# print(root)

# Filling tree from real file
filename = 'FamilyTree.csv'
root = node(-1, 0, "KORIJEN")
with open(filename, newline='', encoding = 'utf8') as file:
    reader = csv.reader(file, delimiter=',')
    for i, row in enumerate(reader):
        if(i != 0):
            # print(str(int(row[0])) + str(int(row[1])) + row[2])
            x = node(int(row[0]), int(row[1]), row[2])
# print(root)

f = open("Porodica Karpić.txt", "w", encoding = 'utf8')
f.write(str(root))
f.close()

f = open("Porodica Karpić.html", "w", encoding = 'utf8')
f.write(root.to_html())
f.close()