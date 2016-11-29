import imdb
import imdbpie
import sys
import woodsy

ia_pie = imdbpie.Imdb()

actor_dict = {}
actor_list_one = []

pie_id_one = woodsy.retrive_movie_pie(ia_pie)

media_obj_one = ia_pie.get_title_by_id(pie_id_one)
actors_one_raw = woodsy.get_full_cast(ia_pie, pie_id_one)

actor_list_two = []
pie_id_two = woodsy.retrive_movie_pie(ia_pie)

media_obj_two = ia_pie.get_title_by_id(pie_id_two)
actors_two_raw = woodsy.get_full_cast(ia_pie, pie_id_two)

print set(actors_one_raw).intersection(actors_two_raw)


# #woodsy.get_right_actors_in_right_api(ia,actors_one_raw,actor_list_one,media_obj_one)
# media_obj_two = woodsy.retrive_movie(ia)
# print media_obj_two
# pie_id_two = woodsy.find_pie_match(ia_pie, media_obj_two['title'], int(media_obj_two['year']))
# pie_obj_two = ia_pie.get_title_by_id(pie_id_two)
#
# actors_two_raw = woodsy.get_full_cast(ia_pie, pie_id_two)
#
# print set(actors_one_raw).intersection(actors_two_raw)

#woodsy.get_right_actors_in_right_api(ia,actors_two_raw,actor_list,media_obj_two)

#for key in actor_dict.keys():
#   if len(actor_dict[key]) > 1:

# media_obj_two = woodsy.retrive_movie(ia)
# print media_obj_one
# pie_id_two = woodsy.find_pie_match(ia_pie, media_obj_two['title'], int(media_obj_two['year']))
# pie_obj_two = ia_pie.get_title_by_id(pie_id_two)



# actors_one = get_actors(media_obj_one)
# actors_two = get_actors(media_obj_two)
# media_one_filmograhpy = []
# media_two_filmograhpy = []
#








# for actor in actors_one:
#    full_person = ia.get_person(actor.getID(), info=["filmography"])
#    try:
#       results = full_person["actor"]
#       print full_person
#    except KeyError:
#       results = full_person["actress"]
#    for result in results:
#       if result == media_obj_two:
#          if actor in actor_dict:
#             actor_dict[actor].append(result)
#          else:
#             actor_dict[actor] = [result]
# print ''
# for key in actor_dict.keys():
#    print key, actor_dict[key]
