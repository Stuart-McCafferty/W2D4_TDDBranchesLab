def get_result(final_score):
    if final_score['home_score'] > final_score['away_score']:
        return f"Home wins, Score was {final_score['home_score']} - {final_score['away_score']}"
    elif final_score['home_score'] < final_score['away_score']:
        return f"Away wins, Score was {final_score['home_score']} - {final_score['away_score']}"
    return f"Draw, Score was {final_score['home_score']} - {final_score['away_score']}"

def get_results(final_scores):
    resultList = []
    for score in final_scores:
        resultList.append(get_result(score))
    return resultList