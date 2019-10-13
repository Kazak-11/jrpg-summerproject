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
          x = coords[0]
          y = coords[1]
        else:
          coords = list(int(i+s[a-1].strip().split(","))
          x = coords[0]
          y = coords[1]
          o.update({"move", [x, y]})
  def __init__(self, name, desc, requirements, reward):
    self.name = name
    self.desc = desc
    self.requirements = requirements
    self.reward = reward
