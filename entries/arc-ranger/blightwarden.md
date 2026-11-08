+++
id = "ref/arc-ranger/blightwarden"
kind = "archetype"
title = "Blightwarden"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blightwarden", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]

[fields]
kind = "archetype"
replaces = ["Wild empathy", "1st favored terrain", "Endurance"]
alters = ["Favored enemy", "Favored terrain"]
+++

**Sources:** People of the Wastes pg 17\
Some rangers feel so closely connected to their homelands that they stand as guardians against
pervasive corruptions that pervert those lands beyond the point of recognition.

**Hunt the Blighted (Ex)**

**Alters:** Favored enemy

**Info:** A blightwarden's first _favored enemy_ is always a special type of creature: _blighted._
His bonuses from his first _favored enemy_ apply to creatures with one or more of the following
templates: [blighted fey](ref/template/blighted-fey),
[fungal creature](ref/template/fungal-creature), [fungoid](ref/template/fungoid),
[Mana Wastes mutant](ref/template/mana-wastes-mutant), [mutant](ref/template/mutant),
[mutant goblin](ref/template/mutant-goblin), and [plagued beast](ref/template/plagued-beast).
Additionally, the bonuses apply against creatures with the [blight](ref/subtype/blight) subtype.

**Special:** Each time the blightwarden gains a new _favored enemy,_ his additional +2 bonus always
applies to this first _favored enemy._

**Emulate Taint (Ex, Su, or Sp)**

**Action:** Standard Action

**Replaces:** Wild empathy

Once per day, a blightwarden can examine visible evidence of a creature that has been affected by a
natural or supernatural blight. This might include visible tracks left by a creature with the
_fungal creature_ template, or a dead creature with the _blighted fey_ template, or any similar
evidence left by any creature as described in the _hunt the blighted_ ability.

When the blightwarden does this, for the next 24 hours, he can use any one extraordinary,
supernatural, or [spell-like ability](ref/umr/spell-like-abilities) granted by the template (or the
_[blight](ref/spell/blight)_ subtype) for a number of minutes equal to his ranger level. This
duration need not be used all at once, but they must be spent in 1-minute increments. Saving throw
DCs for this ability are calculated as if the blightwarden had the relevant template (for example,
the DC of an ability from the _blighted fey_ template would be equal to 10 + half the blightwarden's
Hit Dice + his Constitution modifier). He cannot use abilities that would create a permanent effect
beyond this ability's duration, and can never use more than one ability from a template or subtype
in this way during a single 24-hour period.

For example, the blightwarden cannot use a blighted ooze's _cursed domain_ ability to create a
_domain of evil._ However, the blightwarden could gain a _blighted fey's thorn throw_ ability for a
number of minutes equal to his ranger level (in this case, the blightwarden would gain a thorn
attack for that duration).

**Blightwalker (Ex)**

**Alters:** Favored terrain

**Choice:** The blightwarden can choose to improve this bonus in place of improving a _favored
terrain_ bonus.

**Gained:** At 3rd Level

**Passive:** A blightwarden gains a +2 bonus on initiative checks and Knowledge (geography),
Perception, Stealth, and Survival checks when in areas afflicted by a natural or supernatural
blight. In addition, the blightwarden adds this bonus to ability checks, saving throws, and skill
checks to avoid natural and supernatural hazards in blighted areas. A blightwarden traveling through
blighted areas leaves no trail and cannot be tracked (though he can leave a trail if he chooses).

**Replaces:** 1st favored terrain

**Special:** Blighted areas include [cursed lands](ref/rule/cursed-land),
[domains of evil](ref/rule/domains-of-evil), regions negatively affected by a spell or ability that
affects at least a 300-square-foot area, or regions where a specific
[affliction](ref/rule/afflictions) is prevalent.

**Resist Corruption (Ex)**

**Gained:** At 3rd Level

**Passive:** A blightwarden gains a +2 bonus on saving throws against curses, diseases,
mind-affecting effects, poisons, and transmutation effects.

**Replaces:** Endurance
