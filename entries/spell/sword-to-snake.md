+++
id = "ref/spell/sword-to-snake"
kind = "spell"
title = "Sword to Snake"
aon = "SpellDisplay.aspx?ItemName=Sword%20to%20Snake"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sword_to_snake", path = "json/spells10.json" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "29"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["poison"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a hair from a spider)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one Medium or smaller item" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Cleric, Druid, Hunter, Oracle, Shaman, Sorcerer, Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a hair from a spider)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one Medium or smaller item
Descriptors: poison
:::

When you make an undulating gesture using your hand, the target item changes slightly in shape and
appearance to resemble a cross between its original form and that of a venomous animal. For example,
a staff might change to resemble a snake, a shield might change to resemble an enormous venomous
beetle, or the hilt of a sword might change to resemble a scorpion's tail.

If this spell is cast on a held item, the wielder adds his Will save bonus to the saving throw. You
must be able to see the item to cast this spell on it.

The item retains all its properties, but whenever a creature picks up, attacks with, activates, or
otherwise manipulates the item (with the exception of dropping the item) after this spell is cast,
it animates and bites the creature. The attack is resolved before the action that triggered it. This
spell otherwise does not affect the creature's ability to use the item.

If the item is a nonmagical weapon, it has an attack bonus equal to your caster level plus your
spellcasting ability score modifier, and its attack deals 1d4 points of piercing damage. If the
target item is a magic weapon, it retains any magical qualities, and its enhancement bonus is still
added to both the attack roll and the damage roll.

A creature that takes damage from the bite is affected as if by a
[venomous snake's poison](ref/eq-poison/black-adder-venom). The poison's save DC is equal to this
spell's DC.
