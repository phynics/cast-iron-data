+++
id = "ref/arc-witch/hagbound"
kind = "archetype"
title = "Hagbound"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Hagbound"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hagbound", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "blood-of-the-coven"
page = "16"

[fields]
kind = "archetype"
features = [
  { anchor = "hagbound" },
  { anchor = "hag-s-claws", level = 1 },
  { anchor = "hunched-muscle", level = 2 },
  { anchor = "vain-glamour", level = 4 },
  { anchor = "vile-curse", level = 10 },
  { anchor = "hag-transformation", level = 20 },
]
trades = [
  { replaces = "Hex gained at 1st level", feature = "hex", levels = [1], by = ["hag-s-claws"] },
  { replaces = "The hexes gained at 2nd, 8th, and 14th levels", feature = "hex", levels = [2, 8, 14], by = ["hunched-muscle"] },
  { replaces = "The hexes gained at 4th and 12th levels", feature = "hex", levels = [4, 12], by = ["vain-glamour"] },
  { replaces = "Hex gained at 10th level", feature = "hex", levels = [10], by = ["vile-curse"] },
  { replaces = "Hex gained at 20th level", feature = "hex", levels = [20], by = ["hag-transformation"] },
]
+++

Whether a [changeling](ref/race/changeling) in the process of succumbing to her mother's call, a
witch cursed by a hag to become her instrument of torment, a vain and petty witch overeager for
power, or some other unfortunate soul, a hagbound witch finds its soul has been infected by a hag's
spite and powerful, corrupt arcane magic. Her mind and body begin to transform to reflect her new
being. Hagbound witches suffer a slow transformative taint that is similar to the
[accursed corruption](ref/rule/accursed) and make ideal candidates for this additional power—and
tragedy.

## Hagbound {#hagbound}

A hagbound can take this archetype only if her first character level is a witch level, and she must
select one of the following patrons: [Deception](ref/patron/deception), [Jynx](ref/patron/jynx) (see
Witch Patron Themes on page 17), [Moon](ref/patron/moon), [Occult](ref/patron/occult),
[Plague](ref/patron/plague), [Shadow](ref/patron/shadow), [Strength](ref/patron/strength),
[Vengeance](ref/patron/vengeance), or [Winter](ref/patron/winter). She can escape her inevitable
fate only by removing the hag's hold on her soul, typically with _[miracle](ref/spell/miracle)_ or
an effect of similar power. Until then, she can't take levels in any class other than witch and her
alignment can never become good. Removing the hag's hold causes her to lose this archetype and
become a normal witch.

## Hag's Claws (Ex) {#hag-s-claws}

A hagbound's hands grow into a pair of [hideous claws](ref/umr/natural-attacks) that deal 1d4 points
of damage for a Medium hagbound (1d3 for a Small creature).

This replaces the hex gained at 1st level.

## Hunched Muscle (Ex) {#hunched-muscle}

At 2nd level, warty growths and knobby muscles twist the hagbound's body. She gains a +2 size bonus
to her Strength score. This bonus increases by 2 at 8th level and 14th level, to a maximum of +6.

This replaces the hexes gained at 2nd, 8th, and 14th levels.

## Vain Glamour (Sp) {#vain-glamour}

At 4th level, the hagbound gains the ability to disguise her hideous form behind various pleasing
shapes. This allows her to magically disguise herself at will, as per
_[disguise self](ref/spell/disguise-self)_. At 12th level, she can transform herself at will rather
than spin illusions, as per _[alter self](ref/spell/alter-self)_.

This replaces the hexes gained at 4th and 12th levels.

## Vile Curse (Sp) {#vile-curse}

At 10th level, the hagbound becomes exceptionally skilled at cursing others. She can cast
_[bestow curse](ref/spell/bestow-curse)_ at will, but its duration becomes 24 hours. Once a creature
has been affected by this ability, it is immune to the witch's vile curse ability for 24 hours. If
the witch learns some secret fear or vulnerability of her target and tailors the curse to exploit
this, her target takes a -2 penalty on its Will saving throw against the effect.

This replaces the hex gained at 10th level.

## Hag Transformation {#hag-transformation}

At 20th level, the hagbound transforms into a true hag, purging all goodness and light from her in
exchange for dark power. Her alignment becomes evil if it isn't already. Her type changes to
[monstrous humanoid](ref/type/monstrous-humanoid), and she gains [darkvision](ref/rule/darkvision)
60 feet; immunity to charm, fear, and spell effects; and the ability to join a coven. She gains
[spell resistance](ref/rule/spell-resistance) 31, and she grants this benefit to her other coven
members.

This replaces the hex gained at 20th level.
