

import imdbpie

def retrive_movie_pie(imdb_object):
   media = raw_input("enter the title of the media:")
   print ''
   s_result = imdb_object.search_for_title(media)
   movie_dict = {}
   for n,item in enumerate(s_result):
      movie_dict[n+1] = [item['title'], item['year'], item['imdb_id']]
      if n >= 5:
         break
   print 'Id', '     **movie name**\n'
   for key in movie_dict.keys():
      print key, '     ', movie_dict[key][0], movie_dict[key][1], movie_dict[key][2]
   selected_id = int(raw_input('Enter Id for correct title'))
   movie_one_id = movie_dict[selected_id][2]
   return movie_one_id


def retrive_movie(imdb_object):
   import imdb
   media = raw_input("enter the title of the media:")
   print ''
   s_result = imdb_object.search_movie(media)
   movie_dict = {}
   for n,item in enumerate(s_result):
      movie_dict[n+1] = [item['long imdb canonical title'], item.movieID]
      if n >= 5:
         break
   print 'Id', '     **movie name**\n'
   for key in movie_dict.keys():
      print key, '     ', movie_dict[key][0], movie_dict[key][1]
   selected_id = int(raw_input('Enter Id for correct title'))
   movie_one_id = movie_dict[selected_id][1]
   selected_media_one = imdb_object.get_movie(movie_one_id)
   return selected_media_one


def get_full_cast(imdbpie_object, pie_id):
   actor_list = []
   title = imdbpie_object.get_title_by_id(pie_id)
   for person in title.credits:
      # check if they are a writer
      if person.token == 'cast':
         print(person.name + ' is am actor')
         actor_list.append(person.name)
   return actor_list

def find_pie_match(pie_object, title, year):
   options = pie_object.search_for_title(title)
   for option in options:
      if int(option['year']) == year:
         return option['imdb_id']
   else:
      return 'No Matching movie in alt api'

def get_right_actors_in_right_api(imdb_obj, raw_actors_list, actor_list,media_obj):
   for actor in raw_actors_list:
      right_actor = False
      actor_obj = imdb_obj.search_person(actor)
      full_person = imdb_obj.get_person(actor_obj.getID(), info=["filmography"])
      try:
         results = full_person["actor"]
         print full_person
      except KeyError:
         results = full_person["actress"]
      for result in results:
         if result == media_obj:
            right_actor = True
            break
      if right_actor is True:
         actor_list.append(actor_obj)
         break
