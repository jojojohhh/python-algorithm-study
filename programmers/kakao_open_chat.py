def solution(record):
    user = {}
    chat_log = []
    for r in record:
        r = r.split(" ")
        if len(r) == 3:
            b, u, n = r
            user[u] = n
        else:
            b, u = r
        if b != "Change":
            chat_log.append([u, b])
    return [f"{user[chat[0]]}님이 들어왔습니다." if chat[1] == "Enter" else f"{user[chat[0]]}님이 나갔습니다." for chat in chat_log]
