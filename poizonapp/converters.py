class FourDigitYearConverter:
    '''
    Конвертор для проверки ввода года (4 цифры)

    Приминение:
        register_converter(converters.FourDigitYearConverter, <'con_name'>)
        urlpatterns = [
            ...
            path('url/<con_name: year>/', views.<view>)
        ]
    '''
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%04d%' % value