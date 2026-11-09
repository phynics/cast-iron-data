+++
id = "ref/spell/final-sacrifice"
kind = "spell"
title = "Final Sacrifice"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "final_sacrifice", path = "json/spells4.json" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "22"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 2 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one summoned creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates, then Reflex half (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Bloodrager, Summoner\
3: Antipaladin, Arcanist, Cleric, Oracle, Shaman, Sorcerer, Warpriest, Wizard\
4: Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude negates, then Reflex half (see text)
Spell resistance: yes
Target: one summoned creature
:::

You disrupt the conjuring energies within a summoned creature, causing it to violently explode. If
the target fails its Fortitude save, it is immediately slain and all creatures within 20 feet of the
target take 1d4 points of damage per spell level of the summoning spell that conjured the target.
This damage is fire damage unless the target creature has the cold or water subtype, in which case
it's cold damage. Creatures caught in this explosion take half damage if they succeed at their
Reflex saves against this spell's DC. Final sacrifice can detonate a summoner's eidolon, though an
eidolon receives a +4 bonus on its Fortitude save unless the spell is cast by the eidolon's own
summoner. If this spell targets an eidolon, creatures within 20 feet of the eidolon take an amount
of damage equal to 1d4 + 1/2 the caster level of the summoner who controlled the eidolon.
