+++
id = "ref/carried/ultimate-magic/spells/astral-projection/lesser"
kind = "spell"
title = "Astral Projection, Lesser"
source_ids = ["ultimate-magic"]
section = ["Spells", "Astral Projection"]
tags = ["necromancy"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/Astral Projection/Lesser", path = "ultimate_magic/spell/astral_projection_lesser.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "30 minutes"
components = "V, S, M (jacinth worth 1,000 gp)"
range = "touch"
effects = [
  { label = "Targets", value = "you plus one additional willing creature touched per two caster levels" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
School: necromancy
Level: 5: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting Time: 30 minutes
Components: V, S, M (jacinth worth 1,000 gp)
Range: touch
Targets: you plus one additional willing creature touched per two caster levels
Duration: see text
Saving Throw: none
Spell Resistance: yes
:::

_Limited astral travel._

This spell functions as _[astral projection](ref/spell/astral-projection)_, except you cannot leave
the Astral Plane and explore other planes (though you can still return to the plane you were on when
you cast this spell).
