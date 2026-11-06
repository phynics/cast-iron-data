+++
id = "ref/spell/limp-lash"
kind = "spell"
title = "Limp Lash"
source_ids = ["goblins-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "limp_lash", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a dead wasp)"
range = "20 ft."
effects = [
  { label = "Target", value = "1 creature" },
]
duration = "special (see below)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a dead wasp)
Range: 20 ft.
Duration: special (see below)
Saving throw: none
Spell resistance: yes
Target: 1 creature
:::

**Sources:** Goblins of Golarion pg 28

You create a dark whip-shaped field of energy that wraps around an enemy's neck, leaving everything
except his head paralyzed until you let go of the whip or it is destroyed. You must make a ranged
touch attack with this spell. If you strike your target, he takes a 1d6 penalty to his Strength,
Dexterity, and Constitution each round. This penalty cannot reduce any attribute to less than 1, and
once any of these attributes reaches 1 the target collapses and his body, except his head, becomes
paralyzed. While paralyzed in this way, the target retains full use of his senses, including the
ability to feel pain, and can speak (including casting spells with only verbal components). The whip
has a maximum length of 20 feet, 15 hit points, and a [hardness](ref/umr/hardness) of 5. The spell
ends immediately if you let go of the whip or it is destroyed. When the spell ends, all penalties
the target took from this spell also end.
