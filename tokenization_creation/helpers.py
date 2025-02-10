from functools import reduce


def tokenize_from_ranks(doc,tokens):
    if doc=='':
        return []
    for idx,token in enumerate(tokens):
        if doc==token:
            return [token]
        splits = doc.split(token)
        if len(splits)==1:
            continue
        return reduce(lambda x,y:x+[token]+y,[tokenize_from_ranks(d,tokens[idx+1:]) for d in splits])
    return list(doc)