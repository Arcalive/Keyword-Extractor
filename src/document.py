# -*- coding: utf-8 -*-
################################################################################################################

class Document :
    def __init__(self, text: str, keywords: list) :
        self.tf_dic = {}
        self.id = id(self)
        self.text = ""
        self.url = ""

        self.split_text(text)
        self.cal_tf(keywords)

    ############################################################################################################

    def split_text(self, text: str) :
        text = text.split("\t")
        self.text = " ".join(text[:-1])
        self.url = text[-1].strip()

    ############################################################################################################

    def cal_tf(self, keywords: list) :
        for keyword in keywords :
            temp = keyword.split(" / ")
            self.tf_dic[temp[0]] = int(temp[2])