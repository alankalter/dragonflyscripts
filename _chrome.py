from dragonfly import (Grammar, AppContext, MappingRule, Dictation, Key, Text, Integer, Mimic, Mouse)

context = AppContext(executable="chrome")
grammar = Grammar("chrome", context=context)
noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

rules = MappingRule(
    name = "chrome",
    mapping = {     
"edit": Key("w-a"),
"reload" : Key("f5"),
"open": Key("c-o"),
"jump": Key("f3"),
"new tab": Key("t"),
"search tabs": Key("c-tab"),
"find": Key("c-f"),
"console": Key("cs-j"),
# "inspect": Key("f12"),
"go back": Key("backspace"),
"show <n>": Key("c-%(n)d"),
"address": Key ("f6"),
"stop" : Key("escape"),
"inspect": Mouse("right/10") + Key("up") + Key("enter"),
"menu": Key("a-e"),
"history": Key("c-h"),
"panel": Key("c-rightbracket"),
"prepanel": Key("c-leftbracket"),
"incognito": Key("cs-n"),
"mobile view": Key("cs-m"),
"music": Key("as-p"),
"unsong": Key("as-comma"),
"song": Key("as-dot"),

'close tab': Key('c-w'),
	# 'open new tab': Key('c-t'),
        'duplicate tab': Key('y/25,t'),                  # vimium
        'reopen tab': Key('cs-t'),
        '[go to] next tab': Key('c-pgdown'),
        '[go to] previous tab': Key('c-pgup'),
        # 'go to tab <tab>': Key('c-%(tab)d'),
        # '[go to] first tab': Key('c-1'),
        # '[go to] last tab': Key('c-9'),
        # 'go back': Key('a-left'),
        'go forward': Key('a-right'),
        # 'go to address': Key('a-d'),
        # 'reload page': Key('f5'),
        'labels': Key('f'),                         # vimium
        'show labels in new tab': Key('s-f'),            # vimium
        '[go to] label <n>': Text('%(n)d'),    # vimium
        'duplicate tab': Key('y,t'),                     # vimium
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
