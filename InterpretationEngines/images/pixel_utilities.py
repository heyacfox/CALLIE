"""

import png
import copy
f = open('someimage.png', 'wb')
w = png.Writer(255, 1, greyscale=True)
w.write(f, [range(256)])
f.close()

s = ['110010010011',
     '101011010100',
     '110010110101',
     '100010010011']
s = list(map(lambda x: map(int, x), s))
s2 = copy.deepcopy(s)
f = open('Matrixy.png', 'wb')
palette=[(0x55, 0x55, 0x55), (0xff, 0x99, 0x99)]
w = png.Writer(len(list(s[0])), len(s), palette=palette, bitdepth=1)
w.write(f, s)
f.close()

"""

import math
import statistics
import copy
import random
from PIL import Image

class PixelLike:

    def __init__(self, color_tuple):
        self.color_tuple = color_tuple
        self.weight = 1
        self.dist_from_zero = math.sqrt(color_tuple[0] * color_tuple[0] +
                                        color_tuple[1] * color_tuple[1] +
                                        color_tuple[2] * color_tuple[2])
        
    def add_weight(self):
        self.weight = self.weight + 1
    

def find_element(colorlike_tuple, list_of_elements):
    for pixely in list_of_elements:
        if pixely.color_tuple == colorlike_tuple:
            return pixely



#list_of_tuples = []
#This creates a list of RGBS PixelLikes and gives them weight
def creating_rgbs(pixel_list, width, height):
    returned_list_of_PLs = []
    list_of_tuples = []
    for x in range(0, width):
        for y in range(0, height):
            pixel_tuple = pixel_list[x,y]
            rgb_tuple = tuple([pixel_tuple[0], pixel_tuple[1], pixel_tuple[2]])
            if rgb_tuple == (77, 69, 66):
                print("Here's trouble first")
            #rgb_tuple = tuple([pixel_tuple[0],pixel_tuple[1],pixel_tuple[2])
            if rgb_tuple not in list_of_tuples:
                list_of_tuples.append(rgb_tuple)
                returned_list_of_PLs.append(PixelLike(rgb_tuple))
            else:
                value_retrieved = find_element(rgb_tuple, returned_list_of_PLs)
                value_retrieved.add_weight()
    #TESTING
    for x in returned_list_of_PLs:
        if x.color_tuple == (77, 69, 66):
            print("Here's trouble second")
    return returned_list_of_PLs

#now, we have list_of_rgbs that we can use for our tests.

#okay, here's the principle

#first, we gotta make the dict of the things
#we HAVE to sort the list like NOW



# after we do the one sort, we may have things that have a similar distance, but
#have different places.
#Really, now I want to put things closer together
#So, I want to check the next value and see if the distance
#between that and the NEXT one is lesser than the
#CURRENT one on the right.
#Make the distances between points as small as possible.
"""
list_of_dists = []
for x in list_of_rgbs:
    list_of_dists.append(x.dist_from_zero)
stdev_for_dists = statistics.pstdev(list_of_dists)
"""
def sort_list_of_rgbs(sublist_rgbs):
    #we want to sort
    #all the things. Start at the beginning
    returned_list = []
    for x in sublist_rgbs:
        if x.color_tuple == (77, 69, 66):
            print("Here is trouble 3")
    sublist_rgbs = copy.deepcopy(sublist_rgbs)
    value_first = sublist_rgbs[0]
    print(value_first.color_tuple)
    returned_list.append(value_first)
    #print(returned_list)
    #first thing.
    sublist_rgbs = sublist_rgbs[1:]
    while len(sublist_rgbs) > 0:
        if (len(sublist_rgbs) % 100 == 0):
            print(str(len(sublist_rgbs)))
        #THIS NEEDS TO COME FROM THE VALUE WE JUST PICKED NOT THE 0th THING!
        value_next = sort_lists_helper(returned_list[-1], sublist_rgbs)
        if value_next.color_tuple == (77, 69, 66):
            print("This is trouble")
        returned_list.append(value_next)
        sublist_rgbs.remove(value_next)
    for x in returned_list:
        if x.color_tuple == (77, 69, 66):
            print("Trouble 4")
    return returned_list

def sort_lists_helper(one_rgb, sublist):
    max_dist = 442.0
    temp_return = sublist[0]
    for x in sublist:
        if dist_between_3d_points(one_rgb.color_tuple, x.color_tuple) < max_dist:
            max_dist = dist_between_3d_points(one_rgb.color_tuple, x.color_tuple)
            temp_return = x
    #For this, we want to return the thing
    #that's closest to the selected rgb
    #print(str(max_dist))
    return temp_return
"""
pixel_dict = {}
for x in list_of_rgbs:
    if x in pixel_dict:
        pixel_dict[x] = pixel_dict[x] + 1
    else:
        pixel_dict[x] = 1
"""

def weight_view(sublist):
    new_dict = {}
    for pl in sublist:
        if pl.weight in new_dict:
            new_dict[pl.weight] = new_dict[pl.weight] + 1
        else:
            new_dict[pl.weight] = 1
    return new_dict

def dist_between_3d_points(point1, point2):
    return math.sqrt((point1[0] - point2[0]) * (point1[0] - point2[0]) +
              (point1[1] - point2[1]) * (point1[1] - point2[1]) +
              (point1[2] - point2[2]) * (point1[2] - point2[2]))

def calculate_distances(sublist_rgbs):
    sublist_copy = copy.deepcopy(sublist_rgbs)
    list_of_sub_dists = []
    while len(sublist_copy) > 1:
        dist_one = dist_between_3d_points(sublist_copy[0].color_tuple, sublist_copy[1].color_tuple)
        sublist_copy.pop(0)
	#sublist.pop(0)
        list_of_sub_dists.append(dist_one)
	#list_of_sub_dists.append(dist_one)
    
    #print(list_of_sub_dists[1:20])
    """
    for x in range(1, 20):
        print(sublist_rgbs[x].color_tuple)
    """
    #print("Mean:"+str(statistics.mean(list_of_sub_dists)))
    return statistics.mean(list_of_sub_dists)
#After we 


#Here's how tuple stacking works
#Level 1.1: Create a weight stack for each tuple. This means
#returns a stack_dict
def stackify_rgbs(sublist_rgbs):
    stack_dict = {}
    #creating weight stacks
    for pl in sublist_rgbs:
        stack_dict[pl] = [pl]
        if pl.color_tuple == (77, 69, 66):
            print("Here's trouble")
    low_rank_value = 1
    num_stacks = math.ceil(calculate_distances(sublist_rgbs))
    print("total stacks needed:" + str(num_stacks))
    while len(stack_dict) > num_stacks:
        print("Stacks:"+str(len(stack_dict))+"|RANK"+str(low_rank_value))
        lowest_rank_list = get_weight_rank_stack_keys(low_rank_value, stack_dict)
        #now that we have our list, pick things out of it at random
        length = len(lowest_rank_list)
        while length > 0:
            print(str(length))
            #we need to pop an element and decide where it will go
            #until we break it all down
            #THIS DOESn'T WORK BECAUSE I CAN'T PULL INDEXES FROM THE STACK DICT
            #Okay now it does work because I'm pulling it by a key (which is an object in this case)
            gotten_element = lowest_rank_list.pop(random.randint(0, length - 1))
            if get_stack_weight(stack_dict[gotten_element]) == low_rank_value:
                #GOSH DARN IT I PUT IT IN A DICT AND NOW IT'S DISORDEREDDDDDDD
                choice_tuple = create_tuple_from_list(gotten_element, sublist_rgbs, stack_dict)
                #Okay, now pick something
                #print(choice_tuple)
                choice_left_dist = 500
                choice_right_dist = 500
                if choice_tuple[0] != "XXX":
                    choice_left_dist = dist_between_3d_points(gotten_element.color_tuple, choice_tuple[0].color_tuple)
                if choice_tuple[1] != "XXX":
                    choice_right_dist = dist_between_3d_points(gotten_element.color_tuple, choice_tuple[1].color_tuple)
                #print("Leftish:"+str(choice_left_dist)+"|Rightish:"+str(choice_right_dist))
                if choice_left_dist < choice_right_dist:
                    choosen_tuple = choice_tuple[0]
                else:
                    choosen_tuple = choice_tuple[1]
                #YOU SHOULD NEVER HIT A CHOICE WHERE LEFT AND RIGHT ARE
                #BOTH XXX
                #print(choosen_tuple)
                #STACKED UP
                popped = stack_dict.pop(gotten_element)
                stack_dict[choosen_tuple] = stack_dict[choosen_tuple] + popped
                #NOW WE NEED TO PUT IT IN THE STACK WITH THE CHOOSEN TUPLE
                #AND WE NEED TO KILL OUR STACK
                #We already popped our stack, so we're good
                length = len(lowest_rank_list)
                
            else:
                #If the element stack is no longer in the rank, I need to remove it from the thing
                #and reset the length
                length = len(lowest_rank_list)
        #at the end of all that craziness, bump the low_rank_value
        low_rank_value = low_rank_value + 1
    return stack_dict
#that this stack is going to be a list of colorized tuples.
#Eventually, some weight stacks will be destroyed as others are built up.
#Ultimately, we want as many weight stacks as the mean of distances rounded up? Maybe?
#Level 1.2: identify which elements are in the lowest weight rank.
#pick elements, one at a time out of the low weigh rank, at random
#If the element has moved up to a higher weight rank than our
#current rank we're doing, ignore it.
#Check the weight stacks to the left and right.
#Add thyself to the weight stack that is the closest distance.
#After all of that rank's things have been checked, Count the weight stacks
#If the number of weight stacks equals the mean of

#If
def create_tuple_from_list(element, sublist_rgbs, stack_dict):
    index_value = sublist_rgbs.index(element)
    #That index is where the element is in the sublist, the ordered list thing.
    #we need to find the left and right things
    #but are they their own stacks? Or have they already been absorbed by a stack?
    #left and right things. If we are at the first index, just give us the thing to the right
    #if we are at the last index, just the thing to the left
    right_tuple = "XXX"
    left_tuple = "XXX"
    right_index = index_value + 1
    left_index = index_value - 1
    #CHECK IF THEY LEFT THING IS A STACK
    #IF IT'S NOT A STACK, KEEP GOING UNTIL YOU HIT ONE
    #If we're not the zero, get the left one
    if left_index > 0:
        left_tuple = get_me_element("left", left_index, sublist_rgbs, stack_dict)
    #if we're not the end, get the right one
    if right_index < (len(sublist_rgbs) - 1):
        right_tuple = get_me_element("right", right_index, sublist_rgbs, stack_dict)
    return tuple([left_tuple, right_tuple])
    
def get_me_element(direction, index, sublist_rgbs, stack_dict):
    #These need to be re-written because I'm getting infinite recursion errors
    result = "XXX"
    if direction == "left":
        while index > 0:
            result = get_me_element_helper(index, sublist_rgbs, stack_dict)
            if result == "XXX":
                index = index - 1
            else:
                return result
        return result
    if direction == "right":
        while index < len(sublist_rgbs):
            result = get_me_element_helper(index, sublist_rgbs, stack_dict)
            if result == "XXX":
                index = index + 1
            else:
                return result
        return result
    #Okay didn't get anything cause we couldn't pass the while just return XXX
    return result
    """
    if sublist_rgbs[index] in stack_dict:
        return sublist_rgbs[index]
    else:
        if direction == "left":
            #print("left-len:"+str(len(sublist_rgbs))+"|Index:"+str(index))
            if index == 0:
                return "XXX"
            else:
                return get_me_element("left", index - 1, sublist_rgbs, stack_dict)
        if direction == "right":
            #print("right-len:"+str(len(sublist_rgbs))+"|Index:"+str(index))
            if index == (len(sublist_rgbs) - 1):
                #print("Index:"+str(index)+"|Sublist_val:"+str(len(sublist_rgbs) - 1))
                return "XXX"
            else:
                return get_me_element("right", index + 1, sublist_rgbs, stack_dict)
    raise RuntimeError("There is no possible element in this sector")
    """
def get_me_element_helper(index_to_check, sublist_rgbs, stack_dict):
    if sublist_rgbs[index_to_check] in stack_dict:
        return sublist_rgbs[index_to_check]
    else:
        return "XXX"

def get_weight_rank_stack_keys(rank, stack_dict):
    list_of_keys = []
    for key in stack_dict:
        if get_stack_weight(stack_dict[key]) == rank:
            #print(key)
            list_of_keys.append(key)
    return list_of_keys

def get_stack_weight(pl_stack):
    weight = 0
    for pl in pl_stack:
        weight = weight + pl.weight
    return weight
#move to the next rank.
#

#So, the mean, and the average deviation from the mean.

def sort_PLs(PL_list):
    PL_list.sort(key=lambda x: x.dist_from_zero, reverse=False)
    return PL_list

#Down here are the things that run at setup
#This is the thing with the arctic fox
"""
print("Initialize pixel choosing test")
im = Image.open("arcticfox2.png")
print(im.format, im.size, im.mode)
im.getpixel((2, 5))
#im.show()
pixels = im.load()
list_of_rgbs = []
list_of_rgbs.sort(key=lambda x: x.dist_from_zero, reverse=False)
"""

def create_fake_list():
    return_tuple_dict = {}
    for x in range(0, 50):
        for y in range(0, 50):
            return_tuple_dict[(x, y)] = (x, y, 0)
    return return_tuple_dict

#The final process once we have the stackified list is to re-create the image
#from the original image

def simplify_from_stack(pixels, PL_stack, width, height):
    #For each thing in the image
    
    pixel_map = pixels

    stack_tuplefied = simplify_stack(PL_stack)
    print(stack_tuplefied)
    print(stack_tuplefied.keys())
    for x in range(0, width):
        for y in range(0, height):
            temp_pix = pixel_map[x,y]
            print(str(temp_pix))
            temp_tuple = return_altered_pixel(tuple([temp_pix[0],
                                                   temp_pix[1],
                                                   temp_pix[2]]), stack_tuplefied)
            print(str(x) + "|" + str(y) + ":" +str(temp_tuple))
            pixel_map[x,y] = temp_tuple
    return pixel_map

def return_altered_pixel(color_tuple, stack_tuplefied):
    #at the end of this, return a triple tuple pixel value
    
    for key in stack_tuplefied.keys():
        if key == color_tuple:
            return key
        else:
            if color_tuple in stack_tuplefied[key]:
                return key
    return "XXXXXX"
    
    
def simplify_stack(PL_stack):
    simple_stack = {}
    for key in PL_stack.keys():
        new_key = key.color_tuple
        new_values = []
        for PL in PL_stack[key]:
            new_values.append(PL.color_tuple)
            if PL.color_tuple == (77, 69, 66):
                print("Here's trouble again")
        simple_stack[new_key] = new_values
    return simple_stack
    


#GIANT WRAPPER FOR EVERYTHING INVOLVED HERE
def simplify_image_pixels(pixels, width, height):
    list_of_PLs = creating_rgbs(pixels, width, height)
    sorted_list_of_PLs = sort_PLs(list_of_PLs)
    super_sorted_list_of_PLs = sort_list_of_rgbs(sorted_list_of_PLs)
    stackified_PLs = stackify_rgbs(super_sorted_list_of_PLs)
    new_pixel_map = simplify_from_stack(pixels, stackified_PLs, width, height)
    return new_pixel_map
    

#These are the steps with the fake tuple list
"""
fake_tuple_list = {(0, 0):(0, 0, 0), (1, 0):(6, 4, 5), (2, 0):(6, 4, 5),
                   (0, 1):(20, 20, 20), (1,1):(45, 45, 60), (2,1):(100, 100, 125),
                   (0,2):(30, 20, 10), (1,2):(99, 255, 255), (2,2):(255, 255, 255)}
fake_tuple_list2 = {(0, 0):(0, 0, 0), (1, 0):(0, 0, 0), (2, 0):(5, 5, 5),
                   (0, 1):(5, 5, 5), (1,1):(5, 5, 5), (2,1):(10, 10, 10),
                   (0,2):(5, 5, 5), (1,2):(10, 10, 10), (2,2):(10, 10, 10)}

print("FakeTupleBegin")
faked_created = create_fake_list()
#print(str(faked_created))
fake_PL_list = creating_rgbs(faked_created, 50, 50)
print("Fake is now a list of PLs")
#print(str(fake_PL_list))
sorted_fake_PL_list = sort_PLs(fake_PL_list)
print("Sorted")
stackified_fake_PL_list = stackify_rgbs(sorted_fake_PL_list)
print("Stackified")
#print(stackified_fake_PL_list)
"""
"""
#new arctic fox mix:
im = Image.open("arcticfox2.png")
print(im.format, im.size, im.mode)
im.getpixel((2, 5))
#im.show()
pixels = im.load()
list_of_PLs = creating_rgbs(pixels, im.size[0], im.size[1])
sorted_list_of_PLs = sort_PLs(list_of_PLs)
super_sorted_list_of_PLs = sort_list_of_rgbs(sorted_list_of_PLs)
stackified_PLs = stackify_rgbs(super_sorted_list_of_PLs)

print("Stackified Arctic Fox")
"""
