+++
id = "ref/spell/genius-avaricious"
kind = "spell"
title = "Genius Avaricious"
aon = "SpellDisplay.aspx?ItemName=Genius%20Avaricious"
source_ids = ["pathfinder-30-the-twice-damned-prince"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "genius_avaricious", path = "json/spells13.json" },
]
[[sources]]
publication = "pathfinder-30-the-twice-damned-prince"
page = "68"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, M (valuable offerings; see text), F (one gold coin)"
range = "touch"
effects = [
  { label = "Effect", value = "a vestige of the archdevil Mammon imbues a coin with a negotiable degree of power" },
]
duration = "instantaneous (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 10 minutes
Components: V, S, M (valuable offerings; see text), F (one gold coin)
Range: touch
Duration: instantaneous (see text)
Saving throw: none
Spell resistance: no
Effect: a vestige of the archdevil Mammon imbues a coin with a negotiable degree of power
Subschool: Creation
Descriptors: evil
:::

Casting this spell constitutes performing a rite of sacrifice to the archdevil
[Mammon](ref/faith/mammon), making an offering to the Lord of Erebus and channeling a measure of his
disembodied might into a single coin. The power and abilities of this vestige correspond directly to
the value of the offering, allowing for three distinct effects.

_Corrupted Coin:_ Making a sacrifice worth 1,500 gp corrupts the focus into a "lucky" or "unlucky"
coin as per the caster's will for 1 month. Any creature that bears the coin gains a bonus or penalty
(decided by the caster at the time of casting) on all Appraise, Bluff, Craft, and Profession checks.
This bonus or penalty is equal to 1 per 3 caster levels (maximum +5 at 15th level). In addition, the
coin can produce an effect similar to the spell augury once per day-its flip producing a weal
(heads), woe (tails), or nothing result (landing on the edge). Potentially unknown to the bearer (if
different from the caster), the caster can telepathically hear any question asked of the coin and,
as a free action, influence the result as he chooses.

_Mammon's Mantle:_ Making a sacrifice worth 3,000 gp transforms the coin into a kind of infernal
aegis for any who swallow the coin. Upon ingesting the coin, the target gains a bonus to Charisma
equal to +1 per 3 caster levels (maximum +5 at 15th level). The bearer's blood also takes on a hue
like liquid gold and runs slowly, granting him immunity to poison, disease, and aging effects, and
causing him to automatically stabilize if reduced to fewer than 0 hit points. Additionally, the
bearer can eat gold to heal himself, regaining 1 hit point for every 20 gold pieces he consumes
(materials other than gold provide no benefit). The coin's effects last for 1 day per caster level.

_Gold Guardian:_ Making a sacrifice worth 6,000 gp allows the focus coin to animate nearby coins.
When cast into a pile of 100,000 coins, an [animate hoard](ref/monster/animate-hoard) forms under
the control of the caster. The guardian serves for 1 month. After this month, coins begin
disappearing from the guardian at a rate of 100 gp per day, reducing the creature's hit points by 1
per day. When the guardian's hit points reach 0, the guardian collapses and the focus coin is
destroyed. Coins lost from the guardian can be replaced, restoring any lost hit points.

In addition to the effects of any of these offerings, should the focus coin be swallowed, any being
sired or conceived by the creature while the magic is in effect is born as a
[tiefling](ref/race/tiefling) (bearing an indirect relation to Mammon himself).
