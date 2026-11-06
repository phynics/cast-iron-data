+++
id = "ref/spell/hostile-juxtaposition-greater"
kind = "spell"
title = "Greater Hostile Juxtaposition"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hostile_juxtaposition_greater", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a coin)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature of your size or smaller" },
]
duration = "1 round/level or until discharged"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Mesmerist, Summoner\
5: Arcanist, Psychic, Sorcerer, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a coin)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level or until discharged
Saving throw: Will negates
Spell resistance: yes
Target: one creature of your size or smaller
Subschool: Teleportation
:::

## Hostile Juxtaposition

**Sources:** Ultimate Combat pg 231

You create a dimensional link to the target creature. When attacked or the subject of a spell that
deals damage to you, you can spend an immediate action to cause yourself and the target creature to
teleport and switch places. The target then becomes the target of the triggering attack or spell
instead of you. If you fail to teleport out of the area of an effect, that effect might still affect
you. If the target creature cannot fit safely into the new space without squeezing, or you try to
teleport the target into an occupied space or a space it could not normally stand within, the
juxtaposition fails. Further, if the target is unconscious or dead when you attempt to switch
places, the juxtaposition fails. Once you have used it to teleport once, this spell is discharged.

### Greater Hostile Juxtaposition

**Sources:** Ultimate Combat pg 231

This spell functions like hostile juxtaposition, except you can target one creature for every four
caster levels you have or you can target a single creature that is larger than you are. You can
switch places with each target only once while the effect lasts. Once you have used it to teleport
and switch places with each affected target, the spell is discharged.
