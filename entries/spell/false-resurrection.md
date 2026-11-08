+++
id = "ref/spell/false-resurrection"
kind = "spell"
title = "False Resurrection"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "false_resurrection", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/resurrection" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 8 },
  { class = "Witch", level = 8 },
]
casting_time = "1 minute"
components = "V, S, DF, M (diamond worth 10,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "dead creature touched" },
]
duration = "instantaneous"
saving_throw = "none, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 7: Cleric, Oracle\
8: Shaman, Witch
Casting time: 1 minute
Components: V, S, DF, M (diamond worth 10,000 gp)
Range: touch
Duration: instantaneous
Saving throw: none, see text
Spell resistance: yes
Target: dead creature touched
Subschool: Healing
:::

### False Resurrection

**Sources:** Ultimate Intrigue pg 214

This spell functions as [resurrection](ref/spell/resurrection) except that instead of recalling the
dead soul to life, the spell calls a shadow demon with the advanced simple template to possess the
body. If you fail to overcome the subject's [spell resistance](ref/rule/spell-resistance), the
subject's soul can negate the calling and gain the option to return to life (as resurrection) in the
restored body. The possession otherwise functions (as possession) except that the subject's soul is
not present to resist. When false resurrection ends or the demon is removed from the subject, the
demon returns to the Abyss, leaving the body alive but soulless (like that created by clone). If the
soul hasn't been returned to life already, it has the option to return in the now-empty body if it
still lives (as resurrection). If the body was killed, the demon is sent back to the Abyss but the
subject remains dead.

Attempts to identify false resurrection with a skill check incorrectly identify it as resurrection
(see the [ruse](ref/spelldef/ruse) descriptor). A fooled viewer mistakes false resurrection's aura
as the lingering aura of an instantaneous conjuration effect.
