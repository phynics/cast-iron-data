+++
id = "ref/spell/cleanse"
kind = "spell"
title = "Cleanse"
aon = "SpellDisplay.aspx?ItemName=Cleanse"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cleanse", path = "json/spells2.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "211"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Cleric, Oracle, Warpriest\
6: Inquisitor
Casting time: 1 standard action
Components: S, DF
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

Positive energy infuses and cleanses your body. This spell cures 4d8 points of damage + 1 point per
caster level (maximum +25) and ends any and all of the following adverse conditions affecting you:
ability damage, blinded, confused, dazzled, deafened, diseased, exhausted, fatigued, nauseated,
poisoned, and sickened. In addition, cleanse functions as
[break enchantment](ref/spell/break-enchantment) upon a single additional effect of your choice that
is affecting you and that can be legally affected by this effect.

If used by undead or other creatures healed by negative energy, the spell cleanses with negative
energy rather than positive.
