# -*- coding: utf-8 -*-
from src.keyword_extractor import KeywordExtractor
from src.document_searcher import DocumentSearcher

################################################################################################################

class Fiesta :
    def __init__(self):
        print("환영합니다.\n")
        self.extractor = KeywordExtractor()
        self.searcher = DocumentSearcher()

        self.main()

    ############################################################################################################

    def main(self):
        while 1 :
            try :
                temp = int(input("\n1 입력 : 사전 컴파일\n2 입력 : 문서 색인\n3 입력 : 검색\n4 입력 : 종료\n-> "))
            except :
                print("숫자만 입력해주세요.\n")
                continue

            if temp == 1 :
                self.compile()

            elif temp == 2 :
                self.indexing()

            elif temp == 3 :
                try :
                    self.search()
                except Exception as e :
                    print("에러가 발생하였습니다.", e)

            elif temp == 4 :
                print("시스템을 종료합니다.\n")
                break

            else :
                print("1~4 사이의 값만 입력해주세요.\n")
                continue

    ############################################################################################################

    def compile(self) :
        self.extractor.compile()

    def indexing(self) :
        self.extractor.indexing()

    def search(self) :
        while 1 :
            print("\n검색어를 입력해주세요. \"quit\"를 입력하시면 검색을 종료합니다.")
            line = input("-> ")
            if line == "quit" :
                break
            else :
                keyword = self.extractor.extract(line)
                if not keyword :
                    print("검색어에서 키워드를 발견하지 못하였습니다.")
                    continue

                self.searcher.search(keyword)

################################################################################################################

if __name__ == "__main__" :
    fiesta = Fiesta()