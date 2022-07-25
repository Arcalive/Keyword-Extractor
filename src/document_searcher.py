# -*- coding: utf-8 -*-
import os, sys

from attr import mutable
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from src.document import Document
from fiesta_properties import FiestaProperty

from math import log

################################################################################################################

class DocumentSearcher :
    def __init__(self) :
        self.df_dic = {}
        self.doc_dic = {}

        self.property = FiestaProperty()
        self.load_doc(self.property.extracted_data_path)

    ############################################################################################################

    def load_doc(self, file_path: str) :
        with open(file_path, 'r', encoding = 'utf-8') as f :
            while 1 :
                line = f.readline()
                if not line :
                    break

                line = line.strip()
                if len(line) == 0 :
                    continue

                line = line.split("|||")
                text = line[0].strip()
                tag_mean = line[1].strip().split("\t")

                document = Document(text, tag_mean)

                self.doc_dic[document.id] = document

                i = 1
                for keyword in tag_mean :
                    keyword = keyword.split(" / ")[0]
                    if keyword in self.df_dic :
                        self.df_dic[keyword][0] += 1
                        self.df_dic[keyword][1].append(document.id)
                    else :
                        self.df_dic[keyword] = [i, [document.id]]

    ############################################################################################################

    def search(self, keywords: dict) :
        result_dic = {}
        for keyword in keywords :
            doc_list = self.cal_tfidf(keyword)
            result_dic[keyword] = doc_list

        self.how_to_show(keywords, result_dic)

    ############################################################################################################

    def cal_tfidf(self, keyword: str) -> list:
        N = len(self.doc_dic)
        df = self.df_dic[keyword][0]
        idf = log(N/(df+1))

        temp_list = []
        for doc_id in self.df_dic[keyword][1] :
            tf = self.doc_dic[doc_id].tf_dic[keyword]
            tfidf = tf*idf
            text = self.doc_dic[doc_id].text
            url = self.doc_dic[doc_id].url
            temp_list.append([text, url, tfidf])

        temp_list = sorted(temp_list, key = lambda x:x[2], reverse = True)

        return temp_list

    ############################################################################################################

    def how_to_show(self, keywords: dict, result_dic: dict) :
        if len(keywords) > 1 :
            print("추출된 키워드 : ", end = "")
            i = 1
            for key, value in keywords.items() :
                if i == len(keywords) :
                    print(f"{key} {value[0]}")
                else :
                    print(f"{key} {value[0]} / ", end = "")
                    i += 1

            for key, value in keywords.items() :
                print(f"\n###### \"{key}\" 검색 결과 ######")

                for doc in result_dic[key][:5] :
                    print("문서:", doc[0])
                    print("url:", doc[1])
                    print("스코어:", doc[2])

        else :
            for key, value in keywords.items() :
                print(f"추출된 키워드 : {key} {value[0]}")
                print(f"\n###### \"{key}\" 검색 결과 ######")

                for doc in result_dic[key][:10] :
                    print("문서:", doc[0])
                    print("url:", doc[1])
                    print("스코어:", doc[2])
                    print()

################################################################################################################

if __name__ == "__main__" :
    file_path = "*****************************************************************"

    test = DocumentSearcher()
    test.load_doc(file_path)

    sample = ['***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***']
    test.search(sample)