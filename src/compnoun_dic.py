# -*- coding: utf-8 -*-
################################################################################################################

class CompnounDic :
    def __init__(self) :
        self.dic = {}

    ############################################################################################################

    def combine(self, text: list) -> list:
        length = len(text)
        compnoun_list = []

        i = 0
        for _ in range(length) :
            if i == length :
                break

            elif text[i] in self.dic :
                compnoun = None

                for j in range(length-i) :
                    temp = "".join(text[i:i+j+1])
                    if temp in self.dic :
                        if self.dic[temp] == "True" :
                            compnoun = temp
                        else :
                            continue
                    else :
                        break

                if compnoun :
                    compnoun_list.append(compnoun)
                    i = i + j
                else :
                    i += 1

            else :
                i += 1

        return compnoun_list

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

                line = line.split("\t")
                self.dic[line[0]] = line[1]

    ############################################################################################################

    def compile(self, *inputs, **outputs) :
        compnoun_dic = {}
        compnoun_set = set()
        for input in inputs :
            with open(input, 'r', encoding = 'utf-8') as file :
                while 1 :
                    line = file.readline()
                    if not line :
                        break

                    line = line.strip()
                    if len(line) == 0 :
                        continue

                    line = line.split()
                    temp_line = "".join(line)
                    compnoun_set.add(temp_line)

                    line = outputs["josa"].split(line)

                    for i in range(len(line)) :
                        temp_str = "".join(line[:i+1])

                        if temp_str not in compnoun_set :
                            compnoun_dic[temp_str] = False
                        else :
                            compnoun_dic[temp_str] =True

        compnoun_dic = dict(sorted(compnoun_dic.items()))

        with open(outputs["output"], 'w', encoding = 'utf-8') as f :
            for key, value in compnoun_dic.items() :
                f.write(f"{key}\t{value}\n")

        print("복합명사 사전 컴파일 완료!")


################################################################################################################

if __name__ == "__main__" :
    compnoun_with_syn_list_path = "**************************************************"
    compnoun_list_path = "**************************************************"
    compnoun_dic_path = "**************************************************"

    test = CompnounDic()
    #test.compile(compnoun_with_syn_list_path, compnoun_list_path, output=compnoun_dic_path)
    test.load_dic(compnoun_dic_path)
    #print(test.dic)

    text = ['***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***']
    #text = ['***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***']
    print(text)
    print(test.combine(text))