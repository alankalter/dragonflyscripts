from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic)
release = Key("shift:up, ctrl:up")
grammar = Grammar("line")

rules = MappingRule(
    name = "line",
    mapping = {     


"line <n>": release + Key("c-g") + Text("%(n)d") + Key("enter"),
"num <n>" : Text("%(n)s"),
"line <p> hundred": release + Key("c-g") + Text("%(p)d00") + Key("enter"),
"num <p>" : Text("%(p)s"),
"line <n> oh <p>" : Key("c-g") + Text("%(n)d0%(p)d") + Key("enter"),
"num <n> oh <p>" : Text("%(n)d0%(p)d"),
"line <n> <q>" : Key("c-g") + Text("%(n)d%(q)d") + Key("enter"),
"num <n> <q>" : Text("%(n)d%(q)d"),
"line <n> thousand": release + Key("c-g") + Text("%(n)d000") + Key("enter"),
"num <n> thousand" : Text("%(n)d000"),
"line <n> thousand <p>": release + Key("c-g") + Text("%(n)d00%(p)d") + Key("enter"),
"num <n> thousand" : Text("%(n)d00%(p)d"),
"line <n> thousand <q>": release + Key("c-g") + Text("%(n)d0%(q)d") + Key("enter"),
"num <n> thousand <q>" : Text("%(n)d0%(q)d"),
# Line 1..100        = {Ctrl+g} $1      {Enter};
# Line 1..9 Hundred  = {Ctrl+g} $1 00   {Enter};
# Line 1..99 Oh 1..9 = {Ctrl+g} $1 0 $2 {Enter};
# Line 1..99 10..99  = {Ctrl+g} $1 $2   {Enter};
# Line 1..9 Thousand = {ctrl+g} $1 000  {Enter};

      },
    extras = [
        Dictation("text"),
        Integer("n", 0, 100),
		Integer("p", 0, 10),
		Integer("q", 9, 100),
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
