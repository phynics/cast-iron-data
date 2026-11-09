+++
id = "ref/arc-cleric/fiendish-vessel"
kind = "archetype"
title = "Fiendish Vessel"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fiendish_vessel", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "advanced-race-guide"
page = "170"

[fields]
kind = "archetype"
replaces = ["Channel energy"]
+++

Many clerics pray to or make evil bargains with fiendish powers, devoting body and soul to the
insane plans and wicked aims of their despicable patrons. But these mortal clerics are often just
shallow beings searching for quick power or the caress of true and final oblivion - few truly grasp
the full scope of the entities they worship. Fiendish vessels, through their fiendish heritage,
share an innate connection with their patron, and that connection grants them understanding and
power. A fiendish vessel has the following class features.

**Prerequisites:** Tiefling; Alignment must match patron's

**Domains**

**Info:** A fiendish vessel must select the Daemon, Demon, or Devil subdomain as one of her domain
choices, based on the fiendish patron she chooses to serve.

**Provokes attack of opportunity:** No

**Usage:** Cha3 modifier times/day

**Channel Evil (Su)**

**Action:** Standard Action

**Replaces:** Channel energy

**Special:** For the purposes of feats that affect channel energy, this ability counts as channeling
negative energy. If the feat changes the way the fiendish vessel channels or deals damage with her
channeling, use the amount of damage this ability heals evil creatures to determine the
damage-dealing potential of the affected ability. For instance, if a 5th-level fiendish vessel takes
the [Channel Smite](ref/feat/channel-smite) feat, her channeling deals an additional 3d4 points of
damage to living creatures on a successful hit (though they may save to negate the damage).

A fiendish vessel, rather than channeling positive or negative energy, instead channels the pure
evil power of her fiendish patron. This ability is similar to channeling negative energy, but
instead of healing undead and dealing damage to living creatures, this blast of evil energy
automatically heals evil creatures and debilitates good creatures within its burst.

Channeling this evil causes a [burst](ref/misc/burst) that affects all creatures in a 30-foot radius
centered on the fiendish vessel. In the case of evil creatures, the amount of damage healed is equal
to 1d4 points of damage and increases by 1d4 at every two levels beyond 1st (to a maximum of 10d4 at
19th level). Good creatures in the burst receive a Will saving throw to negate this damage. Good
creatures that fail their saving throws are [sickened](ref/misc/sickened) for 1d4 rounds. Good
creatures with a number of Hit Dice less than or equal to the fiendish vessel's class level - 5 that
fail their saving throws are [nauseated](ref/misc/nauseated) for 1 round and then sickened for 1d4
rounds instead. The DC of this save is equal to 10 + [half](ref/misc/fractions-and-rounding) the
fiendish vessel's level + the fiendish vessel's Charisma bonus. Neutral creatures are unaffected by
this burst of evil energy.

A fiendish vessel can choose whether or not to include herself in this effect. A fiendish vessel
must present her unholy symbol or use her familiar as the divine focus for this ability.

**Fiendish Familiar**

**Action:** Ability

**Gained:** At 3rd Level

A fiendish vessel's patron rewards her with a fiendish servant. The fiendish vessel gains an
[imp](ref/monster/devil-imp), [quasit](ref/monster/demon-quasit), or
[cacodaemon](ref/monster/daemon-cacodaemon) [familiar](ref/ability/familiars) based on the patron
she worships. This ability is identical to the [wizard's](ref/class/wizard) arcane bond with a
familiar and the [Improved Familiar](ref/feat/improved-familiar) feat, using the fiendish vessel's
character level in place of the wizard level.

This tiny fiend acts like a perverse, manifest moral compass. Furthermore, this familiar can act as
a living divine focus and unholy symbol for her spellcasting if the fiendish vessel so desires,
which means that when she uses her _channel evil_ ability, its burst can be centered on the familiar
instead, as long as that familiar is within 30 feet and line of sight. A fiendish vessel's familiar
tends to be fawning and subservient to the fiendish vessel. Should her familiar die, the fiendish
vessel's patron replaces the familiar with an identical one within 1 week, without the need for a
special ritual. Furthermore, the fiendish familiar gains the following special abilities beyond the
standard familiar special abilities.

**Fiendish Augury (Sp)**

**At 3rd Level:** The fiendish vessel can ask the familiar whether a particular course of action
will bring good or bad results for her in the immediate future. This ability acts like the
[augury](ref/spell/augury) spell, with a caster level equal to the fiendish vessel's level, with the
familiar acting as the mouthpiece for the spell.

**Usage:** Once a day

**Usage:** Once a day

**Fiendish Divination (Sp)**

**At 9th Level:** The fiendish vessel can use a more powerful form of divination to gain
intelligence from her patron through her fiendish familiar. This ability acts like the
[divination](ref/spell/divination) spell, with a caster level equal to the fiendish vessel's level;
the familiar acts as the mouthpiece for the spell.

**Usage:** Once a day

**Usage:** Once a day

**Extra Divination (Sp)**

**At 13th Level:** The fiendish vessel can gain intelligence from her patron more often each day.
She can use _fiendish divination_ up to 3 times per day.

**Fiendish Summoning**

**Passive:** When casting _[summon monster](ref/spell/summon-monster)_ spells, a fiendish vessel is
limited to summoning [fiendish](ref/template/fiendish) creatures and evil outsiders of the same
alignment as her patron.

## Fiendish Patrons {#fiendish-patrons}

The following describes some of the more common patrons.

### Archdevils {#archdevils}

::: table
caption = "Archdevils"
head = [
  [
    { text = "Archdevil", header = true },
    { text = "AL", header = true },
    { text = "Areas of Concern", header = true },
    { text = "Domains", header = true },
    { text = "Favored Weapon", header = true },
  ],
  [
    { text = "Baalzebul" },
    { text = "LE" },
    { text = "Arrogance, flies, lies" },
    { text = "Air, Death, Evil, Law" },
    { text = "Spear" },
  ],
  [
    { text = "Belial" },
    { text = "LE" },
    { text = "Adultery, deception, desire" },
    { text = "Charm, Destruction, Evil, Law" },
    { text = "Ranseur" },
  ],
  [
    { text = "Dispater" },
    { text = "LE" },
    { text = "Cities, prisons, rulership" },
    { text = "Evil, Law, Nobility, Trickery" },
    { text = "Heavy mace" },
  ],
  [
    { text = "Mephistopheles" },
    { text = "LE" },
    { text = "Contracts, devils, secrets" },
    { text = "Evil, Knowledge, Law, Rune" },
    { text = "Trident" },
  ],
]
:::

### Demon Lords {#demon-lords}

::: table
caption = "Demon Lords"
head = [
  [
    { text = "Demon Lord", header = true },
    { text = "AL", header = true },
    { text = "Areas of Concern", header = true },
    { text = "Domains", header = true },
    { text = "Favored Weapon", header = true },
  ],
]
body = [
  [
    { text = "Abraxas" },
    { text = "CE" },
    { text = "Forbidden lore, magic, snakes" },
    { text = "Chaos, Evil, Knowledge, Magic" },
    { text = "Whip" },
  ],
  [
    { text = "Baphomet" },
    { text = "CE" },
    { text = "Beasts, labyrinths, minotaurs" },
    { text = "Animal, Chaos, Evil, Strength" },
    { text = "Glaive" },
  ],
  [
    { text = "Dagon" },
    { text = "CE" },
    { text = "Deformity, the sea, sea monsters" },
    { text = "Chaos, Destruction, Evil, Water" },
    { text = "Trident" },
  ],
  [
    { text = "Shax" },
    { text = "CE" },
    { text = "Envy, lies, murder" },
    { text = "Chaos, Destruction, Evil, Nobility" },
    { text = "Dagger" },
  ],
]
:::

### The Four Horsemen {#the-four-horsemen}

::: table
caption = "The Four Horsemen"
head = [
  [
    { text = "Horseman", header = true },
    { text = "AL", header = true },
    { text = "Areas of Concern", header = true },
    { text = "Domains", header = true },
    { text = "Favored Weapon", header = true },
  ],
]
body = [
  [
    { text = "Apollyon" },
    { text = "NE" },
    { text = "Pestilence" },
    { text = "Air, Darkness, Destruction, Evil" },
    { text = "Scythe" },
  ],
  [
    { text = "Charon" },
    { text = "NE" },
    { text = "Death" },
    { text = "Death, Evil, Knowledge, Water" },
    { text = "Quarterstaff" },
  ],
  [
    { text = "Szuriel" },
    { text = "NE" },
    { text = "War" },
    { text = "Evil, Fire, Strength, War" },
    { text = "Greatsword" },
  ],
  [
    { text = "Trelmarixian" },
    { text = "NE" },
    { text = "Famine" },
    { text = "Earth, Evil, Madness, Weather" },
    { text = "Spiked gauntlet" },
  ],
]
:::
