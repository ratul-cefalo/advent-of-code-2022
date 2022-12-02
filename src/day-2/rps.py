from functools import partial, cache
from rps_input import given_cases

# print(given_cases[-5:])


def checker(instance: str, cases: set[str]) -> bool:
    return True if instance in cases else False

WIN_CASES = {'A Y', 'B Z', 'C X'}
does_win = partial(checker, cases=WIN_CASES)

DRAW_CASES = {'A X', 'B Y', 'C Z'}
is_draw = partial(checker, cases=DRAW_CASES)

@cache
def scorer(instance: str) -> int:
    shape_score = dict(
        # A=1, B=2, C=3,
        X=1, Y=2, Z=3
    )
    score = shape_score[instance[-1]]

    if does_win(instance): score+=6
    elif is_draw(instance): score+=3

    return score

def total_score(cases=['A Y', 'B X', 'C Z']):
    scores = map(scorer, cases)
    return sum(scores)

if __name__ == "__main__":
    assert total_score, 15
    print(total_score(given_cases))