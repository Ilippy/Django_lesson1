class MySlug:
    regex = "[-a-zA-Z0-9а-яА-ЯёЁ_]+"

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value