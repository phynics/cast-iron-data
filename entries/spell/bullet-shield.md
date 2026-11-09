+++
id = "ref/spell/bullet-shield"
kind = "spell"
title = "Bullet Shield"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bullet_shield", path = "json/spells2.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "225"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a bullet)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Alchemist, Arcanist, Bloodrager, Investigator, Occultist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a bullet)
Range: touch
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

The warded creature gains a +4 deflection bonus to AC against firearm and ranged attacks, with an
additional +1 to the bonus for every five caster levels you have (to a maximum of +8 at 20th level).
Though the spell is called bullet shield, it also grants this protection from attacks made from
firearms with the scatter weapon quality.
