from urllib import response
from model.model import Ormdb

class WinnersUseCase:
    def execute(self, orm: Ormdb):
        movies = orm.get_all()
        producers = []

        for movie in movies:
            if "winner" in movie and movie["winner"] == "yes":
                exists_producer = False
                for producer in producers:
                    if producer["producer"] == movie["producers"]:
                        producer["years_win"].append(int(movie["year"]))
                        exists_producer = True
                if not exists_producer:
                    producers.append({"producer": movie["producers"], "years_win": [int(movie["year"])] })
        
        r = self.__get_win_interval(producers)
        return r
    
    def __get_win_interval(self, producers):
        respons = {"min":[], "max":[]}
        for producer in producers:
            max_form_producer = {"producer": producer["producer"], "interval":0, "previousWin": 0, "followingWin":0}
            min_form_producer = {"producer": producer["producer"], "interval":0, "previousWin": 0, "followingWin":0}
            if len(producer["years_win"])> 1:
                for year in producer["years_win"]:
                    for i in range(0, len(producer["years_win"])):
                        dif = year - producer["years_win"][i]
                        if dif > 0:
                            max_interval = max_form_producer["interval"]
                            min_interval = min_form_producer["interval"]
                            if not max_interval or dif > max_interval:
                                max_form_producer["interval"] = dif
                                max_form_producer["previousWin"] = producer["years_win"][i]
                                max_form_producer["followingWin"] = year
                            
                            if not min_interval or dif > min_interval:
                                min_form_producer["interval"] = dif
                                min_form_producer["previousWin"] = producer["years_win"][i]
                                min_form_producer["followingWin"] = year
            
            if max_form_producer["interval"]:
                if not respons["max"]:
                    respons["max"].append(max_form_producer)
                else:
                    if respons["max"][0]["interval"] == max_form_producer["interval"]:
                        respons["max"].append(max_form_producer)
                    elif max_form_producer["interval"] > respons["max"][0]["interval"]:
                        respons["max"].clear()
                        respons["max"].append(max_form_producer)

            if min_form_producer["interval"]:
                if not respons["min"]:
                    respons["min"].append(min_form_producer)
                else:
                    if respons["min"][0]["interval"] == min_form_producer["interval"]:
                        respons["min"].append(min_form_producer)
                    elif min_form_producer["interval"] > respons["min"][0]["interval"]:
                        respons["min"].clear()
                        respons["min"].append(min_form_producer)

        return respons
