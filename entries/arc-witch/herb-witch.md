+++
id = "ref/arc-witch/herb-witch"
kind = "archetype"
title = "Herb Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Herb%20Witch"
source_ids = ["ultimate-wilderness", "heroes-of-the-wild"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "herb_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "89"
[[sources]]
publication = "heroes-of-the-wild"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "patron-spells" },
  { anchor = "herb-lore", level = 1 },
  { anchor = "hexes" },
]
trades = [
  { replaces = "Hexes gained at 1st and 10th levels", feature = "hex", levels = [1, 10], by = ["herb-lore"] },
  { alters = "The witch's patron spells", feature = "patron-spells", power = "patron", by = ["patron-spells"] },
]
+++

Some witches dedicate their lives to the mastery of herb lore. Herb witches brew foul-tasting
medicines, sweet poisons, and other concoctions from the untamed plants of the wild.

## Patron Spells {#patron-spells}

An herb witch must choose a patron with a theme compatible with the needs of the natural world,
selected from the following list: [ancestors](ref/patron/ancestors), [animals](ref/patron/animals),
[death](ref/patron/death), [elements](ref/patron/elements), [healing](ref/patron/healing),
[plague](ref/patron/plague), [strength](ref/patron/strength), [time](ref/patron/time),
[water](ref/patron/water), [winter](ref/patron/winter), [wisdom](ref/patron/wisdom), or
[woodlands](ref/patron/woodlands).

This alters the witch's patron spells.

## Herb Lore (Ex) {#herb-lore}

Herb witches are masters of herbalism, and they can use what they gather from garden or grove to
duplicate many of the effects of alchemy. An herb witch can attempt Profession (herbalist) checks in
place of Craft (alchemy) checks, and she gains a bonus on Profession (herbalist) checks equal to
half her class level.

Herb witches are adept at brewing thick herbal cure-alls called remedies. An herb witch prepares
these remedies while communing with her familiar, during which she can prepare a number of remedies
equal to 3 + her Intelligence modifier (minimum 1 remedy). A remedy becomes inert if it leaves the
herb witch's possession, reactivating as soon as it returns to her keeping. A witch can never have
more remedies than 3 + her Intelligence modifier.

As a standard action, the herb witch can administer a remedy to herself or a creature within reach
which consumes the remedy. The herb witch attempts a Profession (herbalist) check against the save
DC of any one disease or poison currently afflicting the consumer. If she is successful, the
affliction is suppressed for 1 minute. At 10th level, if she exceeds the DC of the check by 10 or
more, the affliction immediately ends. If the disease or poison doesn't allow saving throws, the
remedy is ineffective.

An herb witch can also use a remedy to attempt to remove the blinded, deafened, fatigued, nauseated,
sickened, and staggered conditions. This requires a Profession (herbalist) check with a DC equal to
the spell or effect that caused the condition, or a DC 25 check if the condition was caused by an
effect that doesn't allow a saving throw. If the herb witch succeeds, the condition is removed
unless the condition is permanent; at 10th level, if the herb witch succeeds by 10 or more, her
remedy can remove a permanent condition.

Only a single condition, disease, or poison can be removed with each application of a remedy, and a
creature can only benefit from one herbal remedy each day, whether or not the herb witch succeeds at
her skill check.

This replaces the hexes gained at 1st and 10th levels.

## Hexes {#hexes}

An herb witch must select [cauldron](ref/hex/cauldron) as her hex at 2nd level. The following witch
hexes complement the herb witch archetype: fortune, healing, poison steep, swamp hag.

## Major Hexes {#major-hexes}

The following major hexes complement the herb witch archetype: major healing, weather control,
witch's brew.

## Grand Hexes {#grand-hexes}

The following grand hex complements the herb witch archetype: life giver.
