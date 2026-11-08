+++
id = "ref/spell/summon-monster-3"
kind = "spell"
title = "Summon Monster III"
source_ids = ["core-rulebook", "monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_monster_3", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-monster-1" },
]

[fields]
kind = "spell"
school = "conjuration [see text]"
subschools = ["Summoning"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 round"
components = "V, S, F/DF (a tiny bag and a small candle)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one summoned creature" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration \[see text\]
Level: 1: Antipaladin, Arcanist, Bard, Cleric, Medium, Oracle, Psychic, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, F/DF (a tiny bag and a small candle)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one summoned creature
Subschool: Summoning
:::

## Summon Monster I

**Sources:** PRPG Core Rulebook pg 350, Monster Summoner's Handbook pg 18

This spell summons an extraplanar creature (typically an outsider, elemental, or magical beast
native to another plane). It appears where you designate and acts immediately, on your turn. It
attacks your opponents to the best of its ability. If you can communicate with the creature, you can
direct it not to attack, to attack particular enemies, or to perform other actions. The spell
conjures one of the creatures from the 1st Level list on Table 10-1. You choose which kind of
creature to summon, and you can choose a different one each time you cast the spell.

A summoned monster cannot summon or otherwise conjure another creature, nor can it use any
teleportation or planar travel abilities. Creatures cannot be summoned into an environment that
cannot support them. Creatures summoned using this spell cannot use spells or
[spell-like abilities](ref/umr/spell-like-abilities) that duplicate spells with expensive material
components (such as wish).

When you use a summoning spell to summon a creature with an alignment or elemental subtype, it is a
spell of that type. Creatures on Table 10-1 marked with an asterisk (\*) are summoned with a
template that matches your alignment.^[1](ref/spell/summon-monster-3#footnote-1)^ If you are
neutral, you may choose which template (if any) to apply to the
creature.^[2](ref/spell/summon-monster-3#footnote-2)^ Those creatures always have an alignment that
matches yours, regardless of their usual alignment. Summoning these creatures makes the summoning
spell's type match your alignment.

|Alignment|Template|
| --- | --- |
|Good|[Celestial](ref/template/celestial)|
|Evil|[Fiendish](ref/template/fiendish)|
|Lawful|[Resolute](ref/template/resolute)|
|Chaotic|[Entropic](ref/template/entropic)|

#### Table 10-1

|Level|Creature|Subtype|
| --- | --- | --- |
|1|Dire rat\*|-|
|1|Dolphin\*|-|
|1|Dog\*|-|
|1|Eagle\*|-|
|1|Fire beetle\*|-|
|1|Poisonous frog\*|-|
|1|Pony (horse)\*|-|
|1|Viper (snake)\*|-|
|2|Ant, giant (worker)\*|-|
|2|Elemental (Small)|Elemental|
|2|Giant centipede\*|-|
|2|Giant frog\*|-|
|2|Giant spider\*|-|
|2|Goblin dog\*|-|
|2|Horse\*|-|
|2|Hyena\*|-|
|2|Lemure (devil)|Evil, Lawful|
|2|Octopus\*|-|
|2|Squid\*|-|
|2|Wolf\*|-|
|3|Ant, giant (soldier)\*|-|
|3|Ape\*|-|
|3|Aurochs (herd animal)\*|-|
|3|Boar\*|-|
|3|Cheetah\*|-|
|3|Constrictor snake\*|-|
|3|Crocodile\*|-|
|3|Dire bat\*|-|
|3|Dretch (demon)|Chaotic, Evil|
|3|Electric eel\*|-|
|3|Lantern archon|Good, Lawful|
|3|Leopard (cat)\*|-|
|3|Monitor lizard\*|-|
|3|Shark\*|-|
|3|Wolverine\*|-|
|4|Ant, giant (drone)\*|-|
|4|Bison (herd animal)\*|-|
|4|Deinonychus (dinosaur)\*|-|
|4|Dire ape\*|-|
|4|Dire boar\*|-|
|4|Dire wolf\*|-|
|4|Elemental (Medium)|Elemental|
|4|Giant scorpion\*|-|
|4|Giant wasp\*|-|
|4|Grizzly bear\*|-|
|4|Hell hound|Evil, Lawful|
|4|Hound archon|Good, Lawful|
|4|Lion\*|-|
|4|Mephit (any)|Elemental|
|4|Pteranodon (dinosaur)\*|-|
|4|Rhinoceros\*|-|
|5|Agrawgh|-|
|5|Ankylosaurus (dinosaur)\*|-|
|5|Babau (demon)|Chaotic, Evil|
|5|Bearded devil|Evil, Lawful|
|5|Bralani azata|Chaotic, Good|
|5|Dire lion\*|-|
|5|Elemental (Large)|Elemental|
|5|Giant moray eel\*|-|
|5|Kyton|Evil, Lawful|
|5|Orca (dolphin)\*|-|
|5|Salamander|Evil|
|5|Woolly rhinoceros\*|-|
|5|Xill|Evil, Lawful|
|6|Dire bear\*|-|
|6|Dire tiger\*|-|
|6|Elasmosaurus (dinosaur)\*|-|
|6|Elemental (Huge)|Elemental|
|6|Elephant\*|-|
|6|Erinyes (devil)|Evil, Lawful|
|6|Giant octopus\*|-|
|6|Invisible stalker|Air|
|6|Lillend azata|Chaotic, Good|
|6|Shadow demon|Chaotic, Evil|
|6|Succubus (demon)|Chaotic, Evil|
|6|Triceratops (dinosaur)\*|-|
|7|Bebelith|Chaotic, Evil|
|7|Bone devil|Evil, Lawful|
|7|Brachiosaurus (dinosaur)\*|-|
|7|Dire crocodile\*|-|
|7|Dire shark\*|-|
|7|Elemental (greater)|Elemental|
|7|Giant squid\*|-|
|7|Mastadon (elephant)\*|-|
|7|Roc\*|-|
|7|Tyrannosaurus (dinosaur)\*|-|
|7|Vrock (demon)|Chaotic, Evil|
|8|Barbed devil|Evil, Lawful|
|8|Elemental (elder)|Elemental|
|8|Hezrou (demon)|Chaotic, Evil|
|9|Astral Deva (angel)|Good|
|9|Ghaele azata|Chaotic, Good|
|9|Glabrezu (demon)|Chaotic, Evil|
|9|Ice devil|Evil, Lawful|
|9|Nalfeshnee (demon)|Chaotic, Evil|
|9|Trumpet archon|Good, Lawful|

### Summon Monster II

**Sources:** PRPG Core Rulebook pg 352

This spell functions like [summon monster I](ref/spell/summon-monster-1), except that you can summon
one creature from the 2nd-level list or 1d3 creatures of the same kind from the 1st-level list.

### Summon Monster III

**Sources:** PRPG Core Rulebook pg 352

This spell functions like summon monster I, except that you can summon one creature from the
3rd-level list, 1d3 creatures of the same kind from the 2nd-level list, or 1d4+1 creatures of the
same kind from the 1st-level list.

### Summon Monster IV

**Sources:** PRPG Core Rulebook pg 352

This spell functions like summon monster I, except that you can summon one creature from the
4th-level list, 1d3 creatures of the same kind from the 3rd-level list, or 1d4+1 creatures of the
same kind from a lower-level list.

### Summon Monster V

**Sources:** PRPG Core Rulebook pg 352

This spell functions like summon monster I, except that you can summon one creature from the
5th-level list, 1d3 creatures of the same kind from the 4th-level list, or 1d4+1 creatures of the
same kind from a lower-level list.

### Summon Monster VI

**Sources:** PRPG Core Rulebook pg 352

This spell functions like summon monster I, except you can summon one creature from the 6th-level
list, 1d3 creatures of the same kind from the 5th-level list, or 1d4+1 creatures of the same kind
from a lower-level list.

### Summon Monster VII

**Sources:** PRPG Core Rulebook pg 352

This spell functions like summon monster I, except that you can summon one creature from the
7th-level list, 1d3 creatures of the same kind from the 6th-level list, or 1d4+1 creatures of the
same kind from a lower-level list.

### Summon Monster VIII

**Sources:** PRPG Core Rulebook pg 352

This spell functions like summon monster I, except that you can summon one creature from the
8th-level list, 1d3 creatures of the same kind from the 7th-level list, or 1d4+1 creatures of the
same kind from a lower-level list.

### Summon Monster IX

**Sources:** PRPG Core Rulebook pg 352

This spell functions like summon monster I, except that you can summon one creature from the
9th-level list, 1d3 creatures of the same kind from the 8th-level list, or 1d4+1 creatures of the
same kind from a lower-level list.

###### ^1^ {#footnote-1}

By a strict rules-as-written interpretation, regular casters can only apply the celestial or
fiendish templates, since this spell was written before the resolute and entropic templates existed.
_Bestiary 2_ introduced the resolute and entropic templates and said they could apply to summons,
but left no specifics. _Monster Summoner's Handbook_ added archetypes that could use the resolute
and entropic templates. However, Paizo's official open-content website cites _MSH_ and notes "summon
monster can be used to summon creatures with the entropic or resolute templates instead of the
celestial or fiendish template". In any event, only one template may be applied automatically to a
summoned creature: lawful good casters could choose celestial or resolute, but not both. Consult
your GM.

###### ^2^ {#footnote-2}

The original text was written before the entropic and resolute templates were created (see footnote
above), so the text generally refers to neutral on the good-evil axis only. However, a neutral good
caster could theoretically pick either resolute or entropic instead of the default celestial.
Consult your GM.
