+++
id = "ref/arc-alchemist/cruorchymist"
kind = "archetype"
title = "Cruorchymist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Cruorchymist"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cruorchymist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "construct-handbook"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-poisoning" },
  { anchor = "blood-familiar", level = 1 },
  { anchor = "blood-treatment", level = 1 },
  { anchor = "blood-augmentation", level = 4 },
]
trades = [
  { replaces = "Mutagen", feature = "mutagen", by = ["blood-familiar"] },
  { replaces = "Brew Potion", feature = "brew-potion", by = ["blood-treatment"] },
  { replaces = "Poison use", feature = "poison-use", by = ["diminished-poisoning"] },
  { replaces = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["diminished-poisoning"] },
  { replaces = "Poison immunity", feature = "poison-resistance", levels = [10], by = ["diminished-poisoning"] },
  { replaces = "Swift poisoning", feature = "swift-poisoning", by = ["diminished-poisoning"] },
]
+++

Cruorchymists see their blood as just another tool for their experiments. They use this blood to
create new life that can be commanded to serve the cruorchymist's goals.

## Diminished Poisoning {#diminished-poisoning}

A cruorchymist doesn't gain the poison use, poison resistance, poison immunity, or swift poisoning
class features.

## Blood Familiar (Ex) {#blood-familiar}

A cruorchymist has created a [homunculus](ref/monster/homunculus) from basic materials and his own
blood. The homunculus takes the shape of a Tiny humanoid. It functions in all ways as a
[familiar](ref/ability/familiars), treating the cruorchymist's alchemist level as his effective
wizard level. If a cruorchymist wishes to replace his blood [familiar](ref/sidekick/familiar), he
can reduce the cost of the replacement ritual by taking 2 points of Constitution drain for every 100
gp he wishes to forgo. At 3rd level, if the cruorchymist has the infusion discovery, a blood
familiar can deliver extracts that have a range of touch for its cruorchymist master.

This replaces mutagen. A cruorchymist can never gain the mutagen, cognatogen, or inspired cognatogen
ability, even from a discovery or another class.

## Blood Treatment (Ex) {#blood-treatment}

A cruorchymist can give up some of his blood to restore his blood familiar. As a swift or immediate
action, a cruorchymist can take a number of points of
[Constitution drain](ref/rule/ability-damage-drain). His blood familiar heals 1d6 hit points for
every 1 point of Constitution drain the cruorchymist inflicts upon himself in this way.

This replaces Brew Potion.

## Blood Augmentation (Ex) {#blood-augmentation}

At 4th level, a cruorchymist can provide more of his blood to further enhance his blood familiar. As
a swift action, the cruorchymist can take 1 point of
[Constitution damage](ref/rule/ability-damage-drain) to provide his familiar with an
[animal aspect](ref/ability/animal-foci) for 1 minute, treating his alchemist level as his hunter
level. The cruorchymist takes 1 additional point of Constitution damage for every minute he
maintains the animal aspect beyond the first. At 12th level, the cruorchymist can select two animal
aspects for his blood familiar instead of one, taking 2 points of Constitution damage for every
minute that he maintains both animal aspects.
