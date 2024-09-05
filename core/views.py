from django.shortcuts import render

# Create your views here.
import pickle
import os
from django.conf import settings
from django.shortcuts import render


movie_data_path = os.path.join(settings.BASE_DIR, 'movie_data.pkl')
similarity_matrix_path = os.path.join(settings.BASE_DIR, 'similarity_matrix.pkl')


with open(movie_data_path, 'rb') as f:
    new_df = pickle.load(f)

with open(similarity_matrix_path, 'rb') as f:
    similarity = pickle.load(f)

from django.http import JsonResponse

def movie_suggestions(request):
    query = request.GET.get('query', '')
    suggestions = new_df[new_df['title'].str.lower().str.contains(query.lower(), na=False)]['title'].tolist()
    return JsonResponse(suggestions, safe=False)



def recommend(movie):
    try:
        movie_index = new_df[new_df['title'] == movie].index[0]
        distance = similarity[movie_index]
        movies_list = sorted(list(enumerate(distance)), key=lambda x: x[1], reverse=True)[1:6]
        return [new_df.iloc[i[0]].title for i in movies_list]
    except IndexError:
        return ["Movie not found. Please check the name and try again."]


def recommend_movie(request):
    recommendation = None
    movie_name = None

    if request.method == 'POST':
        movie_name = request.POST.get('movie_name')
        if movie_name:
            # Use the `recommend` function
            recommendation = recommend(movie_name)

    return render(request, 'recommend_movie.html', {'movie_name': movie_name, 'recommendation': recommendation})
