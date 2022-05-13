# %%
import json
# %%
record_dict = {
"normal": {
"rock" : 0.625,
"ghost" : 0.391,
"steel" : 0.625,
},
"fire": {
"fire" : 0.625,
"water" : 0.625,
"grass" : 1.600,
"ice" : 1.600,
"bug" : 1.600,
"rock" : 0.625,
"dragon" : 0.625,
"steel" : 1.600,
},
"water": {
"fire" : 1.600,
"water" : 0.625,
"grass" : 0.625,
"earth" : 1.600,
"rock" : 1.600,
"dragon" : 0.625,
},
"grass": {
"fire" : 0.625,
"water" : 1.600,
"grass" : 0.625,
"poison" : 0.625,
"earth" : 1.600,
"flying" : 0.625,
"bug" : 0.625,
"rock" : 1.600,
"dragon" : 0.625,
"steel" : 0.625,
},
"electric": {
"water" : 1.600,
"grass" : 0.625,
"electric": 0.625,
"earth" : 0.391,
"flying" : 1.600,
"dragon" : 0.625,
},
"ice": {
"fire" : 0.625,
"water" : 0.625,
"grass" : 1.600,
"ice" : 0.625,
"earth" : 1.600,
"flying" : 1.600,
"dragon" : 1.600,
"steel" : 0.625,
},
"fighting": {
"normal" : 1.600,
"ice" : 1.600,
"poison" : 0.625,
"flying" : 0.625,
"psychic" : 0.625,
"bug" : 0.625,
"rock" : 1.600,
"ghost" : 0.391,
"dark" : 1.600,
"steel" : 1.600,
"fairy" : 0.625,
},
"poison": {
"grass" : 1.600,
"poison" : 0.625,
"earth" : 0.625,
"rock" : 0.625,
"ghost" : 0.625,
"steel" : 0.391,
"fairy" : 1.600,
},
"earth": {
"fire" : 1.600,
"grass" : 0.625,
"electric": 1.600,
"poison" : 1.600,
"flying" : 0.391,
"bug" : 0.625,
"rock" : 1.600,
"steel" : 1.600,
},
"flying": {
"grass" : 1.600,
"electric": 0.625,
"fighting": 1.600,
"bug" : 1.600,
"rock" : 0.625,
"steel" : 0.625,
},
"psychic": {
"fighting": 1.600,
"poison" : 1.600,
"psychic" : 0.625,
"dark" : 0.391,
"steel" : 0.625,
},
"bug": {
"fire" : 0.625,
"grass" : 1.600,
"fighting": 0.625,
"poison" : 0.625,
"flying" : 0.625,
"psychic" : 1.600,
"ghost" : 0.625,
"dark" : 1.600,
"steel" : 0.625,
"fairy" : 0.625,
},
"rock": {
"fire" : 1.600,
"ice" : 1.600,
"fighting": 0.625,
"earth" : 0.625,
"flying" : 1.600,
"bug" : 1.600,
"steel" : 0.625,
},
"ghost": {
"normal" : 0.391,
"psychic" : 1.600,
"ghost" : 1.600,
"dark" : 0.625,
},
"dragon": {
"dragon" : 1.600,
"steel" : 0.625,
"fairy" : 0.391,
},
"dark": {
"fighting": 0.625,
"psychic" : 1.600,
"ghost" : 1.600,
"dark" : 0.625,
"fairy" : 0.625,
},
"steel": {
"fire" : 0.625,
"water" : 0.625,
"electric": 0.625,
"ice" : 1.600,
"rock" : 1.600,
"steel" : 0.625,
"fairy" : 1.600,
},
"fairy": {
"fire" : 0.625,
"fighting": 1.600,
"poison" : 0.625,
"dragon" : 1.600,
"dark" : 1.600,
"steel" : 0.625,
},
}
# %%
emoji_dict = {
'normal' : "🙂",
'fire' : "🔥",
'water' : "🌊",
'grass' : "🍀",
'electric': "⚡",
'ice' : "❄️",
'fighting': "🥊",
'poison' : "🤮",
'earth' : "⛰️",
'flying' : "🕊️",
'psychic' : "😵‍💫",
'bug' : "🪲",
'rock' : "🪨",
'ghost' : "👻",
'dragon' : "🐉",
'dark' : "🌒",
'steel' : "🧲",
'fairy' : "🧚‍♂️"
}
# %%
header_list = [0.391,0.625,1.600]
# %%
multiplier_dict = dict()
for key_str,value_dict in record_dict.items():
    contain_dict = dict()
    for value_str, value_int in value_dict.items():
        value_list = contain_dict.get(value_int,list())
        value_list.append(value_str)
        contain_dict[value_int] = value_list
    multiplier_dict[key_str] = contain_dict
# %%
reverse_dict = dict()
for key_str,value_dict in record_dict.items():
    for value_str, value_int in value_dict.items():
        contain_value_dict = reverse_dict.get(value_str,dict())
        contain_key_list = contain_value_dict.get(value_int,list())
        contain_key_list.append(key_str)
        contain_value_dict[value_int] = contain_key_list
        reverse_dict[value_str] = contain_value_dict
# %%
index_dict = dict()
line_list = list()
emoji_list = list()
for center_str, mv_dict in multiplier_dict.items(): # multiplier_value_dict
    rv_dict = reverse_dict[center_str] # reverse_value_dict
    # reverse_header_list = sorted(list(reverse_value_dict.keys()))
    # multiplier_header_list = sorted(list(multiplier_value_dict.keys()),reverse=True)
    rh_list = sorted(header_list) # reverse_header_list
    mh_list = sorted(header_list,reverse=True) # multiplier_header_list
    # print(reverse_header_list,center_str,multiplier_header_list)
    # print(center_str,":",[rv_dict.get(n,list()) for n in rh_list],center_str,[mv_dict.get(n,list()) for n in mh_list])
    single_line_list = [rv_dict.get(n,["_"]) for n in rh_list]+[[center_str,center_str.capitalize()]]+[mv_dict.get(n,["_"]) for n in mh_list]
    single_emoji_list = [[emoji_dict.get(k,k) for k in n] for n in single_line_list]
    line_list.append("\t".join(["".join(n) for n in single_line_list]))
    emoji_list.append(" | ".join([" ".join(n) for n in single_emoji_list]))
    index_dict[center_str] = {
        "defense from": rv_dict,
        "attack on": mv_dict
    }
# %%
with open("record.json",'w') as target_handle:
    json.dump(record_dict,target_handle,indent=0)
with open("index.json",'w') as target_handle:
    json.dump(index_dict,target_handle,indent=0)
with open("data.txt",'w') as target_handle:
    target_handle.write("\t".join([str(n) for n in rh_list+["Type"]+mh_list])+"\n")
    target_handle.write("\n".join(line_list)+"\n")
with open("emoji.md",'w') as target_handle:
    target_handle.write("# Pokémon Go Type Effectiveness\n\n")
    target_handle.write(" | ".join([str(n) for n in rh_list+["Type"]+mh_list])+"\n")
    target_handle.write("|".join(['-----' for n in rh_list+["Type"]+mh_list])+"\n")
    target_handle.write("\n".join(emoji_list)+"\n")
# %%
