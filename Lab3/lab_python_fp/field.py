# DONE


def field(list_, *args):
    assert len(list_) != 0
    answer = []
    if len(args) != 1:
        for dictionary in list_:
            dict_ = {}
            for i in dictionary:
                for arg in args:
                    if i == arg:
                        dict_[arg] = dictionary[i]
            answer.append(dict_)
    else:
        for dictionary in list_:
            for i in dictionary:
                for arg in args:
                    if i == arg:
                        answer.append(dictionary[i])
    return answer
