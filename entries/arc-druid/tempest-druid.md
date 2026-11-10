+++
id = "ref/arc-druid/tempest-druid"
kind = "archetype"
title = "Tempest Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Tempest%20Druid"
source_ids = ["adventurers-guide", "inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tempest_druid", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "adventurers-guide"
page = "183"
[[sources]]
publication = "inner-sea-magic"
page = "41"

[fields]
kind = "archetype"
replaces = ["Spontaneous casting", "Nature sense", "Trackless step", "Resist nature's lure", "Venom immunity"]
alters = ["Armor and weapon proficiencies", "Nature bond"]
+++

Many of the druids who train under the aegis of the [Storm Kindlers](ref/rule/aff-storms) focus on
different areas of nature than those classically paid homage to by their kind. These so-called
tempest druids see the personification of nature in the fury of the storm alone and to some extent
eschew the veneration of plant or animal life, and the nature of their powers shifts accordingly.
They still understand the place of plants and animals in the natural order, however; they simply
view such entities - and indeed, all forms of life - as subservient to the true power found in the
storms that lash the world.

**Prerequisites:** The beliefs held by tempest druids are inherently more chaotic than those held by
most druids, and as a result, tempest druids must be chaotic neutral.

**Armor and Weapon Proficiencies**

**Ability:** A tempest druid is proficient with the [trident](ref/eq-weapon/trident), in addition to
the druid's normal armor and weapon proficiencies.

**Alters:** Armor and weapon proficiencies

**Spontaneous Domain Casting**

**Ability:** A tempest druid can channel stored spell energy into domain spells that he has not
prepared ahead of time. He can &quot&lose&quot& a prepared spell to cast any domain spell of the
same level or lower.

**Replaces:** Spontaneous casting

**Nature Bond (Ex)**

**Alters:** Nature bond

**Choice:** He can't choose an animal companion, and must instead select a domain or subdomain from
the following list when he gains the _nature bond_ ability: [Air](ref/domain/air),
[Aquatic](ref/druiddomain/aquatic), [Cloud](ref/domain/air), [Storms](ref/domain/weather),
[Swamp](ref/druiddomain/swamp), [Weather](ref/domain/weather), or [Wind](ref/domain/air).

**Flavor:** As a result of his beliefs, a tempest druid has little connection to the spirituality of
animals or plants.

**Sodden Shore Sense (Ex)**

**Passive:** A tempest druid gains a +4 bonus on Knowledge (nature) and Survival checks in coastal
or marshy lands.

**Replaces:** Nature sense

**Electrical Resistance (Ex)**

**Gained:** At 3rd Level

**Passive:** A tempest druid gains electricity resistance 5.

**Replaces:** Trackless step

**Standard:** He can transfer this resistance to another creature for 1 hour, after which time it
reverts to him.

**Eyes of the Storm (Ex)**

**Ability:** A tempest druid can see through 10 feet of magical fog, mist, rain, wind, or similar
inclement weather conditions, ignoring any concealment such conditions might grant.

**At 12th Level:** His sight increases to 20 feet.

**At 16th Level:** His sight increases to 25 feet.

**At 20th Level:** His sight increases to 30 feet.

**At 8th Level:** His sight increases to 15 feet.

**Gained:** At 4th Level

**Replaces:** Resist nature's lure

**Bend Bolt (Su)**

**Flavor:** A tempest druid can redirect nearby electrical attacks.

**Immediate:** The druid can shift the area or target of an electricity attack by 5 feet in any
direction. If the electricity affects an area, the druid selects one square to be unaffected and an
adjacent square to be affected. If the adjacent square is already in the area, this has no
additional effect in that square. If the electricity affects a target, the druid selects an adjacent
target. For example, if he were in the line of a wizard's lightning bolt, he could have the spell
skip his square and instead affect an adjacent square, even if this meant the spell did not form a
continuous line. If another druid attacked him with [call lightning](ref/spell/call-lightning), he
could shift the called bolt to an adjacent square, affecting a creature in that square (if any).

**Gained:** At 9th Level

**Replaces:** Venom immunity

**Special:** He can't redirect electricity damage conducted to him by physical contact with an
object or creature (such as a [shocking grasp](ref/spell/shocking-grasp) or a
[shock](ref/magic-enh/shock) weapon).

**Usage:** Wis modifier times/day
