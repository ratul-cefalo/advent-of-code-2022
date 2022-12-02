from functools import partial, cache
from rps_input import given_cases


def checker(instance: str, cases: set[str]) -> bool:
    return True if instance in cases else False


WIN_CASES = {"A Y", "B Z", "C X"}
does_win = partial(checker, cases=WIN_CASES)

DRAW_CASES = {"A X", "B Y", "C Z"}
is_draw = partial(checker, cases=DRAW_CASES)


@cache
def scorer(instance: str) -> int:
    shape_score = dict(X=1, Y=2, Z=3)
    score = shape_score[instance[-1]]
    if does_win(instance):
        score += 6
    elif is_draw(instance):
        score += 3
    return score


def total_score_puzzle1(cases=["A Y", "B X", "C Z"]):
    scores = map(scorer, cases)
    return sum(scores)


def total_score_puzzle2(cases=["A Y", "B X", "C Z"]):
    """
    X lose
    Y draw
    Z win
    """
    transform = {
        "A X": "A Z",
        "A Y": "A X",
        "A Z": "A Y",
        "B X": "B X",
        "B Y": "B Y",
        "B Z": "B Z",
        "C X": "C Y",
        "C Y": "C Z",
        "C Z": "C X",
    }
    cases = map(transform.get, cases)
    scores = map(scorer, cases)
    return sum(scores)


if __name__ == "__main__":
    assert total_score_puzzle1() == 15
    assert total_score_puzzle1(given_cases) == 13005
    assert total_score_puzzle2() == 12
    assert total_score_puzzle2(given_cases) == 11373
