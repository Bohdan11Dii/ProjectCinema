menu = [
    {
        'title':'Головна сторінка'
    },
    {
        'title': 'Афіша'
    },
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context

