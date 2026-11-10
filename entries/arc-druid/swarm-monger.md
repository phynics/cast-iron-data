+++
id = "ref/arc-druid/swarm-monger"
kind = "archetype"
title = "Swarm Monger"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "swarm_monger", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "21"

[fields]
kind = "archetype"
replaces = ["Nature bond", "Woodland stride", "Nature sense", "Resist nature's lure", "The normal wild shape options gained at 12th level"]
+++

Swarm mongers are unparalleled survivors, thriving on the filthy fringes of society. Whereas other
druids commune with nature or even the spirit of a city, swarm mongers find beauty and strength in
decay, and they draw their power from fungus, disease, and their own singular will to survive.

**Prerequisites:** Ratfolk

**Fecund Familiar (Ex)**

**Choice:** A swarm monger bonds with an urban [familiar](ref/sidekick/familiar), treating her druid
level as her [wizard](ref/class/wizard) level for the purposes of determining her familiar's
abilities. The swarm monger must select her familiar from the
[following options](ref/ability/familiars): cat, house centipede, rat, raven, or scarlet spider.

**At 12th Level:** Creatures that fail their Fortitude saving throws instead become
[nauseated](ref/misc/nauseated).

**At 5th Level:** Any creature damaged by a fecund familiar's swarm attack must succeed at a
Fortitude saving throw (DC = 10 + 1/2 the swarm monger's druid level + the swarm monger's Wisdom
modifier) or be [sickened](ref/misc/sickened) for 1d6 rounds.

**Passive:** The fecund familiar gains the benefits of its master's _child of pollution, shadowy
opportunist,_ and _venom immunity_ class abilities.

**Replaces:** Nature bond

**Special:** The swarm monger is immune to her own familiar's swarm attack. A fecund familiar cannot
be reduced in size to Diminutive or smaller when in swarm form.

**Standard:** A swarm monger can cause her familiar to burst forth into a full swarm of identical
creatures, filling four contiguous 5-foot squares and gaining
[temporary hit points](ref/rule/temporary-hit-points) equal to
[half](ref/misc/fractions-and-rounding) its master's maximum hit points. While in swarm form, the
familiar loses the _improved evasion, share spells, deliver touch attack,_ and _scry on familiar_
special abilities. It uses its normal AC, saving throws, and skill bonuses, and it gains the
[swarm](ref/subtype/swarm) subtype and the ability to make swarm attacks (dealing 1d6 points of
damage at 1st level and using the swarm monger's druid level as the swarm's Hit Dice to determine
damage increases as per the swarm subtype).

**Usage:** A swarm monger can transform her familiar into a swarm a number of times each day equal
to her Wisdom modifier (minimum 1), and the transformation lasts for 1 minute per druid level, or
until the swarm monger reverts her familiar back to a singular form as a **standard action**.

**Usage:** A swarm monger can transform her familiar into a swarm a number of times each day equal
to her Wisdom modifier (minimum 1), and the transformation lasts for 1 minute per druid level, or
until the swarm monger reverts her familiar back to a singular form as a **standard action**.

**Low Friends (Ex)**

**Ability:** A swarm monger gains [Vermin Heart](ref/feat/vermin-heart) as a bonus feat.

**Gained:** At 2nd Level

**Replaces:** Woodland stride

**Shadowy Opportunist (Ex)**

**Passive:** A swarm monger gains a +2 bonus on Knowledge (local) and Stealth checks.

**Replaces:** Nature sense

**Child of Pollution (Su)**

**Gained:** At 4th Level

**Passive:** A swarm monger gains a +4 bonus on saving throws against disease and poisons, and she
can eat spoiled or rotting food and drink without ill effect.

**Replaces:** Resist nature's lure

**Standard:** A swarm monger can devour a handful of rotting food to gain a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to 1d8 + her druid level that last for 1
hour. She can use this ability a number of times a day equal to one-fourth of her druid level.

**Swarm Shape (Su)**

**Ability:** A swarm monger can use _wild shape_ to transform into a swarm of vermin, functioning as
[swarm skin](ref/spell/swarm-skin), but not allowing her to split into more than one contiguous
swarm. She doesn't leave her gear behind when she uses this ability, and she can revert to her
mundane form normally.

**Gained:** At 12th Level

**Replaces:** The normal _wild shape_ options gained at 12th level
