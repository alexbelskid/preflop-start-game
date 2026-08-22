from pathlib import Path

HTML = Path(__file__).parents[1].joinpath("index.html").read_text(encoding="utf-8")


def test_answer_buttons_do_not_reveal_the_correct_answer_before_choice():
    assert "class=\"action ${o.includes('Повыс')?'raise'" not in HTML
    assert "answer-correct" in HTML
    assert "answer-wrong" in HTML


def test_mobile_table_uses_inset_seats_not_negative_edges():
    assert ".s2{left:-3%" not in HTML
    assert ".s6{left:103%" not in HTML
    assert ".s2{left:8%" in HTML
    assert ".s6{left:92%" in HTML


def test_selected_answer_is_revealed_only_after_answering():
    answer_start = HTML.index("function answer(choice)")
    answer_end = HTML.index("function completedLessons()")
    answer_block = HTML[answer_start:answer_end]
    assert "answer-correct" in answer_block
    assert "answer-wrong" in answer_block
