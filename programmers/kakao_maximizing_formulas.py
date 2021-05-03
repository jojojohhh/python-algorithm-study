from itertools import permutations


def calcul(expression, permutation, idx):
    if idx == len(permutation) - 1:
        return str(eval(expression))
    if permutation[idx] == '*':
        s = eval('*'.join([calcul(e, permutation, idx + 1) for e in expression.split('*')]))
    elif permutation[idx] == '+':
        s = eval('+'.join([calcul(e, permutation, idx + 1) for e in expression.split('+')]))
    elif permutation[idx] == '-':
        s = eval('-'.join([calcul(e, permutation, idx + 1) for e in expression.split('-')]))
    return str(s)


def solution(expression):      
    answer = 0
    op = ['*', '+', '-']
    for permutation in permutations(op):
        answer = max(answer, abs(int(calcul(expression, permutation, 0))))
    return answer
