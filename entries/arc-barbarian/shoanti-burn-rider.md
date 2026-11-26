+++
id = "ref/arc-barbarian/shoanti-burn-rider"
kind = "archetype"
title = "Shoanti Burn Rider"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Shoanti%20Burn%20Rider"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shoanti_burn_rider", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "inner-sea-combat"
page = "44"

[fields]
kind = "archetype"
features = [
  { anchor = "flame-runner", level = 1 },
  { anchor = "cinder-sight", level = 2 },
  { anchor = "cinder-dance", level = 3 },
  { anchor = "mount", level = 4 },
  { anchor = "give-me-fire", level = 5 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["flame-runner"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["cinder-sight"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["cinder-dance"] },
  { replaces = "Rage powers gained at 4th, 8th, 12th, and 16th level", feature = "rage-powers", levels = [4, 8, 12, 16], by = ["mount"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["give-me-fire"] },
]
+++

The Shoanti tribes who live in the Cinderlands have turned the deadly emberstorms that plague the
region into a rite of passage. A few who survive the experience begin to embrace the adrenaline and
surge of joy that comes from dancing along the edge of a whirling firestorm. These thrill-seekers
are known as burn riders, and their exploits are celebrated by all Shoanti. Burn riders learn early
on that speed and lightning-quick reactions are essential to avoid becoming trapped by the fickle
whims of a raging emberstorm. They have an uncanny understanding of fire and can read the currents
in the smoke.

## Flame Runner (Ex) {#flame-runner}

At 1st level, once per rage, a burn rider can goad her mount into a burst of incredible speed. The
mount's speed increases by 10 feet until the end of the burn rider's turn. This bonus to speed
increases by 10 feet at 9th level and again at 15th level. This ability replaces fast movement.

## Cinder Sight (Ex) {#cinder-sight}

At 2nd level, a Shoanti burn rider can see through fire, fog, and smoke without penalty as long as
the light is sufficient to allow her to see normally. This ability replaces uncanny dodge.

## Cinder Dance (Ex) {#cinder-dance}

At 3rd level, when a burn rider succeeds at a Reflex save to avoid fire damage, she can spend an
immediate action to move up to half her speed. If the burn rider ends this movement outside the area
of effect, she takes no damage from the effect. After this sudden movement, the burn rider is
[staggered](ref/misc/staggered) until the end of her next turn. If the burn rider is mounted, her
mount makes the movement instead, and both the mount and the burn rider are staggered until the end
of the burn rider's next turn. This ability replaces trap sense.

## Mount {#mount}

At 4th level, a burn rider gains a loyal mount. This ability functions like the druid's
[animal companion](ref/sidekick/animal-companion) ability (as described in the nature bond class
feature), except that the burn rider always gains a [horse](ref/companion/horse) or
[pony](ref/companion/pony) (though she can gain additional options at the GM's discretion) and her
effective druid level is equal to her Shoanti burn rider level - 3. This ability replaces the rage
powers gained at 4th, 8th, 12th, and 16th level.

## Give Me Fire (Ex) {#give-me-fire}

At 5th level, if a Shoanti burn rider takes fire damage while raging, she regains 1 round of rage.
The burn rider regains the round of rage only if the fire damage bypasses or exceeds any energy
resistance or other protections in effect. The burn rider can only regain 1 round of rage per round.
This ability replaces improved uncanny dodge.

## Rage Powers {#rage-powers}

The following rage powers complement the Shoanti burn rider archetype:
[elemental rage](ref/ragepower/elemental-rage),
[energy resistance](ref/ragepower/energy-resistance),
[ferocious mount](ref/ragepower/ferocious-mount),
[ferocious trample](ref/ragepower/ferocious-trample),
[increased damage reduction](ref/ragepower/increased-damage-reduction),
[low-light vision](ref/ragepower/low-light-vision), [night vision](ref/ragepower/night-vision),
[renewed vigor](ref/ragepower/renewed-vigor), [scent](ref/ragepower/scent),
[spirit steed](ref/ragepower/spirit-steed), [sprint](ref/ragepower/sprint), and
[swift foot](ref/ragepower/swift-foot).
