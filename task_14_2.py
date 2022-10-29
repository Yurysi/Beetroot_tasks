"""
    Write a decorator that takes a list of stop words and replaces them
    with * inside the decorated function

"""


def stop_words(words: list):
    def use_func(func):
        def wrapers(*args, **kwargs):
            sentence = func(*args, **kwargs)
            slogan = sentence.rstrip('!').split()

            for word in words:
                for i in range(len(slogan)):
                    if slogan[i] == word:
                        slogan[i] = '*'
            slogan.append('!')
            result = ' '.join(slogan)
            print(result)

            return slogan

        return wrapers

    return use_func


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


create_slogan("Steve")

# abc = "drinks pepsi in his brand new BMW!"
# v = abc.split()
# print(v)
# for a in v:
#     print(a)
