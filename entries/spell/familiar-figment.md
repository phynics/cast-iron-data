+++
id = "ref/spell/familiar-figment"
kind = "spell"
title = "Familiar Figment"
aon = "SpellDisplay.aspx?ItemName=Familiar%20Figment"
source_ids = ["animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "familiar_figment", path = "json/spells4.json" },
]
[[sources]]
publication = "animal-archive"
page = "24"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "your familiar" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Arcanist, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: your familiar
Subschool: Figment
:::

You create an illusory duplicate of your familiar that moves erratically around your familiar's
space, frequently moving through the familiar's body with a blurring effect that makes it
indistinguishable from the real creature. Attacks against the familiar have a 50% miss chance;
attacks that miss instead target the familiar figment, which reacts as if damaged as appropriate to
the attack but unlike a mirror image is not destroyed when struck. This spell does not grant your
familiar concealment or prevent it from being targeted by spell effects that do not require an
attack roll.

In addition, as a swift action, your familiar can direct the familiar figment to attempt a melee
touch attack, using your base attack bonus and the familiar's Dexterity modifier. If this attack
hits, your familiar (but not other creatures) treats that target as flanked until the end of its
turn.
