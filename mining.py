from konlpy.tag import Twitter

import  re
from  crwal_video_info2 import func_video_crall
from  konlpy.tag import Twitter
import pandas as pd
def mining(comment_list):
    comment_list=comment_list
    #이모션 제거
    remover_emothion = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    #분석에 어긋나는 불용어구 제외
    han = re.compile(r'[ㄱ-ㅎㅏ-ㅣ!?~,".\n\r#\ufeff\u200d]')
    comment_result=[]
    for i in comment_list:
        tokens=remover_emothion.sub(r'',str(i))
        #sub할때 뒤에 인자 str type만 되나?
        print(tokens)
        tokens=re.sub(han,"",tokens)
        comment_result.append(tokens)

    comment_result=pd.DataFrame(comment_result,columns=["comment"])
    return comment_result


def get_noun(comment_txt):
    twitter=Twitter()
    noun=[]

    if len(comment_txt)>0:
        tw=twitter.pos(comment_txt)
        for i,j in tw:
            if j== 'Noun':
                noun.append(i)
        return noun
