from gendiff.generate_diff import generate_diff


PATH_TO_ANSWER = "tests/fixtures/answer_json.txt"

def test_json():
    result = generate_diff(
             'tests/fixtures/file1.json',
             'tests/fixtures/file2.json'
             )
    f = open(PATH_TO_ANSWER)
    answer = f.read()
    print('---')
    print(result)
    print('---')
    print(answer)
    print('---')
    assert result == answer
