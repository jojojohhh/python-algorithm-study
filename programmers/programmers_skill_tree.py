import re


def solution(skill, skill_trees):
    regex = "[^" + skill + "]"
    return len([1 for skill_tree in skill_trees if skill.find(re.sub(regex, "", skill_tree)) == 0])