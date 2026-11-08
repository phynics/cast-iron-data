+++
id = "ref/spell/cyclic-reincarnation"
kind = "spell"
title = "Cyclic Reincarnation"
source_ids = ["core-rulebook", "inner-sea-races", "arcane-anthology", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cyclic_reincarnation", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/reincarnate" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Witch", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (oils worth 1,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "dead creature touched" },
]
duration = "instantaneous"
saving_throw = "none, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Druid, Hunter, Medium, Shaman\
5: Witch
Casting time: 10 minutes
Components: V, S, DF, M (oils worth 1,000 gp)
Range: touch
Duration: instantaneous
Saving throw: none, see text
Spell resistance: yes
Target: dead creature touched
:::

## Reincarnate

**Sources:** PRPG Core Rulebook pg 331

With this spell, you bring back a dead creature in another body, provided that its death occurred no
more than 1 week before the casting of the spell and the subject's soul is free and willing to
return. If the subject's soul is not willing to return, the spell does not work; therefore, a
subject that wants to return receives no saving throw.

Since the dead creature is returning in a new body, all physical ills and afflictions are repaired.
The condition of the remains is not a factor. So long as some small portion of the creature's body
still exists, it can be reincarnated, but the portion receiving the spell must have been part of the
creature's body at the time of death. The magic of the spell creates an entirely new young adult
body for the soul to inhabit from the natural elements at hand. This process takes 1 hour to
complete. When the body is ready, the subject is reincarnated.

A reincarnated creature recalls the majority of its former life and form. It retains any class
abilities, feats, or skill ranks it formerly possessed. Its class, base attack bonus, base save
bonuses, and hit points are unchanged. Strength, Dexterity, and Constitution scores depend partly on
the new body. First eliminate the subject's racial adjustments (since it is no longer necessarily of
his previous race) and then apply the adjustments found below to its remaining ability scores. The
subject of the spell gains two permanent negative levels when it is reincarnated. Negative levels
equal to or greater than the creature's Hit Dice are instead applied as Constitution drain (if this
would reduce its Con to 0 or less, it can't be reincarnated). A character who died with spells
prepared has a 50% chance of losing any given spell upon being reincarnated. A spellcasting creature
that doesn't prepare spells (such as a sorcerer) has a 50% chance of losing any given unused spell
slot as if it had been used to cast a spell.

It's possible for the change in the subject's ability scores to make it difficult for it to pursue
its previous character class. If this is the case, the subject is advised to become a multiclass
character.

For a humanoid creature, the new incarnation is determined using the table below. For non-humanoid
creatures, a similar table of creatures of the same type should be created.

A creature that has been turned into an undead creature or killed by a death effect can't be
returned to life by this spell. Constructs, elementals, outsiders, and undead creatures can't be
reincarnated. The spell can bring back a creature that has died of old age.

|d%|Incarnation|Str|Dex|Con|
| --- | --- | --- | --- | --- |
|01|[Bugbear](ref/monster/bugbear)|+4|+2|+2|
|02-13|[Dwarf](ref/race/dwarf)|+0|+0|+2|
|14-25|[Elf](ref/race/elf)|+0|+2|-2|
|26|[Gnoll](ref/monster/gnoll)|+4|+0|+2|
|27-38|[Gnome](ref/race/gnome)|-2|+0|+2|
|39-42|[Goblin](ref/race/goblin)|-2|+2|+0|
|43-52|[Half-elf](ref/race/half-elf)|+0|+2|+0|
|53-62|[Half-orc](ref/race/half-orc)|+2|+0|+0|
|63-74|[Halfling](ref/race/halfling)|-2|+2|+0|
|75-89|[Human](ref/race/human)|+0|+0|+2|
|90-93|[Kobold](ref/race/kobold)|-4|+0|-2|
|94|[Lizardfolk](ref/monster/lizardfolk)|+2|+2|+2|
|95-98|[Orc](ref/race/orc)|+4|+0|+0|
|99|[Troglodyte](ref/monster/troglodyte)|+0|-2|+4|
|100|Other (GM's choice)|?|?|?|

The reincarnated creature gains all abilities associated with its new form, including forms of
movement and speeds, natural armor, natural attacks, extraordinary abilities, and the like, but it
doesn't automatically speak the language of the new form.

A [wish](ref/spell/wish) or a [miracle](ref/spell/miracle) spell can restore a reincarnated
character to his or her original form.

### Reincarnation on Golarion

**Sources:** Inner Sea Races pg 193

Death is a natural part of life in the Inner Sea region, but it need not be final. Yet returning to
life is not without its perils and peculiarities. While reincarnation is a significant part of the
culture of certain races - particularly the [samsarans](ref/race/samsaran), who reincarnate
countless times over the centuries on their slow paths toward perfection and enlightenment - the use
of the spell reincarnate allows any character to experience this mystical and fundamentally
life-changing event. The table of random races presented here expands on the one presented with the
reincarnate spell. At the GM's discretion, you may use the following optional table when rolling to
determine what new body is generated when a reincarnate spell is cast. This Golarion-specific table
excludes all races that possess racial Hit Dice, but also adds in new races that are relatively
widespread and common in the region. Not all of the races appear on the following
table-[androids](ref/race/android), for example, are beyond the scope of a reincarnate spell to
create (although dead androids and [wyrwoods](ref/race/wyrwood) can themselves be reincarnated, they
have no chance of coming back in the same type of body). Others, such as
[kasathas](ref/race/kasatha) and other alien races, are not true natives of Golarion and thus lack
the "spiritual weight" needed to be included in a table of reincarnation possibilities. Of course, a
result of "GM's choice" gives each GM the opportunity to break these assumptions about allowed
incarnations as she sees fit.

When using these expanded tables, roll first on the Core Incarnations table. This table presents an
array of familiar races. Move on to the Other Incarnations table only if directed to do so. This
larger list presents a selection of less-common races from across Golarion, some of which might be
familiar to the people of the Inner Sea, while others might be almost entirely alien. If the
incarnation rolled has multiple ethnicities or heritages - as is the case with
[aasimar](ref/race/aasimar), [dhampir](ref/race/dhampir), and several similar races - randomly
determine which ethnicity or heritage applies to the new incarnation. Ability score modifiers remain
the same regardless of the final ethnicity or heritage.

#### Core Incarnations

|d%|Incarnation|Str|Dex|Con|
| --- | --- | --- | --- | --- |
|01-12|[Dwarf](ref/race/dwarf)|+0|+0|+2|
|13-24|[Elf](ref/race/elf)|+0|+2|-2|
|25-36|[Gnome](ref/race/gnome)|-2|+0|+2|
|37-48|[Half-elf](ref/race/half-elf)|+0|+2|+0|
|49-60|[Half-orc](ref/race/half-orc)|+2|+0|+0|
|61-72|[Halfling](ref/race/halfling)|-2|+2|+0|
|73-89|[Human](ref/race/human)|+0|+0|+2|
|90-99|Roll on Other Incarnations|?|?|?|
|100|GM's choice|?|?|?|

#### Other Incarnations

|d%|Incarnation|Str|Dex|Con|
| --- | --- | --- | --- | --- |
|01-05|[Aasimar](ref/race/aasimar)|+0|+0|+0|
|06-07|[Aquatic elf](ref/race/aquatic-elf)|+0|+2|-2|
|08-09|[Catfolk](ref/race/catfolk)|+0|+2|+0|
|10-11|[Changeling](ref/race/changeling)|+0|+0|-2|
|12-13|[Dhampir](ref/race/dhampir)|+0|+2|-2|
|14|[Drow](ref/race/drow)|+0|+2|-2|
|15-16|[Duergar](ref/race/duergar)|+0|+0|+2|
|17-18|[Fetchling](ref/race/fetchling)|+0|+2|+0|
|19-20|[Ghoran](ref/race/ghoran)|+0|+0|+2|
|21-22|[Gillman](ref/race/gillman)|+0|+0|+2|
|23-27|[Goblin](ref/race/goblin)|-2|+4|+0|
|28-29|[Grippli](ref/race/grippli)|-2|+2|+0|
|30-33|[Hobgoblin](ref/race/hobgoblin)|+0|+2|+2|
|34-37|[Ifrit](ref/race/ifrit)|+0|+2|+0|
|38-39|[Kitsune](ref/race/kitsune)|-2|+2|+0|
|40-44|[Kobold](ref/race/kobold)|-4|+2|-2|
|45-46|[Merfolk](ref/race/merfolk)|+0|+2|+2|
|47-48|[Nagaji](ref/race/nagaji)|+2|+0|+0|
|49-53|[Orc](ref/race/orc)|+4|+0|+0|
|54-57|[Oread](ref/race/oread)|+2|+0|+0|
|58-59|[Ratfolk](ref/race/ratfolk)|-2|+2|+0|
|60-67|[Samsaran](ref/race/samsaran)|+0|+0|-2|
|68-69|[Skinwalker](ref/race/skinwalker)|+0|+0|+0|
|70-71|[Strix](ref/race/strix)|+0|+2|+0|
|72-74|[Suli](ref/race/suli)|+2|+0|+0|
|75|[Svirfneblin](ref/race/svirfneblin)|-2|+2|+0|
|76-79|[Sylph](ref/race/sylph)|+0|+2|-2|
|80-82|[Tengu](ref/race/tengu)|+0|+2|-2|
|83-87|[Tiefling](ref/race/tiefling)|+0|+2|+0|
|88-91|[Undine](ref/race/undine)|-2|+2|+0|
|92-93|[Vanara](ref/race/vanara)|+0|+2|+0|
|94-95|[Vishkanya](ref/race/vishkanya)|+0|+2|+0|
|96-97|[Wayang](ref/race/wayang)|+0|+2|+0|
|98-99|[Wyvaran](ref/race/wyvaran)|+0|+2|+0|
|100|GM's choice|?|?|?|

### Cyclic Reincarnation

**Sources:** Arcane Anthology pg 13

This spell allows a dead creature that died no more than 1 year before the casting of the spell to
return to life in a body that closely resembles its original body; it functions as
[reincarnate](ref/spell/reincarnate) except as noted. Cyclic reincarnation returns the dead creature
to life in a new body of the same race that the target belonged to in life, and the new body appears
physically similar to the creature's previous one, to the extent that the creature could be easily
mistaken for its own offspring or kin. If the affected creature isn't a humanoid, there is a 75%
chance that the creature returns to life as a youth of its race, gaining the young creature simple
template instead (or becomes a juvenile, in the case of dragons and other creatures whose power is
determined by their age category).

You can use cyclic reincarnation on someone who was killed by a death effect or turned into an
undead creature and then destroyed, but non-humanoids so restored always return to life with the
young creature simple template (or as a juvenile, in the case of creatures whose power is determined
by their age category).

### Reincarnate Spy

**Sources:** Ultimate Intrigue pg 223

This spell functions as reincarnate except that you can cause the new body to resemble a particular
creature, matching its age category and sex and rerolling any race result that would be the wrong
size category. The subject further gains a +5 bonus on Disguise checks to impersonate the chosen
creature due to similar features, although it might take a penalty for being the wrong race.

The spell automatically leaves you with a small piece of the creature's new body, typically a lock
of hair (useful for scrying and other such spells).
