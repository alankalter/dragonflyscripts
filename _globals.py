from dragonfly import (Grammar, FocusWindow, MappingRule, Key, Config, Section, Item, Playback, Mimic, Mouse, Text)

rules = MappingRule(
	name = "general",
	mapping = { 
		"slap": Key("enter"),
		"Max when": Key("w-up"),
		"left when": Key("w-left"),
		"right when": Key("w-right"),
		"min win": Key("w-down"),
    "switch apps": Key("alt:down, tab"),
		"switch app": Key("a-tab/10"),
	"search tabs": Key("ctrl:down, tab"),
	"free": Key("alt:up") + Key("shift:up") + Key("ctrl:up"),
    # "termi": Key("w-b/10, s-tab/10, enter"),
    "foxy": Key("w-b/10, s-tab/10, right:1/10, enter"),
    "foxy reload": Key("w-b/10, s-tab/10, right:1/10, enter/10, f5"),
    "Jimmy": Key("w-b/10, s-tab/10, right:2/10, enter"), 
    "Heidi": Key("w-b/10, s-tab/10, right:3/10, enter"),
    "chrome": Key("w-b/10, s-tab/10, right:4/10, enter"),
    "chrome reload": Key("w-b/10, s-tab/10, right:4/10, enter/10, f5"),
    "bashing": Key("w-b/10, s-tab/10, right:5/10, enter"),
    "como": Mimic("\\no-caps-on") + Mimic("\\no-space-on"),
	"escape": Key('escape'),
	"switch tab": Key('c-tab'),
	"new one": Key('c-n'),
	"click": Mouse('left'),
	"rye click": Mouse('right'),	
	"dee click": Mouse('left:2'),
	"get password": Text('Laikathed0g'),
	"block": Key("f6"),
	"address bar": Key ("a-d"),
	"logout of computer":  Key ("w-l/10"),
	"crack": Key("s-f10")  + Key("down"),
	"open file" : Key("c-o"),
	"logout" : Mimic("press windows ell")
	# svn
	
	}
)

grammar = Grammar("general")
grammar.add_rule(rules)
grammar.load()

def unload():
  global grammar
  if grammar: grammar.unload()
  grammar = None
  