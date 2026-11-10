+++
id = "ref/arc-vigilante/experimenter"
kind = "archetype"
title = "Experimenter"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Experimenter"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "experimenter", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "horror-adventures"
page = "70"

[fields]
kind = "archetype"
replaces = ["Vigilante specialization", "1st-level social talent", "Unshakable", "Startling appearance", "Frightening appearance", "Stunning appearance"]
alters = ["Weapon and armor proficiencies"]
replaces_features = ["vigilante-specialization", "unshakable", "startling-appearance", "frightening-appearance", "stunning-appearance"]
alters_features = ["weapon-and-armor-proficiencies"]
+++

Some vigilantes adopt lives of secrecy to hide their strange experiments from public view.

**Gained class skills:** ka, kd, ke, kg, kh, kl, kna, kno, kp, kr

**Weapon and Armor Proficiency**

**Alters:** Weapon and armor proficiencies

**Info:** Experimenters aren't proficient with martial weapons, medium armor, or shields.

**Forbidden Science (Ex)**

**Ability:** He can take alchemical discoveries in place of vigilante talents, but only discoveries
that affect his mutagen (including _cognatogen_ discoveries).

**Passive:** An experimenter gains a bonus equal to 1/2 his vigilante level on Craft (alchemy)
checks to create alchemical items and on Knowledge (engineering) checks (minimum +1). He also learns
how to craft a _mutagen_ as if he were an [alchemist](ref/class/alchemist) of his class level.

**Replaces:** Vigilante specialization

**Special:** When an experimenter is confused, dazed, frightened, panicked, or stunned, he must
attempt a Will save (DC = 20 + his vigilante level) each round at the start of his turn. If he
fails, he transforms as if he had consumed his mutagen (determine which ability score gets the bonus
randomly). This doesn't consume his mutagen, and lasts a number of rounds equal to 3 + his vigilante
level, after which the transformation ends and he becomes [fatigued](ref/misc/fatigued). While
transformed in this way, he is [confused](ref/misc/confused), and he rerolls any result of &quot&act
normally.&quot& Since the confusion is part of the mutagenic transformation, abilities that prevent
or remove confusion don't apply to this effect, though abilities that end the effect of a mutagen
work normally. He forgets everything that happened while he was involuntarily transformed.

**Mutagen (Su)**

**Action:** Info

**Flavor:** Text from the alchemist class ability.

**Gained:** At 1st Level

**Special:** As with an extract or bomb, a mutagen that is not in your possession becomes inert
until you pick it up again.

**Standard:** You can drink a mutagen to heighten your physical prowess at the cost of your
personality. You gain a +2 natural armor bonus, a +4 alchemical bonus to a physical stat, and a -2
penalty to a mental stat. See below for details.

**Usage:** A mutagen lasts for 10 minutes per alchemist level.

**Usage:** A mutagen lasts for 10 minutes per alchemist level.

You learn how to create a mutagen that you can imbibe in order to heighten your physical prowess at
the cost of your personality. It takes 1 hour to brew a dose of mutagen, and once brewed, it remains
potent until used. You can only maintain one dose of mutagen at a time - if you brew a second dose,
any existing mutagen becomes inert.

When you brew a mutagen, you select one physical ability score for it to boost - either Strength,
Dexterity, or Constitution. If the mutagen enhances your Strength, it applies a penalty to your
Intelligence. If it enhances your Dexterity, it applies a penalty to your Wisdom. If it enhances
your Constitution, it applies a penalty to your Charisma.

A non-alchemist who drinks a mutagen must make a Fortitude save (DC 10 + 1/2 your alchemist level +
your Intelligence modifier) or become [nauseated](ref/misc/nauseated) for 1 hour - a non-alchemist
can never gain the benefit of a mutagen, but you can gain the effects of another alchemist's mutagen
if you drink it. (Although if the other alchemist creates a different mutagen, the effects of the
"stolen" mutagen immediately cease.) The effects of a mutagen do not stack. Whenever you drink a
mutagen, the effects of any previous mutagen immediately end.

**Mutagenic Change (Ex)**

**Fullround:** An experimenter can consume his mutagen (if he has one) and shift from his social
identity to his vigilante identity, as if he had the [quick change](ref/soctalent/quick-change)
social talent.

**Replaces:** 1st-level social talent

**Brew Potion**

**Ability:** An experimenter gains [Brew Potion](ref/feat/brew-potion) as a bonus feat. He treats
his vigilante level as his caster level and can use Craft (alchemy) instead of Spellcraft to brew
potions.

**Gained:** At 3rd Level

**Replaces:** Unshakable

**Special:** He can use another potion of the same spell as a sample to provide the necessary spell
without consuming the potion, increasing the DC by 5.

**Lore Master (Ex)**

**Ability:** An experimenter gains the _lore master_ [bard](ref/class/bard) class feature.

**Gained:** At 5th Level

**Replaces:** Startling appearance

**Lore Master (Ex)**

**Ability:** You can take 10 on any Knowledge skill check that you have ranks in even when
threatened or distracted. You can also choose not to take 10 and can instead roll normally.

**Flavor:** Text from the bard class ability.

**At 11th Level:** You can Take 20 twice a day.

**At 17th Level:** You can Take 20 three times a day.

**Standard:** Once per day, you can take 20 on any Knowledge skill check.

**Craft Construct**

**Ability:** An experimenter gains [Craft Construct](ref/feat/craft-construct) as a bonus feat. He
treats his vigilante level as his caster level and can use Knowledge (engineering) instead of
Spellcraft to craft a construct.

**Gained:** At 11th Level

**Replaces:** Frightening appearance

**Mutable Mutagen**

**Ability:** The duration of an experimenter's mutagen increases to 1 hour per level.

**Gained:** At 17th Level

**Replaces:** Stunning appearance
