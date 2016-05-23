from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)
release = Key("shift:up, ctrl:up")
grammar = Grammar("line")

rules = MappingRule(
    name = "line",
    mapping = {     


"line <n>": release + Key("c-g") + Text("%(n)d") + Key("enter"),



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
