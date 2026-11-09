+++
id = "ref/spell/fleshy-facade"
kind = "spell"
title = "Fleshy Facade"
aon = "SpellDisplay.aspx?ItemName=Fleshy%20Facade"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fleshy_facade", path = "json/spells4.json" },
]
[[sources]]
publication = "monster-codex"
page = "81"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "corporeal undead creature touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "yes (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Arcanist, Bard, Inquisitor, Investigator, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level (D)
Saving throw: yes (harmless)
Spell resistance: yes
Target: corporeal undead creature touched
Subschool: Polymorph
:::

The target's flesh fills out and gains a healthy, natural color. This gives the target the
appearance of a living creature of the type it was when it was still alive (if applicable).
Creatures casting spells such as [detect undead](ref/spell/detect-undead) must succeed at a saving
throw (with a DC equal to the spell's save DC) to detect the target's presence, and if the target is
intelligent, it gains a +10 bonus on Disguise checks to appear alive or recently deceased. If the
undead has any features different from those of the type of living creature it most resembles (such
as a ghoul's elongated teeth and claws), those features shrink and become less prominent, and the
subject deals damage as though it were one size smaller. This spell has no effect on creatures that
are skeletal or otherwise lack flesh.
