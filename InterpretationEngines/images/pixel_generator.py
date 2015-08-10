from .. import generator
from .. import part_machine
from .. import connections
from .. import any_part
from .. import errors
from .. import constants
import queue
import random
from PIL import Image

class PixelGenerator:

    def __init(self, new_part_machine, width, height, start_pixel_tuple):
        self.part_machine = new_part_machine
        self.width = width
        self.height = height
        self.start_tuple = start_pixel_tuple
        self.image_file = Image.new("RGB", (width, height), "white")

    def generate(self):
        #start at the starter pixel
        #create a 2 dimensional array
            #dictionary with key values?
        #WE START AT 0 YO BECAUSE OF THE PIXEL THING
        print("Making Dict Array")
        dict_array = {}
        for x_value in range(0, self.width):
            for y_value in range(0, self.height):
                dict_array[tuple([x_value, y_value])] = ""
        #queue of pixel points and directions
        
        #First, put a random thing in the first pixel
        #THat makes the seed for the Image
        #Start at the pixel for the start
        #add elements to the end of the queue at all available surrounding
        #spaces
        print("Making Queue")
        pixel_queue = []
        for key in dict_array.keys():
            self.add_queue(key, pixel_queue, dict_array)
        #Once all pixels have been placed, go through the queue one by one
        #(we have forward and reverse calculations so whatever)
        #For every pixel,
        #image_pixels = image_file.load()
        print("Initiating While loop")
        while (len(pixel_queue) > 0):
            print("Length of Queue:" + str(len(pixel_queue)))
            selected_pixel = pixel_queue.pop(0)
            #This should return me a list,
            #list of two elements, the value and the weight
            potential_values = retrieve_potentials(selected_pixel[0],
                                                   selected_pixel[1],
                                                   dict_array)
            #potential_values is now a list of CONNECTIONS.
            #first, get our max weight
            max_weight = 0
            for con in potential_values:
                max_weight = max_weight + con.weight
            if max_weight == 0:
                #GAH JUST PICK SOMETHING AT RANDOM
                selected_color_hex = self.part_machine.get_any_part_id()
            else:
                #Otherwise, we stack through the things
                decrement_weight = random.randint(0, max_weight)
                for con in potential_values:
                    decrement_weight = decrement_weight - con.weight
                    if decrement_weight < 1:
                        selected_color_hex = con.part_id
            dict_array[selected_pixel[0], selected_pixel[1]] = selected_color_hex
        #AFTER THAT CRAZY WHILE LOOP ALL THE PIXELS HAVE BEEN PLACED
        #NOW WE PUT PIXELS ON THE IMAGE
        image_pixels = self.image_file.load()
        print("Writing Pixel Values")
        for key in dict_array.keys():
            image_pixels[key[0], key[1]] = hex_to_rgb(dict_array[key])
        #THEN, SAVE IT OUT
        image_file.save("/TestImage.png")
        #combine the possible values from all        
        #surrounding filled in pixel values
            #so, now what do we DO with selected_color_hex?
        
            
        #then, pick one of those values at weighted random
        #to use for the pixel
        #create an image from the dictionary of values

    def retrieve_potentials(self, x_value, y_value, dict_array):
        #THINGS
        #directions are reversed because we want to go
        #BACK to our original value
        adjusts = [[0, 1, "N"],
                   [0, -1, "S"],
                   [1, 0, "W"],
                   [1, 1, "NW"],
                   [1, -1, "SW"],
                   [-1, 0, "E"],
                   [-1, 1, "NE"],
                   [-1, -1, "SE"]]
        all_potentials = []
        for dir_adjust in adjusts:
            
            all_potentials = all_potentials + self.retrieve_potentials_for_adjust(self,
                                                                                  x_value,
                                                                                  y_value,
                                                                                  dir_adjust,
                                                                                  dict_array)
        return all_potentials
            #First, check if there is a key for the
            #value at the adjust
            #Then, check if there is a value for
            #the key at the adjust
            #Then check if there are connections at the
            #direction
    def retrieve_potentials_for_adjust(self, x_value, y_value, dir_adjust, dict_array):
        new_tuple = tuple([x_value + dir_adjust[0], y_value + dir_adjust[1]])
        if new_tuple in dict_array:
            #If it's in the array and if it has a color value we need to make decisions
            if (dict_array[new_tuple] != ""):
                #we need to get the part at the part machine (STIPULATION, WE NEVER USE COLORS
                #THAT HAVE NEVER BEEN PUT INTO THE MACHINE
                part_to_use = self.part_machine.get_part_by_id(dict_array[new_tuple])
                
                #and get connections that are at the designated cardinal direction
                return part_to_use.get_all_connections_in_type(dir_adjust[2])
        #if we make it to the end and we couldn't get things to pass, return
        #an empty list
        return []
        
            
    def add_queue(self, pixel_tuple, pixel_queue, dict_array):
        #check all pixels around the pixel tuple (including middle
        #directions)
        pixel_x = pixel_tuple[0]
        pixel_y = pixel_tuple[1]
        pixel_tuple_adding_list = []
        x_value_adjusts = [0, -1, 1]
        y_value_adjusts = [0, -1, 1]

        for x_adjust in x_value_adjusts:
            for y_adjust in y_value_adjusts:
                self.check_pixel(pixel_x + x_adjust,
                                 pixel_y + y_adjust,
                                 pixel_queue,
                                 dict_array)
                    

    def check_pixel(self, x_value, y_value, pixel_queue, dict_array):
        if ((x != 0) and (y != 0)):
            new_pixel_tuple = tuple([x_value,
                                     y_value])
            if new_pixel_tuple in dict_array:
                if (new_pixel_tuple not in pixel_queue):
                    pixel_queue.append(new_pixel_tuple)
        
def hex_to_rgb(hex_string):
    rgb = colors.hex2color(hex_string)
    return tuple([int(255*x) for x in rgb])
