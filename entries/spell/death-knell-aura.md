+++
id = "ref/spell/death-knell-aura"
kind = "spell"
title = "Death Knell Aura"
source_ids = ["book-of-the-damned-volume-3-horsemen-of-the-apocalypse"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "death_knell_aura", path = "json/spells3.json" },
]
[[sources]]
publication = "book-of-the-damned-volume-3-horsemen-of-the-apocalypse"
page = "38"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death", "evil"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "20 ft."
effects = [
  { label = "Area", value = "20-ft.-radius emanation, centered on you" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Arcanist, Cleric, Inquisitor, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 20 ft.
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Area: 20-ft.-radius emanation, centered on you
Descriptors: death, evil
:::

You gain a shimmering gray aura that feeds on the souls of creatures who die within it. The aura
sheds light as a candle. If a creature at -1 or fewer hit points is within the aura at the start of
its turn, it must save or die, granting you the benefits of death knell.
