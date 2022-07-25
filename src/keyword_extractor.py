# -*- coding: utf-8 -*-
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src.josa_dic import JosaDic
from src.keyword_dic import KeywordDic
from src.compnoun_dic import CompnounDic

from fiesta_properties import FiestaProperty
import re

################################################################################################################

class KeywordExtractor :
    def __init__(self) :
        self.josa = JosaDic()
        self.keyword = KeywordDic()
        self.compnoun = CompnounDic()
        self.property = FiestaProperty()

        self.load_dic()

    ############################################################################################################

    def load_dic(self) :
        print("사전 로드를 시작합니다.")
        try :
            self.josa.load_dic(self.property.josa_dic_path)
            self.keyword.load_dic(keyword = self.property.keyword_dic_path, syn = self.property.syn_dic_path)
            self.compnoun.load_dic(self.property.compnoun_dic_path)
            print("사전을 로드하였습니다.")
        except :
            print("사전 로드에 실패하였습니다.\n1을 입력하여 컴파일을 진행하세요.")

    ############################################################################################################

    def extract(self, text: str) :
        text = re.sub("[^ 0-9a-zA-Z가-힣]", " ", text).strip().split()

        text = self.josa.split(text)

        text = self.compnoun.combine(text)

        text = self.keyword.extract(text)

        return text

    ############################################################################################################

    def compile(self) :
        print("컴파일을 시작합니다.")
        try :
            self.josa.compile(self.property.josa_list_path, self.property.josa_dic_path)
            self.keyword.compile(self.property.keyword_list_path, self.property.keyword_dic_path, self.property.syn_dic_path, self.property.compnoun_with_syn_list_path)

            self.josa.load_dic(self.property.josa_dic_path)
            self.compnoun.compile(self.property.compnoun_with_syn_list_path, self.property.compnoun_list_path, output = self.property.compnoun_dic_path, josa = self.josa)
            print("컴파일 모두 완료!")
        except :
            print("컴파일을 실패하였습니다.")

    ############################################################################################################

    def indexing(self) :
        print("색인을 시작합니다.")
        try :
            with open(self.property.raw_data_path, 'r', encoding = 'utf-8') as f :
                doc_keyword_dic = {}

                while 1 :
                    line = f.readline()
                    if not line :
                        break

                    line = line.strip()
                    if len(line) == 0 :
                        continue

                    orign_line = line

                    line = line.split("\t")
                    line = " ".join(line[:-1])

                    keyword = self.extract(line)
                    if not keyword :
                        continue

                    doc_keyword_dic[orign_line] = keyword

                with open(self.property.extracted_data_path, 'w', encoding = 'utf-8') as file :
                    for doc, keyword_dic in doc_keyword_dic.items() :
                        file.write(f"{doc}\t|||\t")
                        i = 1
                        for key, value in keyword_dic.items() :
                            if i == len(keyword_dic) :
                                file.write(f"{key} / {value[0]} / {value[1]}\n")
                            else :
                                file.write(f"{key} / {value[0]} / {value[1]}\t")
                                i += 1
                print("색인을 완료하였습니다.")
        except :
            print("색인을 실패하였습니다.")

################################################################################################################

if __name__ == "__main__" :
    sentence = """***************************************************************"""

    test = KeywordExtractor().extract(sentence)