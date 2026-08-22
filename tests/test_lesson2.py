from pathlib import Path

HTML = Path(__file__).parents[1].joinpath("index.html").read_text(encoding="utf-8")


def test_course_has_second_lesson_and_persistent_progress():
    assert 'id="lessonSelect"' in HTML
    assert 'Урок 2' in HTML
    assert 'Кто уже вложил фишки' in HTML
    assert "localStorage" in HTML
    assert "completedLessons" in HTML


def test_second_lesson_has_at_least_eight_scenarios():
    marker = "const lesson2Scenarios="
    assert marker in HTML
    block = HTML.split(marker, 1)[1].split("];", 1)[0]
    assert block.count("{pos:") >= 8


def test_bet_state_is_part_of_each_lesson_two_scenario():
    marker = "const lesson2Scenarios="
    block = HTML.split(marker, 1)[1].split("];", 1)[0]
    assert block.count("bets:") >= 8
    assert block.count("action:") >= 8
