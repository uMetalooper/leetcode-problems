class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def evalBackspace(s):
            news = ""
            for c in s:
                if c == "#":
                    news = news[:-1]
                else:
                    news += c
            return news
        evals = evalBackspace(s)
        evalt = evalBackspace(t)
        if evals == evalt:
            return True
        else:
            return False

if Solution().backspaceCompare("ab##", "a#c#"):
    print("same")