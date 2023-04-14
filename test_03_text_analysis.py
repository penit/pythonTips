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
    pattern = r"[\u4E00-\u9FFF]{2,}"  # 漢字が2文字以上連続しているパターン

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


### 
if __name__ == '__main__':

    ### kanji_over2_extratct:from_1_text
    import re
    re_words = w_extract_kanji_over_x(
        text = "ある日、田中さんが公園で漢字の勉強をしていた。"
        #pattern = r"[\u4E00-\u9FFF]{2,}"  # 漢字が2文字以上連続しているパターン
    )
    print(re_words)

    ### kanji_over2_extratct:df__contains__text
    df_text = pd.DataFrame(
        {'no': [0, 1],
         'text': ["ある日、田中さんが公園で漢字の勉強をしていた。",
                    "田中さんが図書館で漢字の勉強をしていた。",],
        }
    )

    df_res = w_extract_kanji_over_x__from_df(
        df_in=df_text,
        text_col_n='text',
    )
    print(df_res)
