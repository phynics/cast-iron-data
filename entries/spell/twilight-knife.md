+++
id = "ref/spell/twilight-knife"
kind = "spell"
title = "Twilight Knife"
aon = "SpellDisplay.aspx?ItemName=Twilight%20Knife"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "twilight_knife", path = "json/spells10.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "252"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, F (a small knife)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "floating knife of force" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Bloodrager, Occultist, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a small knife)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes
Effect: floating knife of force
Descriptors: force
:::

You create a darkly sinister floating knife that attacks the same creature as you each round. If you
choose not to attack a creature, or you make an attack that affects multiple opponents, the knife
makes no attack during that round. The knife uses your base attack bonus modified by either your
Intelligence or Charisma bonus (whichever is higher) when making this attack. Unless you
specifically will it to do otherwise, or it proves impossible to do so, the knife always maneuvers
itself so that it can flank your opponent before making the attack. The knife deals 1d4 points of
force damage on a successful hit and has the same threat range and critical multipliers as a normal
dagger. In addition, if the target is denied a Dexterity bonus to AC or the knife flanks the target,
the knife can make sneak attacks as a rogue, inflicting an extra 1d6 points of force damage per four
caster levels on a successful attack.

A twilight knife cannot be attacked or harmed by physical attacks, but
[dispel magic](ref/spell/dispel-magic), [disintegrate](ref/spell/disintegrate), a
[sphere of annihilation](ref/magic-artifact/sphere-of-annihilation), or a
[rod of cancellation](ref/magic-rod/rod-of-cancellation) affects it. A twilight knife's AC against
touch attacks is 12 (10 + size bonus for Tiny object) plus your Dexterity modifier.

If an attacked creature has [spell resistance](ref/rule/spell-resistance), you make a caster level
check (1d20 + caster level) against that spell resistance the first time the twilight knife strikes
it. If the knife is successfully resisted, the spell is dispelled. If not, the weapon has its normal
full effect on that creature for the duration of the spell.
