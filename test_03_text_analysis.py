
import sys
import time

import numpy as np
import pandas as pd

### kanji_over2_extratct:from_1_text
def w_extract_kanji_over_x(
    text,
    pattern=None,
):
    """ ### kanji_over2_extratct:from_1_text
    text:
    pattern:
    """
    #pattern = r"[\u4E00-\u9FFF]{2,}"  # 漢字が2文字以上連続しているパターン
    pattern = r"([\u4E00-\u9FFF]{2,}|[\u30A0-\u30FF]{2,}|[a-zA-Z]{2,})"  # 漢字、カタカナ、アルファベットが2文字以上連続しているパターン

    matches = re.findall(pattern, text)
    print(matches)
    result = []
    for match in matches:
        if len(match) >= 2:
            result.append(match)

    #print(result)
    return result

### kanji_over2_extratct:df__contains__text
def w_extract_kanji_over_x__from_df(
    df_in,
    text_col_n='text',
):
    """ ### kanji_over2_extratct:from_1_text
    df_in:
    text_col_n='text':
    """

    df_res = df_in.copy()
    print(df_res)
    #time.sleep(5)
    df_res['words__kanji_over2'] = df_res[text_col_n].apply(w_extract_kanji_over_x)

    return df_res


### count_words
def count_words(
    df_in,
    words_col_n='words',
):
    """ ### kanji_over2_extratct:from_1_text
    df_in:
    words_col_n='words':
    """

    df_res = df_in.copy()
    #print(df_res)
    #time.sleep(5)

    ### count
    import itertools
    import collections
    words = list(
        itertools.chain.from_iterable(df_res[words_col_n])
    )
    #print(words)
    #print(type(words))
    #time.sleep(5)

    c = collections.Counter(words)
    #print(c)
    #print(type(c))
    #time.sleep(5)

    # c_common = c.most_common
    # #print(c.most_common)
    # #print(type(c.most_common))
    # print(c_common)
    # print(type(c_common))

    return c, words




### 
if __name__ == '__main__':

    ### kanji_over2_extratct:from_1_text
    import re
    re_words = w_extract_kanji_over_x(
        #text = "ある日、田中さんが公園で漢字の勉強をしていた。"
        text = "ある日、田中さんが公園で漢字の勉強をしていた。カタカナの読み方はフリガナで表記されます。English is also spoken in Japan."
        ### patternの入力は使用しない
        #pattern = r"[\u4E00-\u9FFF]{2,}"  # 漢字が2文字以上連続しているパターン
    )
    print(re_words)

    ### kanji_over2_extratct:df__contains__text
    df_text = pd.DataFrame(
        {'no': [0, 1],
         'text': ["ある日、田中さんが公園で漢字の勉強をしていた。カタカナの読み方はフリガナで表記されます。English is also spoken in Japan.",
                    "田中さんが公園で漢字の勉強をしていた。カタカナの読み方はフリガナで表記されます。English is also spoken in Japan.",
                 ],
        }
    )

    df_res = w_extract_kanji_over_x__from_df(
        df_in=df_text,
        text_col_n='text',
    )
    print(df_res)

    ### count_words
    w_counts_obj, words_l = count_words(
        df_in=df_res,
        words_col_n='words__kanji_over2',
    )
    c_common = w_counts_obj.most_common
    print('### w_counts_obj ###')
    print(w_counts_obj)
    print(type(w_counts_obj))
    print('### c_common ###')
    print(c_common)
    print(type(c_common))
    print('### words_l ###')
    print(words_l)
    print(type(words_l))

    #w_counts_dict = dict(w_counts_obj)
    #print(w_counts_dict)
    #print(type(w_counts_dict))
    #sys.exit()

    df__w_counts_obj = pd.DataFrame([dict(w_counts_obj)]).T
    df__w_counts_obj.columns = ['count']
    print(df__w_counts_obj.info())
    print(df__w_counts_obj)
    df__w_counts_obj.to_csv('df__w_counts_obj.csv', encoding='cp932')
    sys.exit()
    

    ### plot
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set()
    fig = plt.subplots(figsize=(8,8))
    sns.countplot(
        y=words_l,
        order=[i[0] for i in c_common(10)]
    )
    plt.show()
