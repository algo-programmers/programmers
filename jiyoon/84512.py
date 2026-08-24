def solution(word):
    vowles = 'AEIOU'
    count = 0
    answer = 0

    def dfs(current):
        nonlocal count, answer

        if current :
            count += 1

            if current == word:
                answer = count
                return True

        if len(current) == 5:
            return False

        for vowel in vowles:
            if dfs(current + vowel):
                return True

        return False

    dfs("")
    return answer    