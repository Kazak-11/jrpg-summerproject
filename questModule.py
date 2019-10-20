class Quest: # Класс квестов
  quest_name = ""
  quest_desc = ""
  quest_requirements = []
  quest_reward = ""
  def parse_arr(arr): # Парсер строки с триггерами выполнения
    spreadsheet = ""
    for i in arr:
      i_s = i.split(" ")
      o = {}
      if "move" in i_s:
        a = i_s.index("move")
        if a % 2 == 0:
          coords = list(int(i_s[a+1].strip().split(","))
          o.update({"move", coords})
        else:
          coords = list(int(i+s[a-1].strip().split(","))
          o.update({"move", coords})
      elif "have_an_items" in i_s:
        a = i_s.index("have_an_items")
        if a % 2 == 0:
          items_ = list(int(i_s[a+1].strip().split(",")))
          o.update({"have_an_items", items})
        else:
          items_ = list(int(i_s[a-1].strip().split(",")))
          o.update({"have_an_items", items})
      return o
  def __init__(self, name, desc, requirements, reward):
    self.name = name
    self.desc = desc
    self.requirements = requirements
    self.reward = reward
