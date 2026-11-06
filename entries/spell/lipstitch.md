+++
id = "ref/spell/lipstitch"
kind = "spell"
title = "Lipstitch"
source_ids = ["pathfinder-society-field-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lipstitch", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "S, M (a bone needle and sinew thread)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: S, M (a bone needle and sinew thread)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
:::

**Sources:** Pathfinder Society Field Guide pg 57

A rare spell without verbal components, lipstitch sews the target's lips tightly together if it
fails a saving throw, such that no clear speech, bite attacks, spellcasting, or use of command words
is possible. The target takes 1d6 points of damage as the stitches weave through flesh. The victim
can still make enough noise to be heard at a distance with a DC 10 Perception check.

The thread created by lipstitch can be burst with a DC 20 Strength check as a standard action or can
be sliced open with a piercing or slashing weapon (wielded by the target or an ally) as a full-round
action. Cutting the thread provokes attacks of opportunity, while making a Strength check does not.
Either option causes 1d6 points of damage and 1 point of bleed damage. The target has a 20% chance
of failing to cast spells with verbal components until the bleeding is stopped. The effects of
multiple castings of this spell do not stack. Optionally, the thread can be removed more carefully
over the course of a minute with a DC 20 Heal check. If the check fails, the target takes damage and
bleeds as described above. If the check succeeds, the stitches are removed with no harm. Creatures
with no mouths are unaffected by lipstitch. Creatures with multiple mouths lose the use of only one
mouth per casting - the particular mouth is chosen by the caster.
