# -*- coding: utf-8 -*-
################################################################################################################

class JosaDic :
    def __init__(self) :
        self.dic = []

    def split(self, text: list) -> list:
        temp_list = []
        for word in text :
            if len(word) > 2 :
                index = -1
                for i in range(len(word)) :
                    if word[-1-i:] in self.dic :
                        index = i
                if index == -1 or index == len(word)-1:
                    temp_list.append(word)
                else :
                    temp_list.append(word[:-1-index])
                    temp_list.append(word[-1-index:])
            else :
                temp_list.append(word)

        return temp_list

    ############################################################################################################

    def load_dic(self, dic_path: str) :
        with open(dic_path, 'r', encoding = 'utf-8') as f :
            while 1 :
                line = f.readline()
                if not line :
                    break

                line = line.strip()
                if len(line) == 0 :
                    continue

                self.dic.append(line)

    ############################################################################################################

    def compile(self, input: str, output: str) :
        with open(input, "r", encoding = "utf-8") as file :
            josa_list = []
            while 1 :
                line = file.readline()
                if not line :
                    break

                line = line.strip()
                if len(line) == 0 :
                    continue

                line = "".join(line.split())

                josa_list.append(line)

            josa_list = list(set(josa_list))
            josa_list.sort()

            with open(output, "w", encoding = "utf-8") as f:
                for josa in josa_list :
                    f.write(f"{josa}\n")

        print("조사 사전 컴파일 완료!")

################################################################################################################

if __name__ == "__main__" :
    josa_dic_path = "**********************************************************************"

    test = JosaDic()
    test.load_dic(josa_dic_path)
    #print(test.dic)

    text = ['***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***']
    print(test.split(text))