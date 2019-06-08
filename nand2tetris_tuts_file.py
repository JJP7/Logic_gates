from tkinter import *
import pygame
from PIL import Image
from PIL import ImageDraw
import math

# Initialization
pygame.init()

# Images
AND = pygame.image.load("AND_gate.png")
NAND = pygame.image.load("NAND_gate.png")
NOT = pygame.image.load("NOT.png")
OR = pygame.image.load("OR.png")
NOT_toggle = pygame.image.load("NOT_toggle.png")
OR_toggle = pygame.image.load("OR_toggle.png")

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))  #[800, 600]
pygame.display.set_caption("nand2tetris")

pygame.display.update()

FPS = 15

clock = pygame.time.Clock()

#colors

white = (255, 255, 255)
black = (0, 0, 0)
idk = (125, 125, 125)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

logic_gates = []


def get_truth_table():
    pass


def boolean_expreseion():
    pass

def boolean_function():

    pass

def args_kwargs(*args, **kwargs):

    print(args)
    print(kwargs)

    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, kwargs[key])

    # for key, value in kwargs.iteritems(): # should have used .items instead of iteritems....
    #     print("%s = %s" %(key, value))

# Why are you still stuggling with classes yo, ?
# This should just have been simple, right?

class BinaryTree(): # implementation of a binary tree, also this is an ordered binary tree I guess...

    my_trees = []

    def __init__(self, *args, **kwargs):


        #self.tree = []  # contains all of the node information

        BinaryTree.my_trees.append(self)

        for key in kwargs:

            if key == "numlayers":
                self.numlayers = kwargs[key]

            # All a tree needs to know if only the fucking root node.

            if key == "root_node":
                self.root_node = kwargs[key]

    def create_tree(self):

        for l in self.numlayers:
            pass
            # append two things in the layer

    def create_root_Node(self, value):

        # this is the root node
        self.tree.append([])
        self.root_node = Node(value=value, layer=1)
        self.tree[0].append(self.root_node.value)

    def depth_first_search(self):   #used for obtaining data from the tree

        #pseudocode

        pass

    def go_next_layer(self, parent):

        return parent.children

    def breadth_first_search(self, **kwargs):

        # starting from the root node go to all of its chilren in the next layer
        # starting from the nodes of the next layer go to each of its children in the next layer
        # repeat this until there are no layers left.

        in_last_layer = False
        nodes_in_current_layer = [self.root_node]
        nodes_in_next_layer = []

        while in_last_layer == False:

            #print("g;aehg;wae;iohf")
            #print(nodes_in_current_layer)

            if len(nodes_in_current_layer) == 0:
            #if nodes_in_current_layer is None:

                #print("This should work")
                in_last_layer = True
                break

            for node in nodes_in_current_layer:

                for key in kwargs:   # there must be a way to avoid this redundancy

                      if key == "reset_my_tree":
                          node.my_tree = kwargs[key]

                      if key == "create_connections":

                          # create connections for each of the children
                          # don't do a for loop let's make this simple

                          # maybe I should check if it has any children in the first place?   # lol told you so.

                          #print(node.children, len(node.children))

                          if (node.children[0] is not None) or (node.children[1] is not None):

                              if node.children[0] is not None:
                                  pygame.draw.line(gameDisplay, blue, (node.my_gate.position[0], node.my_gate.position[1]),
                                                   (node.children[0].my_gate.position[0], node.children[0].my_gate.position[1]))
                              if node.children[1] is not None:
                                  pygame.draw.line(gameDisplay, blue, (node.my_gate.position[0], node.my_gate.position[1]),
                                                   (node.children[1].my_gate.position[0], node.children[1].my_gate.position[1]))

                nodes_in_next_layer.append(self.go_next_layer(node)[0])
                nodes_in_next_layer.append(self.go_next_layer(node)[1])

            for key in kwargs:

                if key == "show_tree":

                    current_layer_values = []

                    for nodes in nodes_in_current_layer:
                        current_layer_values.append(nodes.value)

                    print(current_layer_values)

            nodes_in_current_layer = nodes_in_next_layer
            nodes_in_next_layer.clear()


    def get_num_layers(self):
        pass

    def create_layer(self):
        pass


    def create_children_node(self, value, position, parent_node):

        if len(self.tree) < (parent_node.layer + 1):  #check if we have already created the next layer

            self.tree.append([]) #equivalently, creating a new layer object, because lists are confusin as fuck.

            for node in self.tree[parent_node.layer]: # new design feature, each layer is a list of children of the parent nodes

                if node.children is None:

                    self.tree[parent_node.layer + 1].insert(value) #displaying the tree is hard too

        child_node = Node(value=value, position=position, layer=parent_node.layer + 1, parent=parent_node)

        self.tree[parent_node.layer + 1][child_node.position] = child_node.value

        #we want to know the nodes in each layer of the tree.
        #the nodes are stored in order

    def fill_node(self):
        pass

    def show_tree(self):

        # print the contents of each node starting from the root node

        print(self.root_node.value)







        #just use breadth first search I guess but it would be better if we stored it already?

class Layers():  #maybe layers should be a class?
    pass



class Node():

    def __init__(self, **kwargs):  #probably should just put value as an *args or **kwargs

        #super().__init__()  no, we don't want inheritance, as that would create a new tree object for every new node.

        for key in kwargs:   #hooray! I actually used the fucking shit thing

            #weren't we like supposed to use an iterator?

            if key == "my_gate":         # the nodes contains an object which can be used to get data from
                self.my_gate = kwargs[key]
                #print("fkdsljfkjdsljflksdjlj",self.my_gate)


            if key == "value":
                self.value = kwargs[key]

            elif key == "position":
                self.position = kwargs[key]

            elif key == "layer":
                self.layer = kwargs[key]

            elif key == "parent":
                self.parent = kwargs[key]

        self.children = [None, None]
        self.my_tree = None

    def create_left_child(self, child_gate, value):

        new_node = Node(my_gate=child_gate, value=value, position=0, layer=self.layer + 1, parent=self)
        self.children[0] = new_node

    def create_right_child(self, child_gate, value):

        new_node = Node(my_gate=child_gate, value=value, position=1, layers=self.layer + 1, parent=self)
        self.children[1] = new_node


class Logic_gates(pygame.sprite.Sprite):

    gate_types = ["a", "o", "n"]
    # logic_gates = []
    # # does calling the class create a new object?

    def __init__(self, position, type):

        super().__init__()

        logic_gates.append(self) #oh I think I just appended it twice
        print(len(logic_gates))

        # position is from the top-left corner
        self.position = position
        self.bounding_box = [self.position[0], self.position[1], self.position[0] + 100, self.position[1] + 100]

        #Sprite handling for each logic gate.
        self.gate_surface = pygame.Surface((100, 100))
        self.gate_surface.fill((255, 255, 255))
        self.gate_rect = self.gate_surface.get_rect()    #what is the point of this get_rect shit man I don't understand

        self.type = type

        self.create_logic_gate(self.type, self.position)

    #you know what would be better?, it would be better if I used inheritance for each gate, because this is repetitive

    def create_AND_gate(self, position):

        gameDisplay.blit(AND, position)

    def create_OR_gate(self, position):

        gameDisplay.blit(OR, position)

    def create_OR_toggle(self, position):

        gameDisplay.blit(OR_toggle, position)

    def create_NOT_gate(self, position):

        gameDisplay.blit(NOT, position)

    def create_NOT_toggle_gate(self, position):

        gameDisplay.blit(NOT_toggle, position)

    def create_NAND_gate(self, position):

        gameDisplay.blit(NAND, position)

    def create_logic_gate(self, type,  position):  #lol, why do I even need to pass in a type? bullshit yeah itself has its own type no need to do this
                                                    # just make seperate classes and you'd be done

        self.update_position(position)
        self.type = type

        if type == "a":
            self.create_AND_gate(position)

        elif type == "o":
            self.create_OR_gate(position)

        elif type == "o1":

            self.create_OR_toggle(position)

        elif type == "n":
            self.create_NOT_gate(position)

        elif type == "n1":

            self.create_NOT_toggle_gate(position)

        elif type == "d":
            self.create_NAND_gate(position)

    def update_position(self, position):

        self.position = position
        self.bounding_box = [self.position[0], self.position[1], self.position[0] + 100, self.position[1] + 100]

    def toggle_gate(self):   # what is this for?, ah this is for connecting/ joining two gates

        #basically just change the state of a gate

        if self.type == "o":

            self.create_logic_gate("o1", self.position)

        elif self.type == "o1":

            self.create_logic_gate("o", self.position)

        elif self.type == "n":

            self.create_logic_gate("n1", self.position)

        elif self.type == "n1":

            self.create_logic_gate("n", self.position)

        elif self.type == "o":
            self.type = "o"
            self.create_logic_gate("a", self.position)

    def connect_gates(self):     # this is for parent gates

        # store the two gates I'm gonna connect in a data stucture



        # check which gates are clicked

        #first gate
        #find gate

        for x in range(0, len(logic_gates)):

            if logic_gates[x].bounding_box[0] <= pos[0] and pos[0] <= logic_gates[x].bounding_box[2]:
                if logic_gates[x].bounding_box[1] <= pos[1] and pos[1] <= logic_gates[x].bounding_box[3]:

                    #toggle gate
                    gate_1 = logic_gates[x]

        for y in range(0, len(logic_gates)):

            if logic_gates[y].bounding_box[0] <= pos[0] and pos[0] <= logic_gates[y].bounding_box[2]:
                if logic_gates[y].bounding_box[1] <= pos[1] and pos[1] <= logic_gates[y].bounding_box[3]:

                    #toggle gate
                    gate_2 = logic_gates[y]

def keep():
    pass


def mouse_selection_test(mouse_event, logic_gates):

    for x in range(0, len(logic_gates)):

        if logic_gates[x].bounding_box[0] <= pos[0] and pos[0] <= logic_gates[x].bounding_box[2]:
            if logic_gates[x].bounding_box[1] <= pos[1] and pos[1] <= logic_gates[x].bounding_box[3]:
                # toggle gate
                gate_1 = logic_gates[x]



def gameloop():

    # events....

    gameExit = False
    mouse_pressed = False
    my_gate = None
    connect_gates = False

    gate_pair = [None, None]
    gate_1 = None
    gate_2 = None


    while gameExit == False:

        # refresh?
        gameDisplay.fill(white)
        #pygame.display.update()
        

        # display logic gates

        # im = Image.open("NOT_gate.png")
        # draw = ImageDraw.Draw(im)
        # draw.ellipse((100, 100, 200, 200), fill=128)
        # #draw.line((0, 0, 500, 500), fill=128)
        # del draw
        # im.save("NOT_gate.png")

        # img = Image.open("OR.png")
        #
        # # maintain aspect ratio
        # width, height = img.size
        # ratio = height/width
        # newheight = ratio * 150
        #
        # img = img.resize((60, 60))
        # img.save("OR.png")


        #print(logic_gates)






        # I'm doing this instead of using a spritesheet
        #gameDisplay.blit(NOT, (100, 100))


        for event in pygame.event.get():  # I just realized, this is an event queue isn't it?

            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.MOUSEBUTTONDOWN:



                pos = pygame.mouse.get_pos()
                x_pos = pygame.mouse.get_pos()[0]
                y_pos = pygame.mouse.get_pos()[1]
                print(pos)

                # does the in keyword create duplicates?
                for x in range(0, len(logic_gates)): # ah maybe this is the one that duplicates shit yeah i think so, it modifies the duplicates instead of the gate itself

                    if logic_gates[x].bounding_box[0] <= pos[0] and pos[0] <= logic_gates[x].bounding_box[2]:
                        if logic_gates[x].bounding_box[1] <= pos[1] and pos[1] <= logic_gates[x].bounding_box[3]:

                            my_gate = logic_gates[x]

                            mouse_pressed = True

                            if connect_gates == True:  # this code is so fucking confusing and so hard to fucking read



                                if gate_pair[0] is None:

                                    #I'm stroing the value, not the object, so the posiiton is lost, maybe I should pass in the object?

                                    new_node = Node(object=my_gate, value=my_gate.type)  #storing this into the data structure

                                    gate_pair[0] = my_gate
                                    print("added the gate")

                                elif gate_pair[0] is not None:

                                    new_node = Node(object=my_gate, value=my_gate.type)  #storing this into the data structure

                                    gate_pair[1] = my_gate

                                    # check which trees each node belong because if they're different trees we will delete them and merge them into one tree.
                                    # it needs to be the root of the tree btw....

                                    #check if the node is the root of the tree

                                    if gate_pair[1].my_node.layer == 1:

                                        gate_pair[0].my_node.create_left_child(gate_pair[1], gate_pair[1].type)

                                        connect_gates = False


                                    # if they are from the same tree (this is impossible btw.)

                                    # else if they are from different trees, comibine them into one tree

                                    if gate_pair[0].my_node.my_tree is not gate_pair[1].my_node.my_tree:

                                        print("fjdklssfj")
                                        print(gate_pair[1].my_node.my_tree, gate_pair[0].my_node.my_tree)


                                        # the child and all of its children should belong to its parent tree now

                                        gate_pair[1].my_node.my_tree = gate_pair[0].my_node.my_tree

                                        if gate_pair[1].my_node.my_tree == gate_pair[0].my_node.my_tree:
                                            print("wakakakaka")


                                        # for child of gate_pair[1] child.tree  = parent tree

                                        gate_pair = [None, None]


                                print(gate_pair)

   # use fucking functions don't fucking hard code everything


                            print(pos, logic_gates[x].position)

                            my_gate = logic_gates[x]
                            #my_gate.create_logic_gate(logic_gates[x].type, pos)
                            my_gate.toggle_gate()

                            break


            if mouse_pressed == True:
                my_gate.create_logic_gate(my_gate.type, pos)   # is this working correctly I should probably refactor this into a function or something

            if event.type == pygame.MOUSEBUTTONUP:

                mouse_pressed = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_c:

                    print("connecting gates")

                    connect_gates = True

                if event.key == pygame.K_SPACE:

                    for x in range(0, len(BinaryTree.my_trees)):

                        print(f"---Tree{x}---")
                        BinaryTree.my_trees[x].breadth_first_search(show_tree=True)


                # Keys for creating logic gates
                good_keys = ["a", "o", "n"]

                # check if pressd key is a good key

                for key in good_keys:
                    if key == event.unicode:

                        #type of gate if the key
                        my_type = key
                        print(key)

                        # create the logic gate, new object
                        new_gate = Logic_gates(pos, my_type)

                        #store tha logic gate in a data structure

                        #create a tree for these new nodes

                        new_node_1 = Node(my_gate=new_gate, value=new_gate.type, layer=1)

                        new_tree = BinaryTree(root_node=new_node_1)

                        new_node_1.my_tree = new_tree

                        new_gate.my_node = new_node_1
                       # print(new_gate.my_node.layer)
                        print(new_node_1.value)
                        print(new_node_1.layer)






 ##############################################################################################################################
        #Drawing then updating

        pygame.draw.line(gameDisplay, black, (10, 10), (50, 50))  # this is gonna be laggy as hell

        for x in range(len(logic_gates)):

            logic_gates[x].create_logic_gate(logic_gates[x].type, logic_gates[x].position)
            # print(logic_gates[x].position)

        # A better way I guess is to use the binary trees data structure

        # draw the connections using the data structure


        for x in range(0, len(BinaryTree.my_trees)):


            BinaryTree.my_trees[x].breadth_first_search(create_connections=True)



            # # # I also need to go through the entire tree don't I?
            # #
            # # current_layer = [tree.root_node]
            # # next_layer = []
            # #
            # # # go to the root, draw the connections to the children.
            # #
            # # # Just applying breadth first search
            # #
            # # for node in current_layer:
            # #
            # #     next_layer.append(node.my_children[0])
            # #     next_layer.append(node.my_children[1])
            # #
            # #
            #
            # for node in current_layer:
            #
            #     pygame.draw.line(gameDisplay, black, (node.my_gate.position[0], node.my_gate.position[1]), ())
            #
            # # draw a line to each children.
        #
        # if (gate_pair[0] is not None) and (gate_pair[1] is not None):  #there should be a better way of doing this.
        #
        #     pygame.draw.line(gameDisplay, red, (gate_pair[0].position), (gate_pair[1].position))

        pygame.display.update()

        #clock.tick(FPS)


    pygame.quit()
    quit()



if __name__ == "__main__":

    # lol I feel really powerful using and knowing *args and **kwargs.
    # I want to be able to create a fucking library with this.

    args_kwargs('a', 'b', 'c', 'd', name="heroin", death="drugs")

    gameloop()

















