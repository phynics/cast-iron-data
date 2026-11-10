+++
id = "ref/arc-vigilante/psychometrist"
kind = "archetype"
title = "Psychometrist"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychometrist", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "59"

[fields]
kind = "archetype"
replaces = ["Social talent gained at 1st level", "Vigilante talents gained at 2nd, 6th, 12th, and 18th levels", "Unshakable"]
alters = ["Vengeance strike"]
replaces_features = ["unshakable"]
alters_features = ["vengeance-strike"]
+++

Wise vigilantes know that there is power in certain seemingly unremarkable items. Psychometrists
aren't spellcasters; instead, they collect strange items or create their own uncanny gadgets that
seem to only work for them. Psychometrists often hide their clandestine activities behind the guise
of an eccentric peddler, curator, tinker, or artificer.

**Gained class skills:** ka, kh

**Lost class skills:** kd, ke

**Occult Awareness**

**Ability:** A psychometrist gains [Psychic Sensitivity](ref/feat/psychic-sensitivity) as a bonus
feat.

**Gained:** At 1st Level

**Replaces:** Social talent gained at 1st level

**Implements and Focus Powers (Su)**

**Ability:** The psychometrist treats his vigilante level as his occultist level for purposes of
determining how his implements' focus powers work, and for determining at what level he may choose
certain focus powers. Unlike an occultist, each of a psychometrist's focus powers has its own
associated implement or gadget. For example, a psychometrist might own a scabbard implement to use
the _legacy weapon_ focus power and an implement that is a pair of boots to use the _sudden speed_
focus power. The psychometrist must assign mental focus separately to each implement each day, and
he doesn't gain resonant powers his implements. Otherwise, this ability acts like the occultist's
implements class feature.

**Choice:** A psychometrist learns to use the powers of one
[implement school](ref/ability/implements) from the [occultist](ref/class/occultist) class; the
conjuration implement school is not available to a psychometrist. This implement school does not
allow the psychometrist to cast any spells of that school of magic, though, and he can't use spell
trigger or spell completion magic items from any schools without succeeding at the appropriate Use
Magic Device check.

**Gained:** At 2nd Level

**Repeat:** The psychometrist learns to use one additional implement school., 0, 6

**Replaces:** Vigilante talents gained at 2nd, 6th, 12th, and 18th levels

**Special:** Each time a psychometrist learns an implement school, he learns the base focus power
from that school, plus one focus power from each implement school he has previously learned (but not
from the new school he just learned). The psychometrist can use focus powers only by expending
_mental focus_ (see below). Unless otherwise noted, the DC for any saving throw against a focus
power equals 10 + 1/2 the psychometrist's vigilante level + the psychometrist's Intelligence
modifier.

The psychometrist can select a school he already knows, and in this case, he gains a total of two
new focus powers from that school (instead of learning the base focus power from the new school).

**Mental Focus (Su)**

**Ability:** Like an occultist, a psychometrist has _mental focus_ he can invest into his implements
each day to allow him to utilize abilities tied to them. A psychometrist has a number of points of
_mental focus_ equal to [half](ref/misc/fractions-and-rounding) his vigilante level plus his
Intelligence modifier.

**Gained:** At 2nd Level

**Mental Focus (Su)**

**Action:** Ability

**Flavor:** Relevant text from the occultist class ability.

You have a number of points of mental focus; these points refresh each day. You can divide this
mental focus between your implements in any way you desire. If an implement is lost or destroyed,
the focus invested in it is lost as well, though you still refresh those points of focus normally.

Once mental focus is invested inside an implement, you can expend the mental focus stored in the
implement to activate the associated focus powers you know.

You refresh your mental focus once each day after receiving at least 8 hours of sleep. After
refreshing your mental focus, you must spend 1 hour preparing your implements and investing them
with this power. Mental focus that is not used before the next time you refresh your focus is lost.

You can choose to save generic mental focus inside your own body instead of investing all of it, but
expending this focus comes at a higher cost. Any focus power you activate with generic focus costs
twice as much mental focus to use (and to maintain, if applicable). You can expend your generic
focus through an appropriate implement on any focus power you know.

**Object Reading (Su)**

**Ability:** A psychometrist can read information from items he examines, and gains the occultist's
_[object reading](ref/spell/object-reading)_ ability.

**Gained:** At 2nd Level

**Replaces:** Unshakable

**Object Reading (Su)**

**Ability:** You learn how to read information from items you examine. Examining an item in this way
requires you to spend 1 minute handling the item. If the item is a magic item, you learn its
properties and command word as if you had successfully examined the item using
[detect magic](ref/spell/detect-magic) and succeeded at a [Spellcraft](ref/skill/spellcraft) check.
This ability does not reveal whether the item is cursed unless your class level is equal to or
greater than the caster level of the item. If the item has any historical significance, you learn
one piece of information about its past (as determined by the GM). Finally, if the item was last
used no longer than 1 day ago per your class level, you learn one piece of information about the
last creature to use the item. This information might be a glimpse of the creature's appearance, a
brief vision of what it saw while using the item, or perhaps its emotional state when it last used
the item. The GM determines what information is gained in this way. This functions like the
[psychometry occult skill unlock](ref/skill/appraise), but doesn't require a skill check and can be
used at will.

**Flavor:** Text from the occultist class ability.

**Psychometric Strike (Su)**

**Alters:** Vengeance strike

**Gained:** At 20th Level

**Passive:** A psychometrist gains twice the usual benefits of _vengeance strike_ (up to the same
maximum) against an opponent who possesses an object that once belonged to the psychometrist.
