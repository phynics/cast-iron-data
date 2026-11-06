+++
id = "ref/spell/mutagenic-touch"
kind = "spell"
title = "Mutagenic Touch"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mutagenic_touch", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Investigator", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a whole fingernail)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "special (see below)"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Investigator
Casting time: 1 standard action
Components: V, S, M (a whole fingernail)
Range: touch
Duration: special (see below)
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

**Sources:** Ultimate Combat pg 237

When you are under of the effects of your mutagen, you can cast this spell to safely pass it to
another creature with a touch. You must make a successful touch attack against the target. On a hit,
the effect of the mutagen passes to the target touched, though in a lesser form. The mutagen's
effect ends for you, and passes on to the creature touched, but the target only gets half of the
alchemical bonus to the physical ability modifier you chose when took the mutagen, and twice the
penalty to the corresponding mental ability score. If the target's mental ability score drops below
3, the target is also confused for the remaining duration of the mutagen. The mutagen continues
until the duration has ended. It can be ended earlier if the target drinks or is fed the contents of
a vial of antitoxin, but with only 50% chance of success.

You can use this spell on a mutagen with either the greater mutagen or advance mutagen discoveries.
When you do, you always pass on half the alchemical bonus to physical abilities and twice the
penalty to the mental ability score.
