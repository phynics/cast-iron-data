+++
id = "ref/spell/soul-bind"
kind = "spell"
title = "Soul Bind"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soul_bind", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Shaman", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, F (see text)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "corpse" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 9: Arcanist, Cleric, Oracle, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (see text)
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Will negates
Spell resistance: no
Target: corpse
:::

**Sources:** PRPG Core Rulebook pg 345

You draw the soul from a newly dead body and imprison it in a black sapphire gem. The subject must
have been dead no more than 1 round per caster level. The soul, once trapped in the gem, cannot be
returned through [clone](ref/spell/clone), [raise dead](ref/spell/raise-dead),
[reincarnate](ref/spell/reincarnate), [resurrection](ref/spell/resurrection),
[true resurrection](ref/spell/true-resurrection), or even a [miracle](ref/spell/miracle) or a
[wish](ref/spell/wish). Only by destroying the gem or dispelling the spell on the gem can one free
the soul (which is then still dead).

The focus for this spell is a black sapphire of at least 1,000 gp value for every HD possessed by
the creature whose soul is to be bound. If the gem is not valuable enough, it shatters when the
binding is attempted. (While creatures have no concept of level or HD as such, the value of the gem
needed to trap an individual can be researched.)
