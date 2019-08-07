import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#execute API calls and execute responses
url = "https://api.github.com/search/repositories?q=language:python&sord=stars"
r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()

print("Total repositories:",response_dict["total_count"])

#explore information about the repository
repo_dicts = response_dict["items"]
print("Repositories returned", len(repo_dicts))

"""
#research the first repository
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
#for key in sorted(repo_dict.keys()):
for key in repo_dict.keys():
    print(key)

print("\nselected information about first repository.")
print("Name:", repo_dict["name"])
print("Owner:", repo_dict["owner"]["login"])
print("Stars:", repo_dict["stargazers_count"])
"""
def description(repo_dict_json):
    description_str = repo_dict_json["description"]
    if description_str:
        return description_str
    else:
        return ""

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict["name"])
    plot_dict = {
        "value":repo_dict["stargazers_count"],
        "label":description(repo_dict),
        "xlink":repo_dict["html_url"]
    }
    plot_dicts.append(plot_dict)

#visualization
my_style = LS("#333366", base_style=LCS)

#create a configuration object
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = True
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

#chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('stars',plot_dicts)
chart.render_to_file("API17/python_repos.svg")

