def solution(participant, completion):
    hash_dict = {}

    for name in participant:
        if name in hash_dict:
            hash_dict[name] += 1
        else:
            hash_dict[name] = 1

    for name in completion:
        hash_dict[name] -= 1

    for name in hash_dict:
        if hash_dict[name] == 1:
            return name