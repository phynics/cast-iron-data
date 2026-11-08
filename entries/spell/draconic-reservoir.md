+++
id = "ref/spell/draconic-reservoir"
kind = "spell"
title = "Draconic Reservoir"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "draconic_reservoir", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "evocation [acid, cold, electricity, or fire]"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a scale from dragon that produces the energy you seek to absorb)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level or until discharged; see text"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: evocation \[acid, cold, electricity, or fire\]
Level: 3: Alchemist, Arcanist, Bloodrager, Investigator, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a scale from dragon that produces the energy you seek to absorb)
Range: touch
Duration: 10 minutes/level or until discharged; see text
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

**Sources:** Advanced Player's Guide pg 217

Draconic reservoir functions as [protection from energy](ref/spell/protection-from-energy),
absorbing 6 points of one type of energy damage per caster level (acid, cold, electricity, or fire,
maximum 60 points). Each round, as a swift action, the subject can release 1d6 points of the
absorbed energy and apply it to any melee attack, as if using an acidic, flaming, frost, or shock
weapon. The first creature the subject strikes with this attack takes the energy damage in addition
to any other consequences of the attack. Releasing energy in this way does not "free up" space to
absorb still more energy; the maximum amount of energy the spell can absorb remains fixed. The
subject cannot release more energy than he currently has absorbed. Once the subject has absorbed all
the energy allowed by the spell, he takes damage as normal from that energy type. Once the energy
has been released, the spell is discharged.

Draconic reservoir does not stack with protection from energy. Draconic reservoir overlaps (and does
not stack with) resist energy. If a character is warded by draconic reservoir and resist energy,
draconic reservoir absorbs damage until it reaches its maximum limit.
