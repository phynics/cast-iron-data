+++
id = "ref/spell/peacebond-greater"
kind = "spell"
title = "Greater Peacebond"
source_ids = ["ultimate-combat", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "peacebond_greater", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/peacebond" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "up to one weapon/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Inquisitor, Occultist\
5: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: S
Range: medium (100 ft. + 10 ft./level)
Target: up to one weapon/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level
Saving throw: Will negates (object)
Spell resistance: yes (object)
:::

### Greater Peacebond

**Sources:** Ultimate Intrigue pg 221

If a target weapon is sheathed or slung as the spell is cast, this functions as
[peacebond](ref/spell/peacebond), locking the target's weapon in place on its owner's body or within
the weapon's sheath or holster. Anyone who then tries to draw the weapon must spend a standard
action and succeed at a Strength check to do so, provoking attacks of opportunity whether the
attempt succeeds or fails. The DC for Strength checks required by this spell is equal to the spell's
save DC.

If a target weapon is not currently sheathed or slung as the spell is cast, the weapon immediately
attempts to sheathe itself, and its wielder must succeed at a Strength check to prevent it from
doing so. Once sheathed or slung in this way, the weapon is difficult to draw, as previously noted
above. Unattended weapons that are not currently sheathed or slung are anchored in place by the
spell, and require a successful Strength check to pick up; each attempt requires a standard action.
If the wielder doesn't have a sheath or sling available for the weapon, failure on the Strength
check causes the weapon to fall to the ground, at which point it requires a Strength check to pick
up, as with unattended weapons.
