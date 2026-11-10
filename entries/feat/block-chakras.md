+++
id = "ref/feat/block-chakras"
kind = "feat"
title = "Block Chakras"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "block_chakras", path = "json/feat02.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/psychic-sensitivity", label = "or" },
]
[[sources]]
publication = "martial-arts-handbook"
page = "28"

[fields]
kind = "feat"
prerequisites = "Psychic Sensitivity or levels in an occult class, brawler's flurry or flurry of blows class feature, ki pool."
prerequisite_feats = ["ref/feat/psychic-sensitivity"]
benefit = "As a standard action, you can spend 1 ki point to make a single unarmed strike that attempts to block one of the target's chakras. If you hit the target and deal damage, you can select either the root, sacral, or navel chakra, as long as you can open that chakra yourself. The target suffers a specific effect based on the chosen chakra (see below), though it can reduce these effects with a successful Fortitude save (DC = 10 + half your character level + the ability modifier you use to calculate your ki pool)."
+++

You've learned how to block the lower chakras of your foes.\
**Prerequisites:** [Psychic Sensitivity](ref/feat/psychic-sensitivity) or levels in an occult class,
brawler's flurry or flurry of blows class feature, ki pool.\
**Benefit:** As a standard action, you can spend 1 ki point to make a single unarmed strike that
attempts to block one of the target's [chakras](ref/rule/activating-chakras). If you hit the target
and deal damage, you can select either the root, sacral, or navel chakra, as long as you can open
that chakra yourself. The target suffers a specific effect based on the chosen chakra (see below),
though it can reduce these effects with a successful Fortitude save (DC = 10 + half your character
level + the ability modifier you use to calculate your ki pool).

- **Root:** The target's DR is reduced by 10 for 1 minute. If the target has multiple forms of DR,
  you choose which DR is reduced. On a successful save, the target's DR is instead reduced by 5 for
  1 round.
- **Sacral:** The target can't use any of its speeds except its land speed (or swim speed for an
  aquatic creature) for 1 round, and it moves at half speed for 1 minute. If it was flying, the
  target can attempt a Fly check to fall safely. On a successful save, the target instead moves at
  half speed for 1 round.
- **Navel:** The target takes a -2 penalty on attack rolls and damage rolls, and it reduces the DCs
  of its spells and abilities by 2 for 1 minute. On a successful save, the penalty and reduction is
  halved and lasts for 1 round.
