from PIL import Image
from .. import consumer
from .. import part_machine
from .. import connections
from .. import any_part
from .. import errors
from .. import constants


class ImageConsumer(consumer.Consumer):

    def add_data_to_machine(self):
        new_machine = self.begin_consume(self.data, self.part_machine)
        return new_machine

    #Here we go. Data is ALWAYS a data type. In this example, we get an
    #image file. We're going to assume that it's a PNG file I guess?
    def begin_consume(self, image_file_path, part_machine_obj):
        image_data = Image.open(image_file_path)
        image_x = image_data.size[0]
        image_y = image_data.size[1]
        pixels = image_data.load()

        for x_value in range(1, image_x):
            for y_value in range(1, image_y):
                self.consume_pixel(x_value, y_value, image_x, image_y, pixels, part_machine_obj)

        return part_machine_obj

    def consume_pixel(x_value, y_value, max_x, max_y, pixels, part_machine_obj):
        #NEED X_MAX HERE
        #North
        if (y_value > 1):
            pass

        #Northeast
        if ((y_value > 1) and (x_value < max_x)):
            pass
        
        #East
        if (x_value < max_x):
            pass

        #Southeast
        if ((x_value < max_x) and (y_value < max_y)):
            pass

        #South
        if (y_value < max_y):
            pass

        #Southwest
        if ((x_value > 1) and (y_value <max_y)):
            pass

        #West
        if (x_value > 1):
            pass

        #Northwest
        if ((x_value > 1) and (y_value > 1)):
            pass
        

        

        #go row by row and get the pixel data
        
