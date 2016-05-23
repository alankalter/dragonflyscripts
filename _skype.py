from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)

context = AppContext(executable="skype")
grammar = Grammar("Skype", context=context)
noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")
release = Key("shift:up, ctrl:up")

rules = MappingRule(
    name = "Skype",
    mapping = {     
"list": Key("a-2"),
"talk" : Key("s-tab:3"),
"focus": Key("enter") + Key("s-tab:3"),
      },
    extras = [
        Dictation("text"),
        Integer("n", 0, 20000),
      ],
    defaults = {
      "n" : 1
      }
    )

grammar.add_rule(rules)

grammar.load()

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
