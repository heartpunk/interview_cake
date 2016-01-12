from hypothesis import given
import hypothesis.strategies as st



def top_scores(scores, highest_possible_score):
    score_counts = [0] * (highest_possible_score + 1)

    for score in scores:
        score_counts[score] += 1

    ret = []

    for index, count in enumerate(score_counts):
        ret.extend([index] * count)

    return ret

@given(st.lists(st.integers(min_value=0), min_size=1))
def test_top_scores(scores):
    assert top_scores(scores, max(scores)) == sorted(scores)

test_top_scores()
