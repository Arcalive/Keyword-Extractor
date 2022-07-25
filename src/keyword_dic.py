# -*- coding: utf-8 -*-
################################################################################################################

class KeywordDic :
    def __init__(self) :
        self.mean_dic = {}
        self.syn_dic = {}

        self.oov_dict = {}

    ############################################################################################################

    def extract(self, text: list) -> dict :

        syn_list = [self.syn_dic[word] if word in self.syn_dic else word for word in text]

        i = 1
        keyword_dic = {}
        try :
            for word, syn in zip(text, syn_list) :
                if word == syn :
                    if word in keyword_dic :
                        keyword_dic[word][1] += 1
                    else :
                        keyword_dic[word] = [self.mean_dic[word], i]
                elif word != syn :
                    if syn in keyword_dic :
                        keyword_dic[syn][1] += 1
                    else :
                        keyword_dic[syn] = [self.mean_dic[word], i]
        except Exception as e :
            #print("키워드 추출 단계에서 에러가 발생하였습니다.", e)
            pass

        return keyword_dic

    ############################################################################################################

    def load_dic(self, **dic_path) :
        for key, value in dic_path.items() :
            with open(value, 'r', encoding = 'utf-8') as f :
                while 1 :
                    line = f.readline()
                    if not line :
                        break

                    line = line.strip()
                    if len(line) == 0 :
                        continue

                    line = line.split("\t")

                    if key == "keyword" :
                        self.mean_dic[line[0]] = ", ".join(line[1:])
                    elif key == "syn" :
                        self.syn_dic[line[0]] = line[1]

    ############################################################################################################

    def compile(self, input: str, keyword_output: str, syn_output: str, comp_output: str) :
        with open(input, "r", encoding = "utf-8") as file :
            keyword_dic = {}
            syn_dic = {}
            keyword_for_comp_list = set()
            line_num = 0

            while 1 :
                line = file.readline()
                if not line :
                    break

                line = line.strip()
                if len(line) == 0 :
                    break

                wrong_line = line
                line = line.split("\t")

                keyword = line[0].upper()
                mean =  line[1]

                try :
                    if mean[0] == "#":
                        no_spaces_keyword = keyword.replace(" ", "")

                        keyword_for_comp_list.add(keyword)

                        if no_spaces_keyword in keyword_dic :
                            keyword_dic[no_spaces_keyword].add(mean)
                        else :
                            keyword_dic[no_spaces_keyword] = {mean}

                        # 복합명사로 합치고, 동의어 사전으로 분리할 것임
                        if len(keyword.split()) > 1 :
                            if keyword in syn_dic :
                                syn_dic[keyword].add(no_spaces_keyword)
                            else :
                                syn_dic[keyword] = {no_spaces_keyword}

                        if line[2:] :
                            syn_list = [i.upper() for i in line[2:] if i.strip()]

                            for syn in syn_list :
                                no_spaces_syn = syn.replace(" ", "")

                                keyword_for_comp_list.add(syn.strip())
                                
                                if keyword in syn_dic :
                                    syn_dic[keyword].add(no_spaces_syn)
                                else :
                                    syn_dic[keyword] = {syn}

                                if no_spaces_syn in keyword_dic :
                                    keyword_dic[no_spaces_syn].add(mean)
                                else :
                                    keyword_dic[no_spaces_syn] = {mean}
                    else :
                        self.oov_dict[line_num] = wrong_line

                except :
                    self.oov_dict[line_num] = wrong_line

                line_num += 1

            for key, value in keyword_dic.items() :
                keyword_dic[key] = sorted(list(value))

            for key, value in syn_dic.items() :
                syn_dic[key] = sorted(list(value))

            keyword_dic = dict(sorted(keyword_dic.items()))
            syn_dic = dict(sorted(syn_dic.items(), key = lambda x : x[1]))
            keyword_for_comp_list = sorted(list(keyword_for_comp_list))

            with open(keyword_output, 'w', encoding= 'utf-8') as k :
                for key, mean_list in keyword_dic.items() :
                    temp = ", ".join(mean_list)
                    k.write(f"{key}\t{temp}\n")

            with open(syn_output, 'w', encoding = 'utf-8') as s :
                for key, syn_list in  syn_dic.items() :
                    for syn in syn_list :
                        s.write(f"{syn}\t{key}\n")

            with open(comp_output, 'w', encoding = 'utf-8') as c :
                for i in keyword_for_comp_list :
                    c.write(f"{i}\n")

        print("키워드 사전 컴파일 완료!")

################################################################################################################

if __name__ == "__main__" :
    input = "*****************************************************"
    keyword_output = "*****************************************************"
    syn_output = "*****************************************************"
    comp_output = "*****************************************************"

    test = KeywordDic()
    #test.compile(input, keyword_output, syn_output, comp_output)
    #print(test.oov_dict)

    test.load_dic(keyword = keyword_output, syn = syn_output)
    #print(test.mean_dic)
    #print(test.syn_dic)

    #text = ['***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***']
    text = ['***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***', '***']
    print(test.extract(text))
