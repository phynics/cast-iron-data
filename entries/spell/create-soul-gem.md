+++
id = "ref/spell/create-soul-gem"
kind = "spell"
title = "Create Soul Gem"
source_ids = ["book-of-the-damned", "book-of-the-damned-volume-3-horsemen-of-the-apocalypse"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "create_soul_gem", path = "json/spells3.json" },
]
[[sources]]
publication = "book-of-the-damned"
page = "184"
[[sources]]
publication = "book-of-the-damned-volume-3-horsemen-of-the-apocalypse"
page = "38"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death", "evil"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S, F (crystal lens worth 500 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one dying or recently dead creature" },
]
duration = "1 day/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Arcanist, Cleric, Occultist, Oracle, Shaman, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, F (crystal lens worth 500 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level
Saving throw: Will negates
Spell resistance: yes
Target: one dying or recently dead creature
Descriptors: death, evil
:::

You draw forth the ebbing life force of a dying creature or one that has died in the past round,
focusing it through a crystal lens focus to transform into a
[soul gem](ref/monster/daemon-cacodaemon). If the creature is alive and fails its saving throw, it
dies and you capture its soul in the gem. If the creature is dead, it can still resist the spell
effect by attempting a Will save as if it were still alive. The value of the soul gem created
depends on the nature of the creature it is made from (see below). Soul gems created by this spell
crumble to dust once the spell's duration expires, releasing the trapped soul to travel on to
judgment in the Great Beyond.

Only one soul gem can be created from a dying creature. Any attempt to resurrect a body whose soul
is trapped in a soul gem requires a caster check against create soul gem's save DC. Failure results
in the [resurrection](ref/spell/resurrection) spell having no effect, while success shatters the
target's soul gem and returns the creature to life as normal. If the soul gem resides in an unholy
location, such as that created by the unhallow spell, the DC of this check increases by 2. If you
are a [souldrinker](ref/pclass/souldrinker), you can cast this spell and expend 5 soul points to
fill the gem with the equivalent of one basic soul.

### The Value of Souls

Trapped souls are one of the fundamental currencies throughout Abaddon, the Abyss, and Hell. Three
key factors influence a soul's value in the soul trade: the strength of the soul's life force (which
relates directly to the CR of the creature from which the soul was harvested), the soul's age (how
long the soul has been cycled through reincarnation, which directly relates to the sapience of the
creature from which the soul was harvested), and the soul's flavor (which is determined by factors
that include the alignment, personality, and religion of the creature from which the soul was
harvested). Of course, it's worth noting that while trading in souls may prove lucrative, the
practice is undeniably evil and an affront to the natural order, and thus it is considered to be an
evil act unless one is trading souls for an altruistic purpose (such as to smash purchased prisons
and release the souls trapped within).

**Life Force:** A soul's life force sets its base gp value. This is equal to the CR of the creature
from which the soul was harvested × 1,000. Thus, the base value of a CR 1 creature's soul is 1,000
gp, while the base value of a CR 20 creature's soul is 20,000 gp.

**Age:** A soul from a creature who in life had an Intelligence, Wisdom, or Charisma score of 2 or
less (including the lack of a score at all in one of those categories, and regardless of how high
the other ability scores were) is less refined and younger in age, and as such is worth half its
base value. Thus, the soul of a CR 1 animal with an Intelligence of 1 is worth 500 gp, while the
soul of a CR 20 vermin with no intelligence score at all would be worth 10,000 gp.

**Flavor:** As a general rule, a soul's flavor has no direct impact on its gp value for the purposes
of functioning as a material component or raw materials for magic item creation, but in certain
circumstances subject to the GM's discretion, the soul's flavor can halve or double its final value.
For example, a paladin's soul might have double its normal value to a daemon who finds lawful good
souls to be particularly delicious, while the soul of a devout worshiper of Desna might be worth
only half as much when used to create a magic item designed to be particularly deadly when used
against chaotic good creatures, since such a soul would inherently resist being used in such a way
