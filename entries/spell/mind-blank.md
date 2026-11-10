+++
id = "ref/spell/mind-blank"
kind = "spell"
title = "Mind Blank"
aon = "SpellDisplay.aspx?ItemName=Mind%20Blank"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mind_blank", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "313"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "24 hours"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 7: Psychic\
8: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 24 hours
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature
:::

The subject is protected from all devices and spells that gather information about the target
through divination magic (such as [detect evil](ref/spell/detect-evil),
[locate creature](ref/spell/locate-creature), [scrying](ref/spell/scrying), and
[see invisibility](ref/spell/see-invisibility)). This spell also grants a +8 resistance bonus on
saving throws against all mind-affecting spells and effects. Mind blank even foils
[limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle), and [wish](ref/spell/wish)
spells when they are used in such a way as to gain information about the target. In the case of
scrying that scans an area the creature is in, such as [arcane eye](ref/spell/arcane-eye), the spell
works but the creature simply isn't detected. Scrying attempts that are targeted specifically at the
subject do not work at all.
