+++
id = "ref/arc-paladin/warrior-of-the-holy-light"
kind = "archetype"
title = "Warrior of the Holy Light"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Warrior%20of%20the%20Holy%20Light"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "warrior_of_the_holy_light", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "advanced-players-guide"
page = "118"

[fields]
kind = "archetype"
features = [
  { anchor = "power-of-faith", level = 4 },
  { anchor = "shining-light", level = 14 },
]
trades = [
  { replaces = "Spells", feature = "spells", by = ["power-of-faith"] },
  { replaces = "Aura of faith", feature = "aura-of-faith", by = ["shining-light"] },
]
+++

Some paladins use their gifts to focus on the holy light that shines within their souls. With the
gifts of purity and redemption, these paladins spend much of their lives helping others find the
true path. Unleashing this power takes patience and comes at a steep price. Warriors of the holy
light have the following class features.

## Power of Faith (Su) {#power-of-faith}

At 4th level, a warrior of the holy light learns to use the power of her faith to bolster her
defenses and aid her allies. This class feature replaces the paladin's spells class feature. A
warrior of the holy light does not gain any spells or spellcasting abilities, does not have a caster
level, and cannot use spell trigger or spell completion magic items.

At 4th level, the warrior of the holy light gains one additional use of her lay on hands ability per
day. She gains one additional use of lay on hands per day for every four levels she attains beyond
4th. She can spend a use of her lay on hands ability to call upon the power of her faith as a
standard action. This causes a nimbus of _light_ to emanate from the warrior of the holy light in a
30-foot radius. All allies in this area (including the warrior of the holy light) receive a +1
morale bonus to AC and on attack rolls, damage rolls, and saving throws against fear as long as they
remain in the area of light. This power lasts for 1 minute.

At 8th level, the nimbus of light heals the paladin and her allies, curing of them of 1d4 points of
ability damage, as per the spell _[lesser restoration](ref/spell/restoration-lesser)_. A creature
can only be healed in this way once per day.

At 12th level, the nimbus of light is treated as _[daylight](ref/spell/daylight)_ for the purposes
of affecting creatures with sensitivity to light. In addition, the nimbus grants the warrior of the
holy light and her allies in the area [resistance](ref/umr/resistance) 10 to one type of energy,
selected by the warrior of the holy light when this power is activated.

At 16th level, the nimbus of light grants the warrior of the holy light and her allies protection
from critical hits. There is a 25% chance that critical hits made against the warrior of the holy
light and her allies in the area are instead treated as normal hits. This does not stack with other
abilities that grant similar protection (such as
_[light fortification](ref/magic-enh/fortification-light)_).

At 20th level, the nimbus of light increases in size out to a range of 60 feet. In addition, all of
its bonuses increase. The morale bonus to AC and on attack rolls, damage rolls, and saving throws
against fear increases to +2. The amount of ability damage healed increases to 2d4. The energy
resistance increases to 20 against one energy type. Finally, protection against critical hits
increases to 50%.

## Shining Light (Su) {#shining-light}

At 14th level, a warrior of the holy light can unleash a 30-foot [burst](ref/misc/burst) of pure,
white light as a standard action. Evil creatures within this burst take 1d6 points of damage for
every two paladin levels and are [blinded](ref/misc/blinded) for 1 round. Evil dragons, evil
outsiders, and evil undead are blinded for 1d4 rounds on a failed save. A Reflex save halves this
damage and negates the blindness. The DC of this save is equal to 10 + 1/2 the warrior of the holy
light's level + the warrior of the holy light's Charisma modifier. Good creatures within this burst
are healed 1d6 points of damage per two paladin levels and receive a +2 sacred bonus on ability
checks, attack rolls, saving throws, and skill checks for 1 round. A warrior of the holy light can
use this ability once per day at 14th level plus one additional time per day at 17th and 20th
levels. This ability replaces aura of faith.
