+++
id = "ref/arc-alchemist/fire-bomber"
kind = "archetype"
title = "Fire Bomber"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Fire%20Bomber"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fire_bomber", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "advanced-race-guide"
page = "117"

[fields]
kind = "archetype"
features = [
  { anchor = "fire-bombardier", level = 1 },
  { anchor = "fiery-cocktail", level = 4 },
  { anchor = "fire-body", level = 8 },
  { anchor = "improved-fire-body", level = 10 },
  { anchor = "greater-fire-body", level = 14 },
]
trades = [
  { replaces = "The alchemist's 4th-level discovery", feature = "discovery", levels = [4], by = ["fiery-cocktail"] },
  { replaces = "Poison resistance +6", feature = "poison-resistance", levels = [8], by = ["fire-body"] },
  { replaces = "Poison immunity", feature = "poison-resistance", levels = [10], by = ["improved-fire-body"] },
  { replaces = "Persistent mutagen", feature = "persistent-mutagen", by = ["greater-fire-body"] },
  { alters = "Bomb", feature = "bomb", by = ["fire-bombardier"] },
  { alters = "throw anything", feature = "throw-anything", by = ["fire-bombardier"] },
]
+++

Fire bombers are exceptionally good at using bombs to burn creatures and blow things up, but are not
quite as good at creating other types of bombs or extracts. A fire bomber has the following class
features.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A fire bomber treats [torches](ref/eq-misc/torch) as a simple weapon.

## Fire Bombardier (Su or Ex) {#fire-bombardier}

At 1st level, when a fire bomber throws a bomb that deals fire damage, all creatures in the splash
radius take an additional point of damage per die of fire damage dealt. Fire bombers only add their
Intelligence bonus to damage from bombs or alchemical substances that deal fire damage. This
otherwise works like the alchemist's bomb and throw anything abilities. This ability alters bomb and
throw anything.

## Bonus Feats {#bonus-feats}

A fire bomber can select the [Burn! Burn! Burn!](ref/feat/burn-burn-burn),
[Fire Tamer](ref/feat/fire-tamer), or [Flame Heart](ref/feat/flame-heart) feat in place of a
discovery.

## Fiery Cocktail (Su) {#fiery-cocktail}

At 4th level, whenever a fire bomber uses a discovery that deals damage other than fire damage, he
can split the damage dice evenly between the bomb's primary damage type and 1d6 points of fire
damage; when there is an odd number of damage dice, the odd die of damage comes from the primary
damage type. For example, an 8th-level fire bomber could throw a
[concussive bomb](ref/discovery/concussive-bomb) that deals 2d6 points of fire damage and 3d4 points
of sonic damage. Additional effects from the bomb still apply, but the save DC for admixture bombs
is reduced by 2. This replaces the alchemist's 4th-level discovery.

## Fire Body (Ex) {#fire-body}

At 8th level, a fire bomber adds _[elemental body I](ref/spell/elemental-body-1)_ to his extract
list as a 3rd-level extract. _[Elemental body](ref/spell/elemental-body-1)_ extracts prepared using
fire body are limited to [fire elementals](ref/monster/fire-elemental) only. This ability replaces
poison resistance +6.

## Improved Fire Body (Ex) {#improved-fire-body}

At 10th level, fire bombers add _[elemental body II](ref/spell/elemental-body-2)_ to their spell
list as a 4th-level extract. _Elemental body_ extracts prepared using improved fire body are limited
to fire elementals only. This ability replaces poison immunity.

## Greater Fire Body (Ex) {#greater-fire-body}

At 14th level, fire bombers add _[elemental body IV](ref/spell/elemental-body-4)_ to their spell
list as a 5th-level extract. _Elemental body_ extracts prepared using greater fire body are limited
to fire elementals only. This ability replaces persistent mutagen.

## Discoveries {#discoveries}

The following discoveries complement the fire bomber archetype:
[fire brand](ref/discovery/fire-brand), [rocket bomb](ref/discovery/rocket-bomb) (see sidebar);
explosive bombs, [fast bombs](ref/discovery/fast-bombs), [inferno bomb](ref/discovery/inferno-bomb),
[precise bombs](ref/discovery/precise-bombs) (_Advanced Player's Guide_);
[breath weapon bomb](ref/discovery/breath-weapon-bomb),
[explosive missile](ref/discovery/explosive-missile),
[immolation bomb](ref/discovery/immolation-bomb) (_Ultimate Combat_);
[bottled ooze](ref/discovery/bottled-ooze), [confusion bomb](ref/discovery/confusion-bomb),
[strafe bomb](ref/discovery/strafe-bomb) (_Ultimate Magic)_.
