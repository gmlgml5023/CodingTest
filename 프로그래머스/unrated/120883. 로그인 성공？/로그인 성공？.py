def solution(id_pw, db):
    dict_db = dict(db)
    if id_pw[0] in dict_db.keys():
        if dict_db[id_pw[0]] == id_pw[1]:
            answer = 'login'
        else :
            answer = 'wrong pw'
    else:
        answer = 'fail'
    return answer
