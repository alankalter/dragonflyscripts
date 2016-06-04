from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)

context = AppContext(executable="notepad++")
grammar = Grammar("notepadplusplus", context=context)
noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")
release = Key("shift:up, ctrl:up")

rules = MappingRule(
    name = "notepadplusplus",
    mapping = {     
"calm": Key("c-q"),
"decalm": Key("c-q"),
"lapse": Key("ca-f"),
"collapse all": Key("a-0"),
"close tab" : Key("c-w"),
# "prettify": Key("c-k") + Key("c-d"),
# "match": Key("c-rightbrace"),
# "close tab": Key ("c-f4"),
# "solution": Key("ca-l"),
# "go back": Key("c-minus"),
# "bookmark": Key("c-k") + Key("c-k"),
# "mark": Key("c-k") + Key("c-n"),
# "breakpoint": Key("f9"),
# "disable": Key("s-f9"),
# "step": Key("f11"),
# "big step": Key("f10"),
# "step out": Key("s-f11"),
# "definition": Key("f12"),
# "references": Key("s-f12"),
# "find and replace" : Key("c-h"),
# "replace [<n>]" : Key("a-r:%(n)d"),
# "search solution": Key("c-semicolon"),
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
