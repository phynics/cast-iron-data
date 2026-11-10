+++
id = "ref/spell/emblem-of-greed"
kind = "spell"
title = "Emblem of Greed"
aon = "SpellDisplay.aspx?ItemName=Emblem%20of%20Greed"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "emblem_of_greed", path = "json/spells4.json" },
]
[[sources]]
publication = "arcane-anthology"
page = "20"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Medium", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 7 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a masterwork or magical melee weapon)"
range = "touch"
effects = [
  { label = "Target", value = "1 masterwork melee weapon touched" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Arcanist, Cleric, Inquisitor, Magus, Medium, Oracle, Sorcerer, Warpriest, Wizard\
7: Shaman
Casting time: 1 standard action
Components: V, S, M (a masterwork or magical melee weapon)
Range: touch
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: 1 masterwork melee weapon touched
Subschool: Polymorph
:::

You transform one melee weapon into a burning [glaive](ref/eq-weapon/glaive) similar to the ones
wielded by the runelords of old. The target of your spell must be a masterwork or magical melee
weapon appropriate to your size. The weapon becomes a glaive appropriate to your size and has a +1
enhancement bonus and the [flaming](ref/magic-enh/flaming) weapon special ability. When wielding the
glaive, you are considered proficient with it and use your caster level as your base attack bonus
(which may give you multiple attacks). When you reach caster level 14th, the glaive gains the
[spell-storing](ref/magic-enh/spell-storing) weapon special ability. When you reach caster level
17th, it loses the flaming weapon special ability, and gains the
[flaming burst](ref/magic-enh/flaming-burst) weapon special ability. The glaive's enhancement bonus
increases to +2 at caster level 15th, and +3 at caster level 19th.

If this spell is cast on a magic weapon, the powers of the spell supersede any that the weapon
normally has, rendering the normal enhancement bonus and powers of the weapon inoperative for the
duration of the spell. This spell is not cumulative with
[greater magic weapon](ref/spell/magic-weapon-greater) or any other spell that might modify the
weapon in any way. This spell does not work on artifacts. A masterwork weapon's bonus on attack
rolls does not stack with an enhancement bonus to attack.
