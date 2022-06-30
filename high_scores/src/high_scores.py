from xml.dom.minidom import parseString


def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_three = []
    counter = 0
    if len(scores) <= 2:
        scores.sort(reverse = True)
        return scores
    while counter < 3:
        the_max = scores.index(max(scores))
        top_three.append(scores.pop(the_max))
        counter += 1
    return top_three

def descending_list(scores):
    scores.sort(reverse = True)
    return scores