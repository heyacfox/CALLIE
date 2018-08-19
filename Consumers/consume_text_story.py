class TextStoryConsumer:


    def __init__(self):
        self.something = 1

    #output of this will be the tree heirarchy that can be used as input to a creator

    def consume_text_list(self, text_list):
        #cycle along each specific part
        #you have a current, and the prev
        #link the current to the prev, reset the prev
        prev_part = text_list[0]
        text_list = text_list[1:]
        output_dict = {}
        for part in text_list:
            if prev_part not in output_dict.keys():
                output_dict[prev_part] = [part]
            else:
                output_dict[prev_part] = output_dict[prev_part] + [part]
            prev_part = part
        return output_dict
