+++
id = "ref/spell/bow-spirit"
kind = "spell"
title = "Bow Spirit"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bow_spirit", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Hunter", level = 4 },
  { class = "Ranger", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Hunter, Ranger
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Creation
:::

**Sources:** Advanced Player's Guide pg 207

A bow spirit is a shapeless force that hovers about you, taking ammunition from your quiver and
firing it. For as long as the bow spirit lasts, you can spend a swift action to direct the bow
spirit to fire an arrow or a bolt at a target of your choice, as if the bow spirit were firing the
necessary ranged weapon. The bow spirit uses your base attack bonus plus your Dexterity modifier, as
well as any bonuses and effects from feats you have that affect ranged attacks, or bonuses from the
ammunition it uses. A bow spirit's attacks do not provoke attacks of opportunity. There must be
ammunition available for the bow spirit to use, and it expends ammunition as if used by you.

A bow spirit occupies your space, and moves with you. It cannot be attacked or harmed by physical
attacks, but [dispel magic](ref/spell/dispel-magic), [disintegrate](ref/spell/disintegrate), a
[sphere of annihilation](ref/magic-artifact/sphere-of-annihilation), or a
[rod of cancellation](ref/magic-rod/rod-of-cancellation) affects it. A bow spirit's AC against touch
attacks is 10 + your Dexterity modifier.
