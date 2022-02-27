import requests

def hero_requests(hero_list, TOKEN = "2619421814940190"):
    intel_dic = {}
    for name in hero_list:
        url = f"https://superheroapi.com/api/{TOKEN}/search/{name}"
        response = requests.get(url)
        h_list = response.json().get('results')
        intel_val = h_list[0].get("powerstats")
        intel_dic.update({int(intel_val.get("intelligence")):name})
        max_int = max(list(intel_dic.keys()))
    hero_name = intel_dic.get(max_int)
    print(f"Самый умный герой {hero_name}.\nЕго уровень интеллекта {max_int}.")
    

    
hero_list = ["Hulk", "Captain America", "Thanos"]
hero_requests(hero_list)
