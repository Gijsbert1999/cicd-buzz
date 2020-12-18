from buzz import generator


def test_sample_single_word():
    woorden_tuple = ('foo', 'bar', 'foobar')
    word = generator.sample(woorden_tuple)
    assert word in woorden_tuple

def test_sample_multiple_words():
    woorden_tuple = ('foo', 'bar', 'foobar')
    words = generator.sample(woorden_tuple, 2)
    assert len(words) == 2
    assert words[0] in woorden_tuple
    assert words[1] in woorden_tuple
    assert words[0] is not words[1]

def test_generate_buzz_of_at_least_five_words():
    phrase = generator.generate_buzz()
    assert len(phrase.split()) >= 5
