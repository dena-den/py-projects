def justify(text, width):
    global full_ans

    if len(text) <= width:
        full_ans += text
        return full_ans

    line = width
    while text[line] != ' ':
        line -= 1
    ans = text[:line]

    if ans.find('\n') != -1:
        full_ans += ans[:ans.find('\n')+1]
        justify(text[(ans.find('\n')+1):], width)
        return full_ans

    if ans.find(' ') == -1:
        full_ans += ans + '\n'
        justify(text[line+1:], width)
        return full_ans

    start = 0
    while len(ans) < width:
        if start >= len(ans):
            start = 0
        space_location = ans.find(' ', start)
        if space_location == -1:
            start = 0
            continue
        ans = ans[:space_location] + ' ' + ans[space_location:]
        while ans[space_location] == ' ':
            space_location += 1
        start = space_location

    full_ans += ans + '\n'
    justify(text[line+1:], width)
    return full_ans

full_ans = ''

print(justify('Responsible and well trained. \n'
              'I want to further develop in the field of electric power, to gain new knowledge and practical skills. \n'
              'Ready to work out a full working week, combining it with your schedule at the university.', 45))