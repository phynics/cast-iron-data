+++
id = "ref/carried/mythic-adventures/monsters/sphinx/mythic"
kind = "creature"
title = "Sphinx, Mythic"
source_ids = ["mythic-adventures"]
section = ["Monsters", "Sphinx"]
tags = ["magical beast", "mythic", "large"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Mythic Adventures/Monsters/Sphinx/Mythic", path = "mythic_adventures/creature/mythic/sphinx_mythic.json" },
]

[fields]
kind = "creature"
cr = "10"
creature_type = "Magical Beast"
subtypes = ["mythic"]
size = "Large"
alignment = "N"
ac = "25, touch 10, flat-footed 24 (+1 Dex, +15 natural, -1 size)"
hp = "142 (12d10+76)"
fortitude = "+11"
reflex = "+9"
will = "+10"
melee = "2 claws +18 (2d8+7/18-20)"
special_attacks = "mythic power (4/day, surge +1d8), pounce, rake (2 claws +18, 2d8+7/18-20), riddle, sphinx's curse"
abilities = ["24", "13", "16", "18", "19", "21"]
+++

::: statblock
CR: 10
XP: 9,600
Alignment: N
Size: Large
Type: Magical Beast (mythic)
Init: +5
Senses: [darkvision](ref/rule/darkvision) 60 ft., detect magic, [low-light vision](ref/rule/low-light-vision), see invisibility; Perception +21
AC: 25, touch 10, flat-footed 24 (+1 Dex, +15 natural, -1 size)
hp: 142 (12d10+76)
Fort: +11
Ref: +9
Will: +10
DR: 10/epic
Resist: electricity 30, fire 30
SR: 21
Speed: 40 ft., fly 60 ft. (poor)
Melee: 2 claws +18 (2d8+7/18-20)
Space: 10 ft.
Reach: 5 ft.
Special Attacks: mythic power (4/day, surge +1d8), pounce, rake (2 claws +18, 2d8+7/18-20), riddle, sphinx's curse
Spell-like abilities: (CL 12th; concentration +17)\
Constant-_[comprehend languages](ref/spell/comprehend-languages)_, _[detect magic](ref/spell/detect-magic)_, _[read magic](ref/spell/read-magic)_, _[see invisibility](ref/spell/see-invisibility)_, _[tongues](ref/spell/tongues)_\
At will-_[statue](ref/spell/statue)_ (self only)\
3/day-_[clairaudience/clairvoyance](ref/spell/clairaudience-clairvoyance)_, _[feeblemind](ref/spell/feeblemind)_ (DC 20)\
1/day-_[greater dispel magic](ref/spell/dispel-magic-greater)_, _[legend lore](ref/spell/legend-lore)_, _[locate object](ref/spell/locate-object)_, _[remove curse](ref/spell/remove-curse)_\
1/week-any one of the following (all symbols last for 1 week maximum): _[symbol of fear](ref/spell/symbol-of-fear)_ (DC 21), _[symbol of pain](ref/spell/symbol-of-pain)_ (DC 20), _[symbol of persuasion](ref/spell/symbol-of-persuasion)_ (DC 21), _[symbol of sleep](ref/spell/symbol-of-sleep)_ (DC 20), _[symbol of stunning](ref/spell/symbol-of-stunning)_ (DC 22)
Ability Scores: Str 24, Dex 13, Con 16, Int 18, Wis 19, Cha 21
Base Atk: +12
CMB: +20
CMD: 31 (35 vs. trip)
Feats: Alertness, Combat Casting, Hover, Improved Critical (claws)M, Improved Initiative, Iron WillM
Skills: Bluff +15, Diplomacy +15, Fly +7, Intimidate +15, Knowledge (any two) +6, Perception +21, Sense Motive +19, Spellcraft +12
Languages: Common, Draconic, Sphinx; comprehend languages, read magic, tongues
Environment: warm deserts and hills
Organization: solitary, pair, or cult (3-6)
Treasure: double
MR: 4
:::

_This woman has the upper body of a human queen, the lower body of a lion, a snake-headed tail, and
great eagle wings._

## Special Abilities {#special-abilities}

### Riddle {#riddle}

::: statblock
Ability Type: Supernatural
:::

A mythic sphinx can expend one use of mythic power to ask a riddle of up to 12 creatures within 100
feet. Each creature is compelled (Will DC 21 negates) to give an answer within 1 minute (creatures
in combat when the sphinx uses this ability gain a +4 bonus on the saving throw). The sphinx gets a
+4 bonus on attack rolls, damage rolls, and saving throws against any creature that refuses to
answer (via a successful saving throw), can't answer (including if it's in an area of silence),
answers incorrectly, or flees the sphinx instead of answering. The bonuses from failing to solve the
riddle last for 24 hours. The need to answer is a compulsion, mind-affecting, language-dependent
enchantment effect. The save DC is Charisma-based.

### Sphinx's Curse {#sphinxs-curse}

::: statblock
Ability Type: Supernatural
:::

A mythic sphinx can expend one use of mythic power when it damages an opponent with a claw attack to
curse its opponent with bleeding wounds (Will DC 21 negates). Whenever a cursed target takes
piercing or slashing damage, it takes 1d6 points of bleed damage every round for the next 1d6
rounds. This bleed damage stacks with itself and with all other bleed effects. A creature that
strikes the killing blow against a mythic sphinx must succeed at a saving throw or become cursed
(this requires no uses of mythic power from the sphinx). The save DC is Charisma-based.

A mythic sphinx is often given a task by a deity, such as watching over a city, testing a great
mortal hero, or guarding an artifact. She is gifted with magic to compel obedience and curse those
who would defy her commands or interfere with her task.
