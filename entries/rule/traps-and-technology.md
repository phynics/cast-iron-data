+++
id = "ref/rule/traps-and-technology"
kind = "rule"
title = "Traps and Technology"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "traps_and_technology", path = "json/rules_campaign_types10.json" },
]

[fields]
kind = "none"
+++

**Sources:** Technology Guide pg 56\
Mundane and magical traps can incorporate technological elements in their construction. Computers
and AIs can also be connected to traps, allowing them to selectively trigger the traps remotely.
Traps that incorporate technology gain the technological type, in addition to their normal type (see
the following examples). The following technological triggers are available to traps

**Electric Eyes:** Similar to a visual trigger, the trap incorporates a camera or other visual and
audio recording device. Electric eyes typically have [darkvision](ref/rule/darkvision) to a range of
120 feet, [low-light vision](ref/rule/low-light-vision), and a Perception bonus of +15. This trigger
adds +1 to the trap's CR and +5 to its crafting DC.

**Genetic:** A genetic trigger works in a fashion similar to scent. It can be set to target or not
target living creatures within 30 feet (adjusted by wind as for scent) based on an individual, close
family, or species relationship. For example, a trap could be set to target orcs, or to not target
an NPC and his close relations. Genetic triggers are used in conjunction with other triggers and
limit the maximum range of those triggers. A trap can incorporate up to half its CR in different
genetic samples and conditions. This trigger adds +1 to the trap's CR and +5 to its crafting DC.

### Concealed Laser Turret

#### CR 4

**Type** mechanical and technological; **Perception DC** 20; **Disable Device** DC 28

**Trigger** camera (Perception +15); **Reset** automatic (1 round)\
**Effect** Atk +10 ranged touch (2d6 fire), range increment 150 ft. (see
[laser pistol](ref/tech-weapon/laser-pistol) for rules on lasers)

### Proximity Mine

#### CR 5

**Type** genetic, proximity **Perception DC** 28; **Disable Device** DC 20

**Trigger** camera (Perception +15); **Reset** none\
**Effect** one [bang\_](ref/tech-weapon/bang-grenade) worth 1,000 gp or less, multiple targets and
saves (see grenade for rules)

### Electrified Door

#### CR 11

**Type** mechanical and technological; **Perception DC** 32; **Disable Device** DC 29

**Trigger** touch (see text); **Reset** automatic (1 minute; see text)\
**Effect** 10d8 electricity damage (Reflex DC 25 half) to anyone touching the door; typically an
electrified door triggers only if a creature attempts to bypass or force the door; electrified doors
connected to a generator have no charge limit, otherwise the trap has only enough energy to function
once with no reset
