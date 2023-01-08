class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dict_=collections.defaultdict()
        for i in s:
            dict_[i]=dict_.get(i,0)+1
        answer=[]
        for i in order:
            if i in dict_:
                answer.append(i*dict_[i])
                dict_[i]=0
        for i in dict_.keys():
            if dict_[i]>0:
                answer.append(i*dict_[i])
        return ''.join(answer)
            