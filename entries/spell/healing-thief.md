+++
id = "ref/spell/healing-thief"
kind = "spell"
title = "Healing Thief"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "healing_thief", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a bit of sponge, damp with tears)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level or until discharged"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Mesmerist\
3: Arcanist, Occultist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a bit of sponge, damp with tears)
Range: touch
Duration: 1 round/level or until discharged
Saving throw: none
Spell resistance: yes
Target: creature touched
:::

**Sources:** Ultimate Combat pg 231

With this spell you can steal the healing of the target creature. You must succeed at a melee touch
attack to strike the target. If you do, until the effect ends, whenever your target is subject to a
healing spell or a supernatural effect that heals hit points, the target only receives half the
healing (rounded down) and you receive the other half (also rounded down). You must remain within 25
feet (plus 5 feet per two caster levels) of the target to gain this benefit. If you move outside
that range, the spell is discharged. Once you steal 5 hit points per your caster level (maximum 50
hit points) of healing from this spell's effect, the spell is discharged.
