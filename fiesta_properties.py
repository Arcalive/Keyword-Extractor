# -*- coding: utf-8 -*-
import os

################################################################################################################

class FiestaProperty :
    def __init__(self) :
        self.josa_list_path = "dics\josa\josa_list\josa.list"
        self.josa_dic_path = "dics\josa\josa.dic"

        self.keyword_list_path = "dics\mean\mean_list\*********.txt"
        self.syn_dic_path = "dics\mean\syn_std.dic"
        self.keyword_dic_path = "dics\mean\word_mean_tag_set.dic"

        self.compnoun_with_syn_list_path = "dics\comp_noun\comp_noun_list\comp_noun_with_mean.list"
        self.compnoun_list_path = "dics\comp_noun\comp_noun_list\comp_noun.list"
        self.compnoun_dic_path = "dics\comp_noun\comp_noun.dic"

        self.raw_data_path = "data\\1. raw_data\*********\*********.txt"
        self.extracted_data_path = "data\\2. keyword_extract_data\*********\*********.txt"

        self.check_dir()

    ############################################################################################################

    def check_dir(self) :
        dir_path = os.getcwd()
        
        self.josa_list_path = os.path.join(dir_path, self.josa_list_path)
        self.josa_dic_path = os.path.join(dir_path, self.josa_dic_path)

        self.keyword_list_path = os.path.join(dir_path, self.keyword_list_path)
        self.syn_dic_path = os.path.join(dir_path, self.syn_dic_path)
        self.keyword_dic_path = os.path.join(dir_path, self.keyword_dic_path)

        self.compnoun_with_syn_list_path = os.path.join(dir_path, self.compnoun_with_syn_list_path)
        self.compnoun_list_path = os.path.join(dir_path, self.compnoun_list_path)
        self.compnoun_dic_path = os.path.join(dir_path, self.compnoun_dic_path)

        self.raw_data_path = os.path.join(dir_path, self.raw_data_path)
        self.extracted_data_path = os.path.join(dir_path, self.extracted_data_path)

################################################################################################################

if __name__ == "__main__" :
    test = FiestaProperty()