from gendiff.generate_diff import generate_diff


PATH_TO_ANSWER = "tests/fixtures/answer.txt"


def test_yaml():
    result = generate_diff(
             'tests/fixtures/file1.yml',
             'tests/fixtures/file2.yml'
             )
    f = open(PATH_TO_ANSWER)
    answer = f.read()[:-1]
    assert result == answer
