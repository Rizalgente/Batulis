from .models import Post

choice = Kelompok.objects.all().values_list('kelompok', 'kelompok')

choice_list = []
for item in choice:
    choice_list.append(item)