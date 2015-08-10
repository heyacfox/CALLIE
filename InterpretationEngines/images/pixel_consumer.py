from PIL import Image
from .. import consumer
from .. import part_machine
from .. import connections
from .. import any_part
from .. import errors
from .. import constants
import matplotlib.colors as colors
import copy

PART_CON_TYPES = {"N":connections.ConnectionTypeList("N"),
                  "NE":connections.ConnectionTypeList("NE"),
                  "E":connections.ConnectionTypeList("E"),
                  "SE":connections.ConnectionTypeList("SE"),
                  "S":connections.ConnectionTypeList("S"),
                  "SW":connections.ConnectionTypeList("SW"),
                  "W":connections.ConnectionTypeList("W"),
                  "NW":connections.ConnectionTypeList("NW")}

class PixelConsumer(consumer.Consumer):

    def add_data_to_machine(self):
        new_machine = self.begin_consume(self.data, self.part_machine)
        return new_machine

    #Here we go. Data is ALWAYS a data type. In this example, we get an
    #image file. We're going to assume that it's a PNG file I guess?
    def begin_consume(self, image_data, part_machine_obj):
        #image_data = Image.open(image_file_pat)
        image_x = image_data.size[0] - 1
        image_y = image_data.size[1] - 1
        pixels = image_data.load()

        for x_value in range(0, image_x):
            print("x-row:"+str(x_value) +"|out of:"+str(image_x))
            for y_value in range(0, image_y):
                self.consume_pixel(x_value,
                                   y_value,
                                   image_x,
                                   image_y,
                                   pixels,
                                   part_machine_obj)

        return part_machine_obj

    def consume_pixel(self, x_value, y_value, max_x, max_y, pixels, part_machine_obj):
        #NEED X_MAX HERE

        #GET THE RGB VALUES
        
        
        #North
        if (y_value > 0):
            self.apply_to_machine(x_value,
                             y_value,
                             x_value,
                             y_value - 1,
                             "N",
                             pixels,
                             part_machine_obj)

        #Northeast
        if ((y_value > 0) and (x_value < max_x)):
            self.apply_to_machine(x_value,
                             y_value,
                             x_value + 1,
                             y_value - 1,
                             "NE",
                             pixels,
                             part_machine_obj)
        
        #East
        if (x_value < max_x):
            self.apply_to_machine(x_value,
                             y_value,
                             x_value + 1,
                             y_value,
                             "E",
                             pixels,
                             part_machine_obj)

        #Southeast
        if ((x_value < max_x) and (y_value < max_y)):
            self.apply_to_machine(x_value,
                             y_value,
                             x_value + 1,
                             y_value + 1,
                             "SE",
                             pixels,
                             part_machine_obj)

        #South
        if (y_value < max_y):
            self.apply_to_machine(x_value,
                             y_value,
                             x_value,
                             y_value + 1,
                             "S",
                             pixels,
                             part_machine_obj)

        #Southwest
        if ((x_value > 0) and (y_value <max_y)):
            self.apply_to_machine(x_value,
                             y_value,
                             x_value - 1,
                             y_value + 1,
                             "SW",
                             pixels,
                             part_machine_obj)

        #West
        if (x_value > 0):
            self.apply_to_machine(x_value,
                             y_value,
                             x_value - 1,
                             y_value,
                             "W",
                             pixels,
                             part_machine_obj)

        #Northwest
        if ((x_value > 0) and (y_value > 0)):
            self.apply_to_machine(x_value,
                             y_value,
                             x_value - 1,
                             y_value - 1,
                             "NW",
                             pixels,
                             part_machine_obj)
        
    def apply_to_machine(self, x1, y1, x2, y2, rel_type, pixels, part_machine_obj):
        #get the pixel value
        #print("x1:"+str(x1)+" y1:"+str(y1)+" x2:"+str(x2)+" y2:"+str(y2)+" rel:"+str(rel_type))
        pixel_from = pixels[x1, y1]
        #get the first three things
        pixel_from_r = pixel_from[0]
        pixel_from_g = pixel_from[1]
        pixel_from_b = pixel_from[2]
        #put it in a tuple
        pixel_from_tuple = tuple([pixel_from_r,
                                 pixel_from_g,
                                 pixel_from_b])
        #convert it to hex
        pixel_from_hex = rgb_to_hex(pixel_from_tuple)
        #get the to pixel value
        pixel_to = pixels[x2, y2]
        #get the first three things
        pixel_to_r = pixel_to[0]
        pixel_to_g = pixel_to[1]
        pixel_to_b = pixel_to[2]
        #put it in a tuple
        pixel_to_tuple = tuple([pixel_to_r,
                               pixel_to_g,
                               pixel_to_b])
        #convert it to hex
        pixel_to_hex = rgb_to_hex(pixel_to_tuple)
        #add the hexes to the machine
        
        self.add_hex_to_machine(pixel_from_hex, pixel_to_hex, rel_type, part_machine_obj)
        

    def add_hex_to_machine(self, hex_from, hex_to, rel_type, part_machine_obj):
        part_machine_obj.add_connection_to_part(hex_from,
                                                rel_type,
                                                "Self",
                                                hex_to,
                                                hex_from,
                                                copy.deepcopy(PART_CON_TYPES))
        

def hex_to_rgb(hex_string):
    rgb = colors.hex2color(hex_string)
    return tuple([int(255*x) for x in rgb])

def rgb_to_hex(rgb_tuple):
    return colors.rgb2hex([1.0*x/255 for x in rgb_tuple])

        #go row by row and get the pixel data
        

#Code references:

#http://stackoverflow.com/questions/214359/converting-hex-color-to-rgb-and-vice-versa
